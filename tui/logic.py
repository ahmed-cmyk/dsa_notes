from dotenv import load_dotenv
import os
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.tools import tool
from langchain_core.documents import Document
from pathlib import Path
from embeddings.vector_store import VectorStore
from embeddings.hasher import Hasher
from tools import db

load_dotenv()

MODEL_NAME = os.environ.get("CHAT_MODEL") or "deepseek"
EMBEDDING_MODEL = os.environ.get("EMBEDDING_MODEL") or "nomic-embed-text"

def _save_files_logic(folder_paths: list[str]):
    """Core logic for saving file hashes and embedding documents."""
    with db.HashDB("file_hashes.db") as hash_db:
        hash_db.initialize_db()
        
        existing_hashes = hash_db.get_all_hashes()

        hasher = Hasher(folder_paths, hash_db)
        current_hashes = hasher.start_hashing()

        new_or_modified_files = {}
        deleted_files = []

        for path, current_hash in current_hashes.items():
            if path not in existing_hashes or existing_hashes[path] != current_hash:
                new_or_modified_files[path] = current_hash
        
        for path in existing_hashes:
            if path not in current_hashes:
                deleted_files.append(path)

        hash_db.save_hashes(new_or_modified_files)
        hash_db.delete_hashes(deleted_files)

        vs = VectorStore(
            embedding_model=EMBEDDING_MODEL,
            db_path="file_hashes.db",
            use_plaintext=True
        )

        documents_to_add = []
        for path, file_hash in new_or_modified_files.items():
            file_content = Path(path).read_text(encoding='utf-8', errors='ignore')
            if vs.use_plaintext:
                file_content = vs.md_to_text(file_content)
            documents_to_add.append(Document(page_content=file_content, metadata={"path": path, "hash": file_hash, "type": "markdown"}))
        
        if documents_to_add:
            vs.embed_documents(documents_to_add)
        if deleted_files:
            vs.delete_documents(deleted_files)

@tool
def ai_embed_documents(folder_paths: list[str] = ['./algorithms', './data_structures']):
    """Saves file hashes in db and then converts files into vector embeddings to store in vector store.
    Can be called by the AI to update its knowledge base.
    """
    _save_files_logic(folder_paths)
    return "Knowledge base updated."

def get_chain():
    chat_model = ChatOllama(model=MODEL_NAME)
    chat_model_with_tools = chat_model.bind_tools([ai_embed_documents])

    prompt = ChatPromptTemplate.from_messages([
        SystemMessage(
            content="""
                    You are an AI that helps people figure out which algorithms to use for leetcode problems.
                    Your knowledge base is derived from documents in the 'algorithms' and 'data_structures' folders.
                    When a user names a problem, you should reply with the recommended algorithm and its time complexity.
                    If the user asks you to update your knowledge base or process new algorithm/data structure files,
                    you can use the `ai_embed_documents` tool.
                    
                    Based on the user's query, I have retrieved the following relevant documents:
                    {context}
                    """
        ),
        MessagesPlaceholder(variable_name="msgs")
    ])
    
    return prompt | chat_model_with_tools | StrOutputParser()

def get_retriever():
    return VectorStore(embedding_model=EMBEDDING_MODEL).get_retriever()

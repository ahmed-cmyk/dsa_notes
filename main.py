from dotenv import load_dotenv
import os
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from rich import print
from rich.panel import Panel
from rich.prompt import Prompt
import sqlite3
from embeddings.vector_store import VectorStore
from embeddings.hasher import Hasher
from tools import db
import typer

load_dotenv()

app = typer.Typer()
MODEL_NAME = os.environ.get("CHAT_MODEL") or "deepseek"

chat_model = ChatOllama(model=MODEL_NAME)
prompt = ChatPromptTemplate([
    SystemMessage(
        content="""
                You are an AI that helps people figure out which algorithms to use for leetcode problems. When a
                user names a problem you are supposed to reply with the recommended algorithm and the time complexity. 

                The format you should use is as follows:
                algorithm: [algorithm_name]
                time complexity: [complexity]
                description: [description]
                pseudocode: [pseudocode]
                """
    ),
    MessagesPlaceholder("msgs")
])

# parse text from message objects irrespective of the format of the underlying content
chain = prompt | chat_model | StrOutputParser()

msgs = []

@app.command()
def chat():
    message = Prompt.ask("[bold blue]user")
    
    while message != "/quit" and message != "/q":
        msgs.append(message)
        print("[bold red]system:", end=" ")
        for chunk in chain.stream({"msgs": msgs}):
            print(chunk, end='')

        print()
        message = Prompt.ask("[bold blue]user")

@app.command()
def save_files():
    hasher = Hasher(['./algorithms', './data_structures'])
    hashes = hasher.start_hashing()
    with db.HashDB("file_hashes.db") as b:
        b.initialize_db()
        b.save_hashes(hashes)

    vs = VectorStore(
        embedding_model=os.environ.get("EMBEDDING_MODEL", "nomic-text-embed"),
        db_path="file_hashes.db",
        use_plaintext=True  # set False if you want raw Markdown
    )
    vs.embed_documents()

def save_to_db():
    with sqlite3.connect('document.db') as connection:
        cursor = connection.cursor()

def main():
    app()
    print("Hello from dsa-notes!")


if __name__ == "__main__":
    main()

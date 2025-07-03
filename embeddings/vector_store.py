from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings
from langchain_core.documents import Document
from pathlib import Path
import sqlite3
import markdown
from bs4 import BeautifulSoup


def md_to_text(md_str: str) -> str:
    """
    Convert Markdown to plain text by rendering it to HTML then stripping tags.
    """
    html = markdown.markdown(md_str)
    soup = BeautifulSoup(html, "html.parser")
    return soup.get_text()


class VectorStore:
    def __init__(self, embedding_model: str, db_path: str, use_plaintext: bool = False):
        """
        :param embedding_model: name of the embedding model to use (for Ollama)
        :param db_path: path to your SQLite DB containing file paths and hashes
        :param use_plaintext: if True, strips markdown formatting before embedding
        """
        self.embeddings = OllamaEmbeddings(model=embedding_model)
        self.db_path = db_path
        self.use_plaintext = use_plaintext

        self.vector_store = Chroma(
            collection_name="dsa_collection",
            embedding_function=self.embeddings,
            persist_directory="./data/"
        )

    def get_file_records(self):
        """
        Fetch (path, hash) tuples from SQLite.
        """
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT path, hash FROM file_hashes")
            return cursor.fetchall()

    def embed_documents(self):
        """
        Main function — embed all documents, updating only if changed.
        """
        records = self.get_file_records()

        for path_str, db_hash in records:
            path = Path(path_str)

            if not path.is_file():
                print(f"⚠️ Skipping missing file: {path}")
                continue

            # check if already embedded & up-to-date
            existing = self.vector_store.get(where={"path": str(path)})

            if (
                existing
                and "metadatas" in existing
                and len(existing["metadatas"]) > 0
                and existing["metadatas"][0].get("hash") == db_hash
            ):
                print(f"✅ No changes detected: {path}")
                continue

            # prepare content
            raw_md = path.read_text(encoding='utf-8', errors='ignore')
            if self.use_plaintext:
                content = md_to_text(raw_md)
            else:
                content = raw_md

            doc = Document(
                page_content=content,
                metadata={
                    "path": str(path),
                    "hash": db_hash,
                    "type": "markdown"
                }
            )

            # delete old version (if exists)
            self.vector_store.delete(where={"path": str(path)})

            # add updated document
            self.vector_store.add_documents([doc])
            print(f"♻️ Updated embedding: {path}")

        print("✅ Vector store updated & saved to disk.")

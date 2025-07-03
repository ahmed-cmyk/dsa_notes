from dotenv import load_dotenv
import os
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from rich import print
from rich.prompt import Prompt
import sqlite3
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
                """
    ),
    MessagesPlaceholder("msgs")
])

# parse text from message objects irrespective of the format of the underlying content
chain = prompt | chat_model | StrOutputParser()

msgs = []

@app.command()
def chat():
    message = Prompt.ask("user")
    
    while message != "/quit":
        msgs.append(message)
        print("system:", end=" ")
        for chunk in chain.stream({"msgs": msgs}):
            print(chunk, end='')

        print("\n")
        message = Prompt.ask("user")

def goodbye(name: str):
    print(f"Goodbye, {name}")
    raise typer.Exit()

def save_to_db():
    with sqlite3.connect('document.db') as connection:
        cursor = connection.cursor()

def main():
    app()
    print("Hello from dsa-notes!")


if __name__ == "__main__":
    main()

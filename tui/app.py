from textual.app import App, ComposeResult
from textual.containers import Container
from textual.widgets import Footer, Header
from textual.reactive import reactive
from textual import work

from tui.widgets import AppTitle, ChatBox, UserInput
from tui.logic import get_chain, get_retriever

from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.runnables import RunnablePassthrough
from operator import itemgetter


class ChatApp(App):
    CSS_PATH = "app.tcss"

    chain = reactive(None)
    retriever = reactive(None)
    msgs = reactive([])

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initialize_ai()

    def initialize_ai(self):
        self.retriever = get_retriever()
        chain = get_chain()
        
        self.chain = (
            {
                "context": itemgetter("msgs") | self.retriever,
                "msgs": itemgetter("msgs"),
            }
            | chain
        )

    def compose(self) -> ComposeResult:
        yield Header(name="DSA CLI")
        yield AppTitle(id="app-title")
        with Container(id="app-grid"):
            yield ChatBox(id="chat-box")
            yield UserInput(id="user-input")
        yield Footer()

    def on_user_input_submitted(self, message: UserInput.UserInputSubmitted) -> None:
        chat_box = self.query_one("#chat-box", ChatBox)
        chat_box.write(f"[bold blue]You:[/bold blue] {message.value}")

        self.msgs.append(HumanMessage(content=message.value))

        self.get_ai_response()

    @work(exclusive=True)
    async def get_ai_response(self) -> None:
        user_input = self.query_one(UserInput)
        user_input.toggle_disabled()

        chat_box = self.query_one("#chat-box", ChatBox)
        ai_response = ""
        
        async for chunk in self.chain.astream({"msgs": self.msgs}):
            ai_response += chunk
        
        chat_box.write(f"[bold green]Agent:[/bold green] {ai_response}")

        self.msgs.append(AIMessage(content=ai_response))
        user_input.toggle_disabled()

    def on_button_pressed(self) -> None:
        self.exit()


if __name__ == "__main__":
    app = ChatApp()
    app.run()

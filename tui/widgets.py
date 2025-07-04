from textual.app import RenderResult
from textual.widgets import Label, RichLog, Input
from textual.containers import Container
from textual.message import Message


class AppTitle(Label):
    """Display the title of the app"""

    def render(self) -> RenderResult:
        return "DSA Helper CLI"


class ChatBox(RichLog):
    """A widget to display chat messages."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.auto_scroll = True

    def write(self, message: str):
        self.write_line(message)


class UserInput(Container):
    """A widget for user input."""

    class UserInputSubmitted(Message):
        """Message to be posted when user input is submitted."""

        def __init__(self, value: str) -> None:
            super().__init__()
            self.value = value

    def compose(self) -> RenderResult:
        yield Input(placeholder="Ask me about an algorithm...")

    def on_input_submitted(self, event: Input.Submitted) -> None:
        if event.value:
            self.post_message(self.UserInputSubmitted(event.value))
            event.input.value = ""

    def toggle_disabled(self) -> None:
        self.query_one(Input).disabled = not self.query_one(Input).disabled

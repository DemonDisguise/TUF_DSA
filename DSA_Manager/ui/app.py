import subprocess

from textual.app import App, ComposeResult
from textual.widgets import (
    Header,
    Footer,
    Input,
    DataTable,
    Static,
    Button
)

from textual.containers import Vertical, Horizontal

from core.scanner import Scanner
from core.indexer import Indexer
from core.search import SearchEngine


class DSAManagerApp(App):

    CSS = """
    Screen {
        background: #0f172a;
        color: #e2e8f0;
    }

    Header {
        background: #111827;
        color: #60a5fa;
    }

    Footer {
        background: #111827;
        color: #93c5fd;
    }

    #search {
        margin: 1 2 0 2;
        border: solid #3b82f6;
        background: #111827;
        color: #f8fafc;
    }

    #table {
        margin: 1 2;
        height: 1fr;

        background: #111827;

        border: solid #334155;

        color: #f8fafc;
    }

    #stats {
        height: 1;

        margin: 0 2 1 2;

        color: #94a3b8;
    }
    
    #topbar {
        height: 3;
        margin: 1 2 0 2;
    }

    .mode-btn {
        margin-left: 1;
        min-width: 12;
    }
    """

    BINDINGS = [
        ("q", "quit", "Quit"),
        ("r", "refresh", "Refresh"),
        ("/", "focus_search", "Search"),
        ("escape", "clear_search", "Clear"),
    ]

    def __init__(self):

        super().__init__()

        self.problems = []

        self.filtered = []
        
        self.search_mode = "all"

    def compose(self) -> ComposeResult:

        yield Header()

        yield Vertical(

            Horizontal(

                Input(
                    placeholder="Search problems...",
                    id="search"
                ),

                Button(
                    "All",
                    id="mode_all",
                    classes="mode-btn"
                ),

                Button(
                    "Title",
                    id="mode_title",
                    classes="mode-btn"
                ),

                Button(
                    "Topic",
                    id="mode_topic",
                    classes="mode-btn"
                ),

                Button(
                    "Subtopic",
                    id="mode_subtopic",
                    classes="mode-btn"
                ),

                id="topbar"
            ),

            DataTable(
                zebra_stripes=True,
                cursor_type="row",
                id="table"
            ),

            Static(
                id="stats"
            )
        )

        yield Footer()

    def on_mount(self):

        self.title = "DSA Problem Manager"

        self.sub_title = "VS Code Workspace Explorer"

        self.load_problems()

        table = self.query_one(DataTable)

        table.add_columns(
            "Title",
            "File",
            "Main Topic",
            "Sub Topic",
            "Relative Path",
            "Lang"
        )

        table.cursor_type = "row"

        table.focus()

        self.update_table(self.problems)

    def load_problems(self):

        problems = Indexer.load()

        if problems is None:

            scanner = Scanner(".")

            problems = scanner.scan()

            Indexer.save(problems)

        self.problems = problems

        self.filtered = problems

    def update_table(self, problems):

        table = self.query_one(DataTable)

        table.clear()

        for problem in problems:

            table.add_row(

                problem.title,

                problem.filename,

                problem.main_topic,

                problem.sub_topic,

                problem.rel_path,

                problem.extension
            )

        stats = self.query_one("#stats", Static)

        stats.update(

            f"Problems: {len(problems)}"
        )

    def on_input_changed(self, event: Input.Changed):

        query = event.value.strip()

        self.filtered = SearchEngine.search(

            query,

            self.problems,
            
            self.search_mode
        )

        self.update_table(self.filtered)
    
    def on_button_pressed(
        self,
        event: Button.Pressed
    ):

        button_id = event.button.id

        if button_id == "mode_all":

            self.search_mode = "all"

        elif button_id == "mode_title":

            self.search_mode = "title"

        elif button_id == "mode_topic":

            self.search_mode = "topic"

        elif button_id == "mode_subtopic":

            self.search_mode = "subtopic"

        self.notify(
            f"Search Mode: {self.search_mode}"
        )

        query = self.query_one("#search", Input).value

        self.filtered = SearchEngine.search(

            query,

            self.problems,

            self.search_mode
        )

        self.update_table(self.filtered)

    def on_data_table_row_selected(

        self,

        event: DataTable.RowSelected

    ):

        row_index = event.cursor_row

        if row_index >= len(self.filtered):

            return

        problem = self.filtered[row_index]

        try:

            # Opens INSIDE current VS Code workspace
            subprocess.run(

                f'code -r "{problem.abs_path}"',

                shell=True
            )

        except Exception as e:

            self.notify(

                f"Failed to open file: {e}",

                severity="error"
            )

    def action_refresh(self):

        self.notify("Refreshing index...")

        scanner = Scanner(".")

        self.problems = scanner.scan()

        Indexer.save(self.problems)

        self.filtered = self.problems

        self.update_table(self.problems)

        self.notify(

            f"Indexed {len(self.problems)} problems"
        )

    def action_focus_search(self):

        self.query_one("#search", Input).focus()

    def action_clear_search(self):

        search = self.query_one("#search", Input)

        search.value = ""

        self.filtered = self.problems

        self.update_table(self.problems)
from ipywidgets import widgets
from IPython.display import display


class BlockTimestampsUI:
    def __init__(self, api_handler, table_manager, start_page=1):
        """
        Initializes the UIManager.

        Args:
            api_handler (APIHandler): An instance of the APIHandler class.
            table_manager (TableManager): An instance of the TableManager class.
            start_page (int): The initial page to display.
        """
        self.api_handler = api_handler
        self.table_manager = table_manager
        self.current_page = start_page
        self.output_area = widgets.Output()
        self.loading_label = widgets.Label(value="")
        self.prev_button = widgets.Button(description="Previous Page", disabled=True)
        self.next_button = widgets.Button(description="Next Page")
        self.initialize_buttons()

    def initialize_buttons(self):
        """
        Set up button click handlers and initial states.
        """
        self.prev_button.on_click(self.prev_page_callback)
        self.next_button.on_click(self.next_page_callback)

    def update_buttons(self):
        """
        Enable or disable buttons based on the current page.
        """
        self.prev_button.disabled = self.current_page == 1

    def fetch_and_render(self, page):
        """
        Fetch data and render the table for the given page.
        """
        self.loading_label.value = "Loading..."
        self.output_area.clear_output(wait=True)
        with self.output_area:
            data = self.api_handler.fetch_data(page)
            if data:
                self.table_manager.render_table(data["response"]["result"]["data"])
            else:
                print("Failed to fetch data")
        self.loading_label.value = ""

    def next_page_callback(self, _):
        """
        Handle next page button click.
        """
        self.current_page += 1
        self.update_buttons()
        self.fetch_and_render(self.current_page)

    def prev_page_callback(self, _):
        """
        Handle previous page button click.
        """
        if self.current_page > 1:
            self.current_page -= 1
            self.update_buttons()
            self.fetch_and_render(self.current_page)

    def render_ui(self):
        """
        Render the complete user interface.
        """
        button_box = widgets.HBox([self.prev_button, self.next_button])
        display(widgets.VBox([button_box, self.loading_label, self.output_area]))
        self.fetch_and_render(self.current_page)

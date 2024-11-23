import pandas as pd
from ipywidgets import widgets, HTML
from IPython.display import display, clear_output


class TableManager:
    def __init__(self, table_width="100%"):
        self.table_width = table_width

    def render_table(self, data):
        pass
        df = pd.DataFrame(data)
        table_style = f"""
            <style>
                table {{ width: {self.table_width}; margin: auto; }}
            </style>
        """
        display(HTML(table_style))
        display(df)
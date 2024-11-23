from src.ui_manager import BlockTimestampsUI
from src.table_manager import TableManager
from src.chain_insights_client import ChainInsightsClient


def get_block_timestamps_ui(network, page_size, start_page, table_width):
    api_handler = ChainInsightsClient(network=network, page_size=page_size)
    table_manager = TableManager(table_width=table_width)
    block_timestamps_ui = BlockTimestampsUI(api_handler=api_handler, table_manager=table_manager, start_page=start_page)
    return block_timestamps_ui

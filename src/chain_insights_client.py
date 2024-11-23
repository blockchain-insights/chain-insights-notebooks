import requests

class ChainInsightsClient:

    def __init__(self, network, page_size):
        self.base_url = f"http://185.239.209.254:9900/v1/balance-tracking/{network}/timestamps"
        self.page_size = page_size

    def fetch_data(self, page):
        """
        Fetch data from the API for the given page.

        Args:
            page (int): The page number to fetch.

        Returns:
            dict: JSON response or None if an error occurs.
        """
        try:
            response = requests.get(
                f"{self.base_url}?page={page}&page_size={self.page_size}&response_type=json",
                headers={"accept": "application/json"}
            )
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error fetching data: {e}")
            return None

import pandas as pd

CSV_SEPARATOR = ","

class Loader:

    def load_dataset(self, url: str) -> pd.DataFrame:
        return pd.read_csv(url, delimiter=CSV_SEPARATOR)
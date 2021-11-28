from foo.importer.reader import Reader
import pandas as pd


class CsvReader(Reader):

    def __init__(self):
        self.data = None

    def load(self, param):
        file_path = param["path"]
        # 将excel转换成DataFrame
        self.data = pd.read_csv(file_path, encoding="utf8")

    def get_value(self, column: int, row: int):
        return self.data.iat[row, column]

    def get_row(self, row: int):
        return self.data.iloc[row]

    def get_size(self) -> int:
        # df.shape[0] 或 len(df) 返回行数; df.shape[1] 返回列数; 
        return self.data.shape[0]

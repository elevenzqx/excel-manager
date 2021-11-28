from foo.outputer.writer import Writer
import pandas as pd


class CsvWriter(Writer):

    def __init__(self):
        self.path = ''

    def load(self, param):
        self.path = param["value"]

    def wirte(self, df : pd.DataFrame, param):
        # 将excel转换成DataFrame
        df.to_csv(self.path)

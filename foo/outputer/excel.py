import pandas as pd
from foo.importer.reader import Reader


class ExcelWriter(Reader):

    def __init__(self):
        self.path = ''

    def load(self, param):
        self.path = param["value"]

    def write(self, df: pd.DataFrame, param):
        # 将excel转换成DataFrame
        df.to_excel(self.path, sheet_name='biubiu')

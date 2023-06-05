import pandas as pd


# 定义抽象的输出器
class Writer:
    def load(self, param):
        pass

    def write(self, df: pd.DataFrame, param):
        pass


writers = {}


# 注册读取器
def register(name, w: Writer):
    writers[name] = w


def writer(name) -> Writer:
    return writers[name]

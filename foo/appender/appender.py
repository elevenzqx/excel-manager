import pandas as pd


# 定义抽象的输出器
class Appender:
    def load(self, param):
        pass

    def append(self, data, param) -> pd.DataFrame:
        pass


appends = {}


# 注册读取器
def register(name, append: Appender):
    appends[name] = append


def appender(name) -> Appender:
    return appends[name]

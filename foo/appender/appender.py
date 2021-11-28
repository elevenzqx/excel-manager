import pandas as pd

# 定义抽象的输出器
class Appender:
    def load(self, param):
        pass

    def append(self, data, param) -> pd.DataFrame:
        pass



appenders = {}


# 注册读取器
def register(name, appender: Appender):
    appenders[name] = appender


def appender(name) -> Appender:
    return appenders[name]

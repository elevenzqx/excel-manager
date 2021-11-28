import pandas as pd

# 定义抽象的输出器
class Writer:
    def load(self, param):
        pass

    def wirte(self, df : pd.DataFrame, param):
        pass



writers = {}


# 注册读取器
def register(name, writer: Writer):
    writers[name] = writer


def outputer(name) -> Writer:
    return writers[name]

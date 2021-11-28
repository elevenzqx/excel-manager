# 定义抽象的读取器
class Reader:
    def load(self, param):
        pass

    def get(self, column) -> str:
        pass


readers = {}


# 注册读取器
def register(name, reader: Reader):
    readers[name] = reader


def get_reader(name) -> Reader:
    return readers[name]

# 定义抽象的读取器
class Reader:
    def load(self, param):
        pass

    def get_value(self, column: int, row: int):
        pass

    def get_row(self, row: int):
        pass

    def get_size(self) -> int:
        pass


readers = {}


# 注册读取器
def register(name, reader: Reader):
    readers[name] = reader


def importer(name) -> Reader:
    return readers[name]

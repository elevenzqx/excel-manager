# 定义抽象的拦截器
class Filter:
    def load(self, column, value: str, match: bool):
        pass

    def filter(self, row) -> bool:
        pass


filters = {}


# 注册拦截器
def register(name, f: Filter):
    filters[name] = f


# 获取拦截器
def get_filter(name) -> Filter:
    return filters[name]

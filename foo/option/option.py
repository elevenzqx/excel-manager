# 定义抽象的读取器
class Handler:
    # 抽象的执行器，用于进行运算处理
    def handle(self, row, option, data):
        pass


handlers = {}


# 注册读取器
def register(name, h: Handler):
    handlers[name] = h


def get_handler(name) -> Handler:
    return handlers[name]

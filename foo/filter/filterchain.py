from foo.filter.filter import get_filter


class FilterChain:
    def __init__(self) -> None:
        self.chain = []

    def add(self, option):
        f = get_filter(option["name"])
        f.load(option["column"], option["value"], option["match"])
        self.chain.append(f)

    def do_filter(self, row) -> bool:
        for f in self.chain:
            if not f.filter(row):
                return False
        return True

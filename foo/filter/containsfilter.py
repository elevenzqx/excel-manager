from foo.filter.filter import Filter


class ContainsFilter(Filter):

    def __init__(self):
        self.values = ""
        self.match = bool(1)
        self.column = ""

    def load(self, column, value: str, match: bool):
        self.values = value.split(",")
        self.match = match
        self.column = column

    def filter(self, row) -> bool:
        for key in self.values:
            row_value = row[self.column]
            if key in row_value:
                return self.match
        return not self.match

from foo.group.group import Reader
import re


class RegxReader(Reader):

    def __init__(self):
        self.pattern = None
        self.index = 0

    def load(self, param):
        self.pattern = re.compile(param["value"])
        self.index = param["index"]

    def get(self, column) -> str:
        m = self.pattern.search(column)
        if m:
            return m.group(self.index)
        return ""


class NoneReader(Reader):

    def __init__(self):
        self.value = ""

    def load(self, param):
        self.value = param["value"]

    def get(self, column) -> str:
        return self.value

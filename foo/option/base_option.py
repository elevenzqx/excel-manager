from foo.option.option import Handler


class CountHandler(Handler):

    def handle(self, row, option, data):
        if option["name"] not in data:
            data[option["name"]] = 1
            return
        data[option["name"]] += 1


class SumHandler(Handler):

    def handle(self, row, option, data):
        if option["name"] not in data:
            data[option["name"]] = row[option["column"]]
            return
        data[option["name"]] += row[option["column"]]


class TextHandler(Handler):

    def handle(self, row, option, data):
        data[option["name"]] = row[option["column"]]

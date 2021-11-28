from foo.appender.appender import Appender
import pandas as pd


class GroupAppender(Appender):

    def __init__(self):
        self.path = ''

    def load(self, param):
        self.path = param["value"]

    def append(self, data, param) -> pd.DataFrame:
        # df = pd.DataFrame.from_dict(group_map, orient="index")
        datas = {}
        for x in param["value"]:
            # x["input"][x["outter"]
            pass
        return None


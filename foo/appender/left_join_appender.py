from foo.appender.appender import Appender
import pandas as pd


class LeftJoinAppender(Appender):

    def __init__(self):
        self.path = ''

    def load(self, param):
        self.path = param["value"]

    def append(self, data, param) -> pd.DataFrame:
        output_data = {}
        for x in param["value"]:
            option_type = x["type"]
            if option_type == "main" or option_type == "join":
                data_input = data[x["input"]]
                data_out = data_input[x["outter"]]
                for key, value in data_out.items():
                    real_key = key
                    if "dict" in x:
                        if key in x["dict"]:
                            real_key = x["dict"][key]
                    if real_key in output_data:
                        for k in value:
                            output_data[real_key][k] = value[k]
                    else:
                        if option_type == "main":
                            output_data[real_key] = value
            else:
                pass

        df = pd.DataFrame.from_dict(output_data, orient="index")
        return df


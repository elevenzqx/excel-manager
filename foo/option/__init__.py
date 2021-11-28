from foo.option.option import register
from foo.option.base_option import *

register("count", CountHandler())
register("sum", SumHandler())
register("text", TextHandler())

from foo.filter.filter import register
from foo.filter.containsfilter import *

register("contains", ContainsFilter())

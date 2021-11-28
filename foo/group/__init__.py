from foo.group.group import register
from foo.group.base_group import *

register("regx", RegxReader())
register("none", NoneReader())

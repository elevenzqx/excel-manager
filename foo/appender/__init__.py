from foo.appender.appender import register
from foo.appender.group_appender import *

register("group-appender", GroupAppender())

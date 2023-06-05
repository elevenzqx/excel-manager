from foo.appender.appender import register
from foo.appender.left_join_appender import *

register("left-join-appender", LeftJoinAppender())

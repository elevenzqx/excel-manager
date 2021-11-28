from foo.outputer.writer import register
from foo.outputer.excel import *
from foo.outputer.csv import *

register("csv", CsvWriter())
register("excel", ExcelWriter())

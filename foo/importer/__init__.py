from foo.importer.reader import register
from foo.importer.excel import *
from foo.importer.csv import *

register("csv", CsvReader())
register("excel", ExcelReader())

import os, sys
from collections import namedtuple
import csv

with open("files.csv", "rb") as f:
    reader = csv.reader(f)
    fields = reader.next()
    Row = namedtuple("Row", fields)

    files = [Row(*row) for row in reader]

for f in files[:10]:
    print f

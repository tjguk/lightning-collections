import os, sys
from collections import defaultdict
import csv

files = defaultdict(list)

with open("files.csv", "rb") as f:
    for path, name, _, _ in csv.reader(f):
        files[path].append(name)

for file in files['C:\\Python27\\']:
    print file

file_counts = defaultdict(int)

with open("files.csv", "rb") as f:
    for path, name, _, _ in csv.reader(f):
        file_counts[path] += 1

print file_counts['C:\\Python27\\']

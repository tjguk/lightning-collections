import os, sys
import csv

from winsys import fs

python_dirpath = fs.file(sys.executable).path
with open("files.csv", "wb") as f:
    writer = csv.writer(f)
    writer.writerow(["Path", "Name", "Size", "Modified"])

    for f in python_dirpath.flat():
        writer.writerow([f.path, f.name, f.size, f.written_at])

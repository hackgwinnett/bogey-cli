import os

root = "database/"
txt = ".txt"
csv = "csv"

def clear():
    files = os.listdir(root)
    filelen = len(files)

    for x in range(0, filelen - 1):
        if txt or csv in files[x]:
            files.pop(x)

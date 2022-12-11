import os.path
from typing import List


def two_lists_files(path: str, exp: str, flag: bool) -> List:
    res = [[], []]
    for root, dirs, files in os.walk(path):
        res[0] = files
        if flag is True:
            for sub_files in files:
                res[0].append(sub_files)

    return res[0]


print(two_lists_files("C:/Dev/files_2", ".txt", True))

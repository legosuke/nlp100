# -*- coding: utf-8 -*-

"""
14. 先頭からN行を出力
    自然数Nをコマンドライン引数などの手段で受け取り，
    入力のうち先頭のN行だけを表示せよ．確認にはheadコマンドを用いよ．
"""

import sys
from typing import List

def head(in_file_path: str, N: int) -> List[str]:
    with open(in_file_path, mode="r") as fin:
        return fin.readlines()[:N]

def main() -> None:
    N = int(sys.argv[1])
    head_n = head("./popular-names.txt", N)
    for s in head_n:
        print(s, end="")

if __name__ == "__main__":
    main()
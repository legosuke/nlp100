# -*- coding: utf-8 -*-

"""
15. 末尾のN行を出力Permalink
    自然数Nをコマンドライン引数などの手段で受け取り，
    入力のうち末尾のN行だけを表示せよ．確認にはtailコマンドを用いよ．
"""

import sys
from typing import List

def tail(in_file_path: str, N: int) -> List[str]:
    with open(in_file_path, mode="r") as fin:
        return fin.readlines()[-N:]

def main() -> None:
    N = int(sys.argv[1])
    tail_n = tail("./popular-names.txt", N)
    for s in tail_n:
        print(s, end="")

if __name__ == "__main__":
    main()
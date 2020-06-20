# -*- coding: utf-8 -*-

"""
19. 各行の1コラム目の文字列の出現頻度を求め，出現頻度の高い順に並べるPermalink
    各行の1列目の文字列の出現頻度を求め，その高い順に並べて表示せよ．
    確認にはcut, uniq, sortコマンドを用いよ．
"""

import pathlib
from collections import Counter

def cut(in_file_path: str, out_file_path: str, c: int) -> None:
    with open(in_file_path, mode="r") as fin, open(out_file_path, mode="w") as fout:
        fout.write("\n".join(s.split()[c] for s in fin))

def main() -> None:
    in_file_path = "./popular-names.txt"

    out_dir = "dst19"
    out_file_path = out_dir + "/col1.txt"
    pathlib.Path(out_dir).mkdir(exist_ok=True)
    cut(in_file_path, out_file_path, 0)

    in_file_path = out_file_path
    with open(in_file_path, mode="r") as fin:
        count_of_string = Counter([s[:-1] for s in fin.readlines()])
        sorted_list = sorted(count_of_string.items(), key=lambda x: x[1], reverse=True)
        for s in sorted_list:
            print(f"{s[0]} : {s[1]} 回")

if __name__ == "__main__":
    main()
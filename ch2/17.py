# -*- coding: utf-8 -*-

"""
17. １列目の文字列の異なり
    1列目の文字列の種類（異なる文字列の集合）を求めよ．
    確認にはcut, sort, uniqコマンドを用いよ．
"""

import pathlib

def cut(in_file_path: str, out_file_path: str, c: int) -> None:
    with open(in_file_path, mode="r") as fin, open(out_file_path, mode="w") as fout:
        fout.write("\n".join(s.split()[c] for s in fin))

def main() -> None:
    in_file_path = "./popular-names.txt"

    out_dir = "dst17"
    out_file_path = out_dir + "/col1.txt"
    pathlib.Path(out_dir).mkdir(exist_ok=True)
    cut(in_file_path, out_file_path, 0)

    in_file_path = out_file_path
    with open(in_file_path, mode="r") as fin:
        set_of_strings = set(s[:-1] for s in fin.readlines())
        for s in set_of_strings:
            print(s)

if __name__ == "__main__":
    main()
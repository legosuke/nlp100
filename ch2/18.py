# -*- coding: utf-8 -*-

"""
18. 各行を3コラム目の数値の降順にソートPermalink
    各行を3コラム目の数値の逆順で整列せよ（注意: 各行の内容は変更せずに並び替えよ）．
    確認にはsortコマンドを用いよ（この問題はコマンドで実行した時の結果と合わなくてもよい）．
"""

import pathlib

def sort_by_column(in_file_path: str, out_file_path: str, c: int) -> None:
    with open(in_file_path, mode="r") as fin, open(out_file_path, mode="w") as fout:
        lines = sorted([s.split() for s in fin.readlines()], key=lambda x: int(x[c]), reverse=True)
        for s in lines:
            fout.write(" ".join(s) + "\n")

def main() -> None:
    in_file_path = "./popular-names.txt"

    out_dir = "dst18"
    out_file_path = out_dir + "/sorted.txt"
    pathlib.Path(out_dir).mkdir(exist_ok=True)
    
    sort_by_column(in_file_path, out_file_path, 2)

if __name__ == "__main__":
    main()
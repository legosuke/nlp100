# -*- coding: utf-8 -*-

"""
13. col1.txtとcol2.txtをマージPermalink
    12で作ったcol1.txtとcol2.txtを結合し，
    元のファイルの1列目と2列目をタブ区切りで並べたテキストファイルを作成せよ．
    確認にはpasteコマンドを用いよ．
"""

import shutil, pathlib

def paste(in_file_path1: str, in_file_path2: str, out_file_path: str) -> None:
    with open(in_file_path1, mode="r") as fin1, open(in_file_path2, mode="r") as fin2, open(out_file_path, mode="w") as fout:
        fout.write("".join(f"{s1.rstrip()}\t{s2}" for s1, s2 in zip(fin1.readlines(), fin2.readlines())))

def main() -> None:
    in_dir = "dst12"
    in_dir_path = pathlib.Path(in_dir)
    assert(in_dir_path.exists())

    out_dir = "dst13"
    out_dir_path = pathlib.Path(out_dir)
    if out_dir_path.exists():
        shutil.rmtree(out_dir_path)
    out_dir_path.mkdir(exist_ok=True)

    paste(in_dir + "/col1.txt", in_dir + "/col2.txt", out_dir + "/col1col2.txt")

if __name__ == "__main__":
    main()
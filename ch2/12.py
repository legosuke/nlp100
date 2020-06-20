# -*- coding: utf-8 -*-

"""
12. 1列目をcol1.txtに，2列目をcol2.txtに保存
    各行の1列目だけを抜き出したものをcol1.txtに，
    2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．
    確認にはcutコマンドを用いよ．
"""

import shutil, pathlib

def cut(in_file_path: str, out_file_path: str, c: int) -> None:
    with open(in_file_path, mode="r") as fin, open(out_file_path, mode="w") as fout:
        fout.write("\n".join(s.split()[c] for s in fin))

def main() -> None:
    path = "./popular-names.txt"

    out_dir = "dst12"
    out_dir_path = pathlib.Path(out_dir)
    if out_dir_path.exists():
        shutil.rmtree(out_dir_path)
    out_dir_path.mkdir(exist_ok=True)
    
    cut(path, out_dir + "/col1.txt", 0)
    cut(path, out_dir + "/col2.txt", 1)

if __name__ == "__main__":
    main()
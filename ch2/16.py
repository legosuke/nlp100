# -*- coding: utf-8 -*-

"""
16. ファイルをN分割するPermalink
    自然数Nをコマンドライン引数などの手段で受け取り，
    入力のファイルを行単位でN分割せよ．同様の処理をsplitコマンドで実現せよ．
"""

import sys, shutil, pathlib


def split(in_file_path: str, N: int) -> None:
    # 出力用のディレクトリを作る
    out_dir = "dst16"
    out_dir_path = pathlib.Path(out_dir)
    if out_dir_path.exists():
        shutil.rmtree(out_dir_path)
    out_dir_path.mkdir(exist_ok=True)

    # 入力ファイルをN分割する
    with open(in_file_path, mode="r") as fin:
        lines = fin.readlines()
        for i in range(0, len(lines), N):
            out_file_path = out_dir + "/data" + str(i // N)
            with open(out_file_path, mode="w") as fout:
                fout.writelines("".join(s for s in lines[i:i+N]))

def main() -> None:
    N = int(sys.argv[1])
    split("./popular-names.txt", N)

if __name__ == "__main__":
    main()
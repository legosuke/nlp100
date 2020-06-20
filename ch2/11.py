# -*- coding: utf-8 -*-

"""
11. タブをスペースに置換
    タブ1文字につきスペース1文字に置換せよ．
    確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．
"""

def main() -> None:
    path = "./popular-names.txt"

    with open(path, mode="r") as f:
       for s in f:
           print(s.replace("\t", " "), end="")

if __name__ == "__main__":
    main()
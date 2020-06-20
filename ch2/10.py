# -*- coding: utf-8 -*-

"""
10. 行数のカウント
    行数をカウントせよ．確認にはwcコマンドを用いよ．
"""

def main() -> None:
    path = "./popular-names.txt"

    with open(path, mode="r") as f:
       print(len(f.readlines()))

if __name__ == "__main__":
    main()
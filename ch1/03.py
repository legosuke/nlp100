# -*- coding: utf-8 -*-

"""
03. 円周率
    “Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.”
    という文を単語に分解し，各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ．
"""

import re

def main() -> None:
    s = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
    length_list = list(map(len, re.split(r",*\s|\.", s)))[:-1]
    print(length_list)

if __name__ == "__main__":
    main()
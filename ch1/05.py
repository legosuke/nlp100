# -*- coding: utf-8 -*-

"""
05. n-gram
    与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．
    この関数を用い，”I am an NLPer”という文から単語bi-gram，文字bi-gramを得よ．
"""

from typing import List, Sequence, TypeVar

T = TypeVar('T')

def n_gram(s: Sequence[T], n: int) -> List[Sequence[T]]:
    return [s[i:i+n] for i in range(len(s)-n+1)]

def main() -> None:
    s = "I am an NLPer"
    print(n_gram(s, 2))

    word_list = s.split()
    print(n_gram(word_list, 2))


if __name__ == "__main__":
    main()
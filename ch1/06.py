# -*- coding: utf-8 -*-

"""
06. 集合
    “paraparaparadise”と”paragraph”に含まれる文字bi-gramの集合を，
    それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．
    さらに，’se’というbi-gramがXおよびYに含まれるかどうかを調べよ．
"""

from typing import List, Sequence, TypeVar

T = TypeVar('T')

def n_gram(s: Sequence[T], n: int) -> List[Sequence[T]]:
    return [s[i:i+n] for i in range(len(s)-n+1)]

def main() -> None:
    s_list = ["paraparaparadise", "paragraph"]
    X, Y = [set(n_gram(s, 2)) for s in s_list]
    
    print(X.union(Y))
    print(X.intersection(Y))
    print(X.difference(Y))
    print("se" in X)
    print("se" in Y)

if __name__ == "__main__":
    main()
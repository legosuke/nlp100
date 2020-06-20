# -*- coding: utf-8 -*-

"""
07. テンプレートによる文生成Permalink
    引数x, y, zを受け取り「x時のyはz」という文字列を返す関数を実装せよ．
    さらに，x=12, y=”気温”, z=22.4として，実行結果を確認せよ．
"""

def text(x: int, y: str, z: float) -> str:
    return f"{x}時の{y}は{z}"

def main() -> None:
    x, y, z = 12, "気温", 22.4
    print(text(x, y, z))

if __name__ == "__main__":
    main()
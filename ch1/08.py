# -*- coding: utf-8 -*-

"""
08. 暗号文Permalink
    与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．
    - 英小文字ならば(219 - 文字コード)の文字に置換
    - その他の文字はそのまま出力
    この関数を用い，英語のメッセージを暗号化・復号化せよ．
"""

def cipher(s: str) -> str:
    return "".join(chr(219 - ord(c)) if c.islower() else c for c in s)

def main() -> None:
    s = "Hello World."
    encode_s = cipher(s)
    decode_s = cipher(encode_s)
    print(encode_s)
    print(decode_s)

if __name__ == "__main__":
    main()
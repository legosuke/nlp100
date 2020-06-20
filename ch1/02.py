# -*- coding: utf-8 -*-

"""
02. 「パトカー」＋「タクシー」＝「パタトクカシーー」
    「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．
"""

def main() -> None:
    s_list = ["パトカー", "タクシー"]
    t = ""
    for i in range(4):
        t += s_list[0][i] + s_list[1][i]
    print(t)

if __name__ == "__main__":
    main()
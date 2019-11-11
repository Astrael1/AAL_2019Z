# -*- coding: utf-8
import re
import codecs
import sys
from table import *

def test1(n: int):
    m = MixingTable()
    for i in range(n):
        word = input()
        m.add(word)
    m.writeAll()

def test2(n: int):
    m = MixingTable()
    for i in range(n):
        word = input()
        m.remove(word)


def main():
    test2(3)

if __name__== "__main__":
    main()
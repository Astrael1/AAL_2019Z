# -*- coding: utf-8
from table import *

def main():
    m = MixingTable()
    m.add('a')
    m.add('b')
    m.add('c')
    m.writeAll()

if __name__== "__main__":
    main()
# -*- coding: utf-8
from table import *

def main():
    m = MixingTable()
    string = 'abc'
    where = m.add(string)
    print(m.content[where].storedString, m.content[where].count)

if __name__== "__main__":
    main()
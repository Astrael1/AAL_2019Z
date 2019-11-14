# Szymon Malolepszy, 293149
# -*- coding: utf-8
import re
import codecs
import sys
from table import *

def test1(output):
    m = MixingTable()
    
    n = input()
    n = int(n)
    for i in range(n):
        word = input()
        m.add(word)
    if output == True:
        m.writeAll()

def test2(output):
    m = MixingTable()
    n = input()
    n = int(n)
    for i in range(n):
        word = input()
        m.remove(word)
    if output == True:
        m.writeAll()

def test3(output):
    m = MixingTable()
    n = input()
    n = int(n)
    for i in range(n):
        word = input()
        m.add(word)
    k = input()
    k = int(k)
    for i in range(k):
        word = input()
        m.remove(word)
    if output == True:
        m.writeAll()

def test4():
    n = input()
    n = int(n)
    m = MixingTable()
    for i in range(n):
        word = input()
        m.add(word)
    m.writeAll()

def showInstruction():
    with open('program_instruction.txt', 'r') as f:
        instruction = f.read()
        print(instruction)

def main():
    writeOutput = False
    if '-v' in sys.argv:
        writeOutput = True
    if len(sys.argv) == 1:
        showInstruction()
    elif sys.argv[1] == '-t1':
        test1(writeOutput)
    elif sys.argv[1] == '-t2':
        test2(writeOutput)
    elif sys.argv[1] == '-t3':
        test3(writeOutput)
    elif sys.argv[1] == '-t4':
        test4()
    else:
        showInstruction()

if __name__== "__main__":
    main()
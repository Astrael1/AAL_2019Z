# Szymon Malolepszy, 293149
# mixing table
# -*- coding: utf-8
import re
import codecs
import sys
import time
from table import *

def test1(output, writeTime):
    m = MixingTable()
    
    n = input()
    n = int(n)
    start = time.clock()
    for i in range(n):
        word = input()
        m.add(word)
    if writeTime == True:
        elapsed = (time.clock() - start) * 1000
        print(elapsed)
    if output == True:
        m.writeAll()

def test2(output, writeTime):
    m = MixingTable()
    n = input()
    n = int(n)
    start = time.clock()
    for i in range(n):
        word = input()
        m.remove(word)
    if writeTime == True:
        elapsed = (time.clock() - start) * 1000
        print(elapsed)
    if output == True:
        m.writeAll()

def test3(output, writeTime):
    m = MixingTable()
    n = input()
    n = int(n)
    for i in range(n):
        word = input()
        m.add(word)
    k = input()
    k = int(k)
    start = time.clock()
    for i in range(k):
        word = input()
        m.remove(word)
    if writeTime == True:
        elapsed = (time.clock() - start) * 1000
        print(elapsed)
    
    if output == True:
        m.writeAll()

def test4(writeTime):
    n = input()
    n = int(n)
    m = MixingTable()
    for i in range(n):
        word = input()
        m.add(word)
    start = time.clock()
    m.getAll()
    if writeTime == True:
        elapsed = (time.clock() - start) * 1000
        print(elapsed)

def showInstruction():
    with open('program_instruction.txt', 'r') as f:
        instruction = f.read()
        print(instruction)

def main():
    writeOutput = False
    writeTime = False
    if '-v' in sys.argv:
        writeOutput = True
    if '-t' in sys.argv:
        writeTime = True
    if len(sys.argv) == 1:
        showInstruction()
    elif sys.argv[1] == '-t1':
        test1(writeOutput, writeTime)
    elif sys.argv[1] == '-t2':
        test2(writeOutput, writeTime)
    elif sys.argv[1] == '-t3':
        test3(writeOutput, writeTime)
    elif sys.argv[1] == '-t4':
        test4(writeTime)
    else:
        showInstruction()

if __name__== "__main__":
    main()

# -*- coding: utf-8
class Structure:
    def __init__(self):
        self.storedString = ''
        self.count = 0

class MixingTable:
    def __init__(self, hashingBase = 300, k = 102499):
        self.k = k
        self.hashingBase = hashingBase
        self.content = []
        for i in range(k):
            self.content.append(Structure())
    def hash(self, string, previous = 0):
        index = 0
        if isinstance(string, str) == False:
            raise TypeError('MixingTable.hash: string expected')
        for char in string:
            index *= self.hashingBase
            index += ord(char) + previous
            index %= self.k
        return index
    def add(self, string):
        if isinstance(string, str) == False:
            raise TypeError('MixingTable.add: string expected')
        previousIndeces = set()
        lastIndex = 0
        done = False
        while done == False:
            index = self.hash( string, lastIndex)
            if previousIndeces.__contains__(index):
                raise RuntimeError('MixingTable.add: hash function looped')
            if self.content[index].count == 0:
                self.content[index].count = 1
                self.content[index].storedString = string
                done = True
            elif self.content[index].storedString == string:
                self.content[index].count += 1
                done = True
            else:
                lastIndex = index
                previousIndeces.add(index)
            
            return index

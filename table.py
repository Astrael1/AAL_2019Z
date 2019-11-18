# Szymon Malolepszy, 293149
# mixing table
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
    def hash(self, string: str, previous = 0):
        index = 0
        for char in string:
            index *= self.hashingBase
            index += ord(char) + previous
            index %= self.k
        return index
    def add(self, string: str):
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
    def remove(self, string: str):
        previousIndeces = set()
        lastIndex = 0
        index = self.hash( string, lastIndex)
        done = False
        while previousIndeces.__contains__(index) == False and done == False:
            if self.content[index].storedString == string:
                self.content[index].count -= 1
                if self.content[index].count == 0:
                    self.content[index].storedString = ''
                done = True
            lastIndex = index
            previousIndeces.add(index)
            index = self.hash( string, lastIndex)
        return done
    
    def writeAll(self):
        for struct in self.content:
            for i in range(struct.count):
                print(struct.storedString)
    def getAll(self):
        result = []
        for struct in self.content:
            for i in range(struct.count):
                result.append(struct.storedString)
        return result




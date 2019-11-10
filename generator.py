# -*- coding: utf-8
import re
import codecs
import json




def configure():
    arraySize = 400
    endNumber = 399
    transitionArray = []
    lettersArray = [0] * arraySize

    for i in range(arraySize):
        transitionArray.append([0] * arraySize)

    f = codecs.open('/home/osboxes/Desktop/AAL/repo/text_probe.txt', 'r', 'utf-8')
    for line in f:
        line = re.sub("[-!.,;\n]", "", line)
        for word in line.split():
            firstCharacter = word[0]
            lastCharacter = word[-1]
            #mark 'beginning' -> 'first character' transition
            index = ord(firstCharacter)
            transitionArray[0][index] += 1
            #mark 'last character' -> 'end' transition
            index = ord(lastCharacter)
            transitionArray[index][endNumber] += 1
            #mark last character in character array
            lettersArray[index] += 1
            for i in range(1, len(word)):
                firstCharacter = word[i-1]
                lastCharacter = word[i]
                index1 = ord(firstCharacter)
                index2 = ord(lastCharacter)
                lettersArray[index1] += 1
                transitionArray[index1][index2] += 1
    with open("config.json", 'w') as f:
        json.dump(transitionArray, f, ensure_ascii=False, indent=4)
        json.dump(lettersArray, f, ensure_ascii=False)

def read():
    with open('config.json', 'r') as f:
        data = f.read()

def main():
    read()

if __name__== "__main__":
    main()


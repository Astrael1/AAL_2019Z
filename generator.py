# Szymon Malolepszy, 293149
# mixing table
# -*- coding: utf-8
import re
import codecs
import json
import random
import sys

# end of word code
EOW = 399

def configure(filename=''):
    arraySize = 400
    transitionArray = []
    lettersArray = [0] * arraySize

    for i in range(arraySize):
        transitionArray.append([0] * arraySize)

    if filename=='':
        f = codecs.open('text_probe.txt', 'r', 'utf-8')
    else:
        f = codecs.open(filename, 'r', 'utf-8')
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
            transitionArray[index][EOW] += 1
            for i in range(1, len(word)):
                firstCharacter = word[i-1]
                lastCharacter = word[i]
                index1 = ord(firstCharacter)
                index2 = ord(lastCharacter)
                transitionArray[index1][index2] += 1

    for idx, val in enumerate(transitionArray):
        count = 0
        for number in val:
            count += number
        lettersArray[idx] = count
    f.close()
             
    with open("config.json", 'w') as f:
        results = [ transitionArray, lettersArray ]
        json.dump(results, f, ensure_ascii=False, indent=4)

def generateWords(n, outputFile='', howToWrite = 'w'):
    with open('config.json', 'r') as f:
        data = f.read()
        result = json.loads(data)
    
    transitionArray = result[0]
    lettersArray = result[1]
    resultsToWrite = []
    for i in range(n):
        generatedWord = ''
        # code of last letter added
        index = 0
        while index != EOW:
            maximum = lettersArray[index]
            randomizer = random.randint(0, maximum)
            # code of next letter to add
            index2 = 0
            while randomizer > 0:
                index2 += 1
                randomizer -= transitionArray[index][index2]
            if index2 != EOW and index2 != 0:
                    try:
                        generatedWord = generatedWord + unichr(index2)
                    except ValueError as identifier:
                        print("Niefajny kod:" + str(index2))
                    
            index = index2
        resultsToWrite.append(generatedWord)
    if outputFile == '':
        print(n)
        for word in resultsToWrite:
            print(word)
    else:
        with codecs.open(outputFile, howToWrite, 'utf-8') as f:
            f.write(str(len(resultsToWrite)))
            f.write('\n')
            for word in resultsToWrite:
                f.write(word + '\n')

def generateWordsN(n, length, outputFile='', howToWrite = 'w'):
    with open('config.json', 'r') as f:
        data = f.read()
        result = json.loads(data)
    
    transitionArray = result[0]
    lettersArray = result[1]
    resultsToWrite = []
    for i in range(int(n)):
        generatedWord = ''
        # code of last letter added
        index = 0
        for i in range(int(length)):
            maximum = lettersArray[index]
            randomizer = random.randint(1, maximum)
            # code of next letter to add
            index2 = 0
            while randomizer > 0:
                index2 += 1
                randomizer -= transitionArray[index][index2]
            if index2 != EOW:
                    try:
                        generatedWord = generatedWord + unichr(index2)
                    except ValueError as identifier:
                        print("Niefajny kod:" + str(index2))
            else:
                index2 = ord('a')
                generatedWord = generatedWord + 'a'
                    
            index = index2
        resultsToWrite.append(generatedWord)
    if outputFile == '':
        print(n)
        for word in resultsToWrite:
            print(word)
    else:
        with codecs.open(outputFile, howToWrite, 'utf-8') as f:
            f.write(str(len(resultsToWrite)))
            f.write('\n')
            for word in resultsToWrite:
                f.write(word + '\n')

def showInstruction():
    with open('generator_instruction.txt', 'r') as f:
        instruction = f.read()
        print(instruction)

def main():

    howToWrite = 'w'
    if '-o' in sys.argv:
        filename = sys.argv[sys.argv.index('-o') + 1]
        if '-a' in sys.argv:
            howToWrite = 'a'
    else:
        filename = ''
    
    
    if len(sys.argv) == 1 or '-h' in sys.argv:
        showInstruction()
    elif sys.argv[1] == '-c':
        configure()
    elif sys.argv[1] == '-g':
        if '-n' in sys.argv:
            wordCount = sys.argv[sys.argv.index('-n') + 1]
            generateWordsN(int(sys.argv[2]), wordCount, filename, howToWrite)
        else:
            generateWords(int(sys.argv[2]), filename, howToWrite)
    else:
        showInstruction()

if __name__== "__main__":
    main()
# -*- coding: utf-8
import re
import codecs
from table import *


def main():
    m = MixingTable()
    f = codecs.open('/home/osboxes/Desktop/AAL/repo/text_probe.txt', 'r', 'utf-8')
    for line in f:
        line = re.sub("[-!.,;\n]", "", line)
        for word in line.split():
            m.add(word)
    m.writeAll()

if __name__== "__main__":
    main()
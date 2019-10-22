# -*- coding: utf-8 -*-

import random
import time
import sys
import os

text = raw_input("Enter text in English: ")

def getRandomChar():
    return chr(random.randint(32, 127))

def printLine(line):
    sys.stdout.write("\r")
    sys.stdout.write(line)
    sys.stdout.flush()

chars = list(text)

invalidCharacters = [char for char in chars if ord(char) < 32 or ord(char) > 127]

if (len(invalidCharacters) > 0):
    print "Your text has invalid characters. Good bye!"
    sys.exit(os.EX_IOERR)

textLength = len(chars)
newTextChars = ['']*textLength 
index = 0

while (index < textLength):
    newTextChars[index] = getRandomChar()

    printLine(''.join(newTextChars))
    time.sleep(0.01)

    if (newTextChars[index] == chars[index]):
        index += 1

printLine(''.join(newTextChars))
print
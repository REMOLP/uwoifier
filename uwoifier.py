import sys
import random
import argparse
import re
#from typing import List, Tuple, Dict

# Constants
UWU_WORDS = ['uwu', 'uWu', 'UwU', 'Uwu', 'uwU', 'UWU']
OWO_WORDS = ['owo', 'oWo', 'OwO', 'Owo', 'owO', 'OWO']

def readFile(file_name):
    with open(file_name, 'r', encoding="utf-8") as f:
        return f.readlines()

def getArgs():
    parser = argparse.ArgumentParser(description='uwoifier - a simple script that takes the input (either from a file or in a interactive repl) and returns back string with randomly changed words but in a way that still makes sense in terms of UwU or OwO.')
    parser.add_argument('-f', '--file', help='Input text file name', type=str)
    parser.add_argument('-i', '--interactive', help='Interactive mode', action='store_true')
    parser.add_argument('-m', '--mode', help='Mode of program. It can be \'uwu\', \'owo\' or \'mix\'', type=str)
    args = parser.parse_args()
    if not args.file and not args.interactive:
        parser.print_help()
        sys.exit(1)
    return (args.file, args.interactive, args.mode)

def getRandomWord(mode):
    if mode == 'uwu':
        return random.choice(UWU_WORDS)
    elif mode == 'owo':
        return random.choice(OWO_WORDS)

def getRandomWordWithContext(mode, word):
    # Gets a random word from the list of words based on the mode with the context of the previous word.
    if mode == 'uwu':
        if word == 'o' or word == 'O':
            return random.choice(['u', 'U']) + random.choice(UWU_WORDS)
        elif word == 'u' or word == 'U':
            return random.choice(['o', 'O']) + random.choice(UWU_WORDS)
        else:
            return random.choice(['u', 'U']) + random.choice(UWU_WORDS)
    elif mode == 'owo':
        if word == 'o' or word == 'O':
            return random.choice(['w', 'W']) + random.choice(OWO_WORDS)
        elif word == 'w' or word == 'W':
            return random.choice(['o', 'O']) + random.choice(OWO_WORDS)
        else:
            return random.choice(['w', 'W']) + random.choice(OWO_WORDS)

def uwuMode(line):
    line = re.sub(r'(?<![uo])u(?![uo])', getRandomWord('uwu'), line)
    line = re.sub(r'(?<![uo])U(?![uo])', getRandomWord('uwu').upper(), line)
    line = re.sub(r'(?<![ow])o(?![ow])', getRandomWord('uwu'), line)
    line = re.sub(r'(?<![ow])O(?![ow])', getRandomWord('uwu').upper(), line)
    return line

def owoMode(line):
    line = re.sub(r'(?<![ow])o(?![ow])', getRandomWord('owo'), line)
    line = re.sub(r'(?<![ow])O(?![ow])', getRandomWord('owo').upper(), line)
    line = re.sub(r'(?<![uo])u(?![uo])', getRandomWord('owo'), line)
    line = re.sub(r'(?<![uo])U(?![uo])', getRandomWord('owo').upper(), line)
    return line


def mixMode(line):
    # Mix mode. Mix both UwU and OwO.
    # Works kinda meh :/
    line = re.sub(r'(?<=[^uo])(u)(?=[^uo])', getRandomWordWithContext('uwu', 'u'), line)
    line = re.sub(r'(?<=[^uo])(U)(?=[^uo])', getRandomWordWithContext('uwu', 'U').upper(), line)
    line = re.sub(r'(?<=[^ow])(o)(?=[^ow])', getRandomWordWithContext('owo', 'o'), line)
    line = re.sub(r'(?<=[^ow])(O)(?=[^ow])', getRandomWordWithContext('owo', 'O').upper(), line)
    return line

def main():
    file_name, interactive, mode = getArgs()
    if interactive:
        try:
            while True:
                line = input('> ')
                if mode == 'uwu':
                    print(uwuMode(line))
                elif mode == 'owo':
                    print(owoMode(line))
                elif mode == 'mix':
                    print(mixMode(line))
                else:
                    print(mixMode(line))
        except KeyboardInterrupt:
            print("\n\nPapa ^^ UwU OwO")
    else:
        lines = readFile(file_name)
        for line in lines:
            if mode == 'uwu':
                print(uwuMode(line))
            elif mode == 'owo':
                print(owoMode(line))
            elif mode == 'mix':
                print(mixMode(line))
            else:
                print(mixMode(line))

if __name__ == '__main__':
    main()

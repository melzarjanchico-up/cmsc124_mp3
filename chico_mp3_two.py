"""
    FILE:       chico_mp3_numbertwo.py
    ABOUT:      Implements a recursive-descent (predictive) parser for a given grammar.

    NAME:       Melzar Jan E. Chico
    COURSE:     CMSC124 B
    DATE:       8 Novemeber 2021
    TASK:       Machine Problem 3 - Lexical and Syntax Analysis (No. 2)

    NOTICE:     The grammar was modified in accordance "to I see fit that it accepts correct inputs"
                Here's the final grammar:
                    <integer> ::= [+|-] <num>
                    <num> ::= <digit><num'>
                    <num'> ::= <digit><num'> | .<decimal> | e
                    <decimal> ::= <digit><decimal'>
                    <decimal'> ::= <digit><decimal'> | e
                    <digit> ::= 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9
"""

class numberParser:
    def __init__(self, strLine) -> None:
        self.__strLine = strLine
        self.__currChar = None
        self.__currPos = -1
        self.__isError = False
        self.nextChar()

    def nextChar(self):
        self.__currPos += 1

        if self.__currPos >= len(self.__strLine):
            # Forced '$' incase user forgot the dollar sign
            self.__currChar = '$'
        else:
            self.__currChar = self.__strLine[self.__currPos]

    def match(self, char):
        return self.__currChar == char

    def start(self):
        self.integer()

        # Checks if the parser read the string entirely
        if not self.match('$') or (self.match('$') and self.__currPos < len(self.__strLine)-1):
            self.__isError = True

        return (True if not self.__isError else False)

    ##### PROCEDURES IN THE GRAMMAR RULES BELOW #####
    def integer(self):
        if self.match('+') or self.match('-'):
            self.nextChar()
        self.number()

    def number(self):
        self.digit()
        self.number_prime()

    def number_prime(self):
        if self.__currChar.isnumeric():
            self.digit()
            self.number_prime()
        elif self.match('.'):
            self.nextChar()
            self.decimal()
        else:
            pass

    def decimal(self):
        self.digit()
        self.decimal_prime()

    def decimal_prime(self):
        if self.__currChar.isnumeric():
            self.digit()
            self.decimal_prime()
        else:
            pass

    def digit(self):
        if self.__currChar in ['0','1','2','3','4','5','6','7','8','9']:
            self.nextChar()
        else:
            self.__isError = True

def inputPrompt():
    print('(MP3 #2) Enter string: ', end='')
    inputStr = input()
    return inputStr

def main():
    inputString = inputPrompt()

    while inputString != 'exit':
        # Parser segment
        parser = numberParser(inputString)
        print('String is ACCEPTED.\n' if parser.start() else 'String is NOT ACCEPTED.\n')

        inputString = inputPrompt()

main()
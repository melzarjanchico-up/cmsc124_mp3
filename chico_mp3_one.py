"""
    FILE:       chico_mp3_one.py
    ABOUT:      A class that that does recursing parsing for the first grammar in the MP3

    NAME:       Melzar Jan E. Chico
    COURSE:     CMSC124 B
    DATE:       8 Novemeber 2021
    TASK:       Machine Problem 3 - Lexical and Syntax Analysis (No. 1)

    NOTICE:     The grammar was modified in accordance "that I see fit that it accepts correct inputs"
                Here's the final grammar:
                    <expr> ::= <term><expr'>
                    <expr'> ::= +<term><expr'> | -<term><expr'> | e
                    <term> ::= <factor><term'>
                    <term'> ::= *<factor><term'> | /<factor><term'> | e
                    <factor> ::= (<expr>) | <digit>
                    <digit> ::= 0 | 1 | 2 | 3
"""

class ArithmeticParser:
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
        self.expression()

        # Checks if the parser read the string entirely
        if not self.match('$') or (self.match('$') and self.__currPos < len(self.__strLine)-1):
            self.__isError = True

        return (True if not self.__isError else False)

    ##### PROCEDURES IN THE GRAMMAR RULES BELOW #####
    def expression(self):
        self.term()
        self.expression_prime()

    def expression_prime(self): # note: this procedure can be further simplified.
        if self.match('+'):     # <expr'> ::= +<term><expr'>
            self.nextChar()
            self.term()
            self.expression_prime()
        elif self.match('-'):   # <expr'> ::= -<term><expr'>
            self.nextChar()
            self.term()
            self.expression_prime()
        else:                   # <expr'> ::= e (this can be removed too, just added this for clarity)
            pass

    def term(self):
        self.factor()
        self.term_prime()
    
    def term_prime(self):       # note: this procedure can be further simplified.
        if self.match('*'):     # <term'> ::= *<factor><term'>
            self.nextChar()
            self.factor()
            self.term_prime()
        elif self.match('/'):   # <term'> ::= /<factor><term'>
            self.nextChar()
            self.factor()
            self.term_prime()
        else:                   # <term'> ::= e (this can be removed too, just added this for clarity)
            pass

    def factor(self):
        if self.match('('):
            self.nextChar()
            self.expression()
            if self.match(')'):
                self.nextChar()
            else:
                self.__isError = True
        elif self.__currChar in ['0','1','2','3']:  # This could be self.digit(), but it's redundant
            self.nextChar()
        else:
            self.__isError = True

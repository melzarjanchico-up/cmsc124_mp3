from chico_mp3_one import ArithmeticParser
from chico_mp3_two import NumberParser

def inputPrompt(gramMode):
    print(f'\t(For #{gramMode}) Input string: ', end='')
    inputStr = input()
    return inputStr

def main():
    print('Machine Problem 3: Lexical/Syntax Analysis')
    print('by Melzar Jan Chico - CMSC124B')
    grammarMode = None

    while grammarMode != '3':
        print('\nSelect between:\n\t[1] arithmetic parsing\n\t[2] number parsing\n\t[3] exit')
        print('Input selection: ', end='')

        inputString = ''
        grammarMode = input()

        if grammarMode == '1':
            print('\n\tType your strings. Type \'exit\' to go back.')
            while inputString != 'exit':
                inputString = inputPrompt(1)
                if inputString == 'exit':
                    break

                # Parser segment
                parser = ArithmeticParser(inputString)
                print('\tString is ACCEPTED.\n' if parser.start() else '\tString is NOT ACCEPTED.\n')

        elif grammarMode == '2':
            print('\n\tType your strings. Type \'exit\' to go back.')
            while inputString != 'exit':
                inputString = inputPrompt(2)
                if inputString == 'exit':
                    break

                # Parser segment
                parser = NumberParser(inputString)
                print('\tString is ACCEPTED.\n' if parser.start() else '\tString is NOT ACCEPTED.\n')

        elif grammarMode == '3':
            break

        else:
            print('Invalid choice. Try again.')

main()
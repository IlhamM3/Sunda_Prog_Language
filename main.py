import suns_interpreter
import suns_lexer
import suns_parser

from sys import *

if __name__ == '__main__':
    lexer = suns_lexer.sunslexer()
    parser = suns_parser.sunsparser()
    env = {}
    while True:
        try:
            text = input('suns > ')
        except EOFError:
            break
        if text:
            tree = parser.parse(lexer.tokenize(text))
            suns_parser.sunsparser(tree, env)
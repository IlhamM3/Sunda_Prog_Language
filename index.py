import suns_lexer
import suns_parser
import suns_interpreter

from sys import *

# EXECUTE FROM FILE BAHASAKU.suns
lexer = suns_lexer.sunslexer()
parser = suns_parser.sunsparser()
env = {}

file = open(argv[1])
text = file.readlines()
for line in text:
    tree = parser.parse(lexer.tokenize(line))
    suns_interpreter.sunsinterpreter(tree, env)

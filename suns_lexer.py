from sly import Lexer

class sunslexer (Lexer):
    tokens = {NAME, NUMBER, STRING, IF, THEN, ELSE,
              FOR, TO, ARROW, EQEQ, FUN, PRINT, ERROR}
    ignore = ' \t '
    literals = {'=', '+', '-', '/', '*',
                '(', ')', ',', ';', '<', ">"}

    # Tokens
    PRINT = r'nyitak'
    IF = r'upami'
    THEN = r'teras'
    ELSE = r'henteu'
    FOR = r'kahatur'
    TO = r'kanggo'
    FUN = r'fungsi'
    ERROR = r'lepat'
    NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'
    STRING = r'\".*?\"'
    ARROW = r'->'
    EQEQ = r'=='
    
    # Define Number Tokens
    @_(r'\d+')
    def NUMBER(self, t):
        t.value = int(t.value)
        return t

    # Define Comment Token
    @_(r'#.*')
    def COMMENT(self, t):
        pass

    # Define a rule so we can track line numbers
    @_(r'\n+')
    def newline(self, t):
        self.lineno = t.value.count('\n')

    # Define Error
    def error(self, t):
        print("Illegal character '%s'" % t.value[0])
        self.index += 1


if __name__ == '__main__':
    lexer = sunslexer()
    env = {}
    while True:
        try:
            text = input('suns > ')
        except EOFError:
            break
        if text:
            lex = lexer.tokenize(text)
            for token in lex:
                print(token)
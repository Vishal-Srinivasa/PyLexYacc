from ply import lex

tokens = [
   'NUMBER',
   'PLUS',
   'MINUS',
   'TIMES',
   'DIVIDE',
   'LPAREN',
   'RPAREN',
   'COMPARISON',
   'COLON',
   'COMMA',
   'ASSIGNMENT',
   'IDENTIFIER',
   'NEWLINE',
   'SEMICOLON'
]

# Regular expression rules for simple tokens
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_COMPARISON = r'==|!=|>|<|>=|<='
t_COLON = r'\:'
t_SEMICOLON = r'\;'
t_COMMA = r'\,'
t_ASSIGNMENT = r'\='

keywords = {
    'if' : 'IF',
    'def' : 'DEF',
    'try' : 'TRY',
    'except' : 'EXCEPT',
    'while' : 'WHILE',
    'and' : 'AND',
    'or' : 'OR',
    'not' : 'NOT',
    'print' : 'PRINT'
}
tokens = tokens + list(keywords.values())

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)    
    return t

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = keywords.get(t.value, 'IDENTIFIER')
    return t

def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore  = ' \t'


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()


data = "while 10>2:a = 10;b=10;"


lexer.input(data)


while True:
    tok = lexer.token()
    if not tok: 
        break
    print(tok)
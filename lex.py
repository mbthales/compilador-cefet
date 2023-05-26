import ply.lex as lex

reserved_words = ['var', 'mostrar', 'maiusculo']

tokens = (
    'ID',
    'VARIABLE_NAME',
    'SYMBOL',
    'NUMBER',
    'TEXT',
)

t_NUMBER = r'\d+'
t_TEXT = r'\".*\"'
t_ignore = ' \t'

def t_SYMBOL(t):
    r'[=, (, )]'
    return t

def t_VARIABLE_NAME(t):
    r'\b[a-zA-Z_][a-zA-Z_0-9]*\b'
    if t.value in reserved_words:
        t.type = 'ID'
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()

# data = open('teste.txt', 'r')

# lexer.input(data.read())

# # Tokenize
# while True:
#     tok = lexer.token()
#     if not tok:
#         break      # No more input
#     print(tok)
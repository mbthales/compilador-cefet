import ply.lex as lex

reserved_words = ['var', 'mostrar', 'maiusculo', 'minusculo', 'se', 'inicio', 'fim']

tokens = (
    'ID',
    'VARIABLE_NAME',
    'SYMBOL',
    'TERM',
)

t_TERM = r'"[a-zA-Z_][a-zA-Z_0-9]*"|\d+'
t_ignore = ' \t'

def t_SYMBOL(t):
    r'[=()><]|==|!='
    return t

def t_VARIABLE_NAME(t):
    r'\b[a-zA-Z_][a-zA-Z_0-9]*\b'
    if t.value in reserved_words:
        t.type = 'ID'
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    
class LexicalError(Exception):
    pass

def t_error(t):
    raise LexicalError(f"Lexical error: Illegal character '{t.value[0]}' at line {t.lexer.lineno}")

lexer = lex.lex()
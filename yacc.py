import ply.yacc as yacc

from lex import tokens

variables = {}

def p_expression_create_variable(p):
    '''expression : ID VARIABLE_NAME SYMBOL term
    | ID VARIABLE_NAME SYMBOL expression'''
    variables[p[2]] = p[4]

def p_expression_function_call(p):
    '''expression : ID SYMBOL term SYMBOL
    | ID SYMBOL expression SYMBOL'''
    if p[1] == 'mostrar':
        if p[3] in variables:
            print(variables[p[3]])
        else:
            print(p[3])
    elif p[1] == 'maiusculo':
        if p[3] in variables:
            p[0] = variables[p[3]].upper()
        else:
            p[0] = p[3].upper()

def p_expressions(p):
    '''expressions : expression 
    | expressions expression'''
    pass

def p_symbol(p):
    'symbol : SYMBOL'
    p[0] = p[1]

def p_term(p):
    '''term : NUMBER 
    | TEXT
    | VARIABLE_NAME'''
    p[0] = p[1]

def p_error(p):
    print("Syntax error in input!")

parser = yacc.yacc(start='expressions')
data = open('teste.txt', 'r')

parser.parse(data.read())

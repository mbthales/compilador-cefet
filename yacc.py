import ply.yacc as yacc

from lex import tokens

variables = {}

def p_expression_create_variable(p):
    '''expression : ID VARIABLE_NAME SYMBOL TERM
    | ID VARIABLE_NAME SYMBOL expression'''
    if p[3] != "=" or p[1] != "var":
        p_error(p)
    else:
        variables[p[2]] = p[4]

def p_expression_function_call(p):
    '''expression : ID SYMBOL TERM SYMBOL
    | ID SYMBOL VARIABLE_NAME SYMBOL
    | ID SYMBOL expression SYMBOL'''
    if p[1] == 'mostrar':
        if p[3] in variables:
            print(variables[p[3]].strip('"'))
        else:
            print(p[3].strip('"'))
    elif p[1] == 'maiusculo':
        if p[3] in variables:
            p[0] = variables[p[3]].upper()
        else:
            p[0] = p[3].upper()

def p_expressions(p):
    '''expressions : expression 
    | expressions expression'''
    pass

def p_error(p):
    print("Syntax error in input!")
    raise SyntaxError()

parser = yacc.yacc(start='expressions')
data = open('teste.txt', 'r')

parser.parse(data.read())

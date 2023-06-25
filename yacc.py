import ply.yacc as yacc

from lex import tokens

variables = {}
conditional_stack = [True]

def p_condition(p):
    'condition : ID TERM SYMBOL TERM'

    id_1 = p[1]
    term_1 = int(p[2])
    symbol = p[3]
    term_2 = int(p[4])

    operations = {
        '<': lambda x, y: x < y,
        '>': lambda x, y: x > y,
        '==': lambda x, y: x == y,
        '!=': lambda x, y: x != y
    }

    if id_1 == 'se':
        if symbol in operations:
            result = operations[symbol](term_1, term_2)
            conditional_stack.append(result)
        else:
            p_error(p)
    else:
        p_error(p)

def p_block(p):
    'block : ID expressions ID'

    id_1 = p[1]
    id_2 = p[3]

    if id_1 == 'inicio' or id_2 == 'fim':
        conditional_stack.pop()
    else:
        p_error(p)

    pass

def p_function(p):
    '''function : ID SYMBOL TERM SYMBOL
    | ID SYMBOL VARIABLE_NAME SYMBOL
    | ID SYMBOL function SYMBOL'''

    id_1 = p[1]
    symbol_1 = p[2]
    aux = p[3] # term or variable_name or function
    symbol_2 = p[4]

    if conditional_stack and conditional_stack[-1]:
        if symbol_1 == '(' or symbol_2 == ')':
            if id_1 == 'mostrar':
                if aux in variables:
                    print(variables[aux].strip('"'))
                else:
                    print(aux.strip('"'))
            elif id_1 == 'maiusculo':
                if aux in variables:
                    p[0] = variables[aux].upper()
                else:
                    p[0] = aux.upper()
            elif id_1 == 'minusculo':
                if aux in variables:
                    p[0] = variables[aux].lower()
                else:
                    p[0] = aux.lower()
            else:
                p_error(p)
        else:
            p_error(p)

def p_variable(p):
    '''variable : ID VARIABLE_NAME SYMBOL TERM
    | ID VARIABLE_NAME SYMBOL function'''

    id_1 = p[1]
    variable_name = p[2]
    symbol = p[3]
    aux = p[4] # term or function

    if symbol == "=" and id_1 == "var":
        variables[variable_name] = aux
    else:
        p_error(p)

def p_expressions(p):
    '''expressions : expressions function
    | expressions condition block
    | expressions variable
    | function
    | condition block
    | variable
    '''
    pass

def p_error(p):
    print("Syntax error in input!")
    raise SyntaxError()

parser = yacc.yacc(start='expressions')
data = open('main.txt', 'r')

parser.parse(data.read())

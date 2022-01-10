tokens = ('NAME','NUMBER',)

# Tokens
t_NAME    = r'[a-zA-Z_][a-zA-Z0-9_]*'

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

literals = ['+','(',')','=']

# Ignored characters
t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    if (t.value[0] != '#'):        
        t.lexer.skip(1)
        print("Error in input")
        exit()
    else:        
        print("Accepted")
        exit()    
        
# Build the lexer
import ply.lex as lex
lex.lex()

# dictionary of names (for storing variables)
names = { }

def p_statement_assign(p):
    '''statement : NAME '=' expression'''
    names[p[1]] = p[3]

def p_statement_expr(p):
    '''statement : expression'''
    print(p[1])

def p_expression_binop(p):
    '''expression : expression '+' expression'''
    if p[2] == '+'  : p[0] = p[1] + p[3]

def p_expression_group(p):
    '''expression : '(' expression ')' '''
    p[0] = p[2]

def p_expression_number(p):
    '''expression : NUMBER'''
    p[0] = p[1]

def p_expression_name(p):
    '''expression : NAME'''
    try:
        p[0] = names[p[1]]
    except LookupError:        
        print("Error in input")
        exit()        

def p_error(p):    
    print("Error in input")
    exit()

import ply.yacc as yacc
yacc.yacc(write_tables = False, debug = False)

while True:
    try:
        input_data = input()
    except EOFError:
        break
    yacc.parse(input_data)

#code adapted from dabeaz.com
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
        print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)  
        
# Build the lexer
import ply.lex as lex
lex.lex()

if __name__ == "__main__":
    input_data = ""
    new_input_data = ""
    
    while new_input_data != "#":
        new_input_data = input()
        
        if(new_input_data != "#"):
            input_data += new_input_data + "\n"
        
lex.input(input_data)

while True:
    tok = lex.token() 

    if (tok is None):
        break
    elif (tok.type == 'NAME'):
        print('(\''+tok.type+'\''+','+' \''+str(tok.value)+'\''+', '+str(tok.lineno)+', '+str(tok.lexpos)+')')
    elif (tok.type == 'NUMBER'):
        print('(\''+tok.type+'\', '+str(tok.value)+', '+str(tok.lineno)+', '+str(tok.lexpos)+')')
    else:
        print('(\''+tok.type+'\''+','+' \''+str(tok.value)+'\''+', '+str(tok.lineno)+', '+str(tok.lexpos)+')')
 
#code adapted from dabeaz.com
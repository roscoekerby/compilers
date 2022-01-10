tokens = ('COUNT','SYMBOL')

# Tokens
t_SYMBOL    = r'[A-Z][a-z]*'

def t_COUNT(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Ignored characters
t_ignore = " \t"

errorLine = None 

def t_newline(t):
    r'\n+'   
    t.lexer.lineno += t.value.count("\n")

def setErrorLine(eLine):
    global errorLine 
    errorLine = eLine    

def getErrorLine():
    global errorLine    
    return errorLine

def t_error(t):
    if (t.value[0] != '#'):       
        t.lexer.skip(1)
        eLine = tok.lineno        
        setErrorLine(eLine)        
        print("Error in formula")
    else:
        print(count)
        exit()    
        
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

input_data += "#"       
lex.input(input_data)

names = {'H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar', 'K', 'Ca', 'Sc', 
'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr', 'Rb', 'Sr', 'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 
'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'I', 'Xe', 'Cs', 'Ba', 'La', 'Ce' , 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu', 'Hf', 
'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn', 'Fr', 'Ra', 'Ac', 'Th', 'Pa', 'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm',
'Md', 'No', 'Lr', 'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt', 'Ds', 'Rg', 'Cn', 'Uut'}

count = 0
tok = lex.token() 
tempSymbol = ""   

while True:    
    templine = tok.lineno     

    while templine == tok.lineno:
        if templine != getErrorLine():        
            if (tok is None):
                print('Error in formula')                
                setErrorLine(templine)
            elif (tok.type == 'COUNT'):                
                count = count + tok.value - 1
            elif (tok.type == 'SYMBOL'):
                if (str(tok.value) in names and str(tok.value) != tempSymbol):                   
                    count = count+1
                    tempSymbol = str(tok.value)
                else:
                    print('Error in formula')                   
                    setErrorLine(templine)
            
        tok = lex.token()  
        if (templine != None):
            if (templine != tok.lineno):
                if (templine!=getErrorLine()):                    
                    print(count)          
                count = 0

#code adapted from dabeaz.com
            

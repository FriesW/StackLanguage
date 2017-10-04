from Stack import Stack
import re
from pprint import pprint as pp

SOURCE = "test.txt"

ops = [
"NOP", "IF", "NOTIF", "ELSE", "ENDIF", "WHILE", "ENDWHILE", "DO", "DOWHILE",
"DEBUG", "RETURN",
"DEPTH", "DROP", "ROT", "REVROT", "SWAP",
"INVERT", "AND", "OR", "XOR", "RSHIFT", "LSHIFT",
"MAX", "MIN", "GREATERTHANOREQUAL", "GREATERTHAN", "LESSTHANOREQUAL", "LESSTHAN", "EQUAL", "NOTEQUAL",
"BOOLOR", "BOOLAND", "ONOTEQUAL",
"NOT", "MOD", "DIV", "MUL", "EXP", "SUB", "ADD", "ABS", "NEGATE"]

#Read in file
f = open(SOURCE, 'r')
data = f.read()
f.close()
#Upper case
data = data.upper()
#Remove all extra whitespace
data = re.sub("\s+", ' ', data).strip()
#Explode
commands = data.split(' ')

pp(commands)

#Validate ops and nesting
def evalError(*args): 
    e = ""
    for i in args:
        e += str(i)
    raise ValueError(e)

n = Stack() #n for Nesting
pos = 0
for c in commands:
    pos += 1
    ###print "Eval " + c + "\n" + n.contents() + "E\n"
    if c not in ops:
        try:
            int(c)
        except:
            evalError("Item ", pos, ": Encountered command which is not an opcode or valid stack item: ", c)
    #Push IF
    elif c == "IF":
        n.push(c)
    #Push NOTIF
    elif c == "NOTIF":
        n.push(c)
    #ELSE must follow IF or NOTIF
    elif c == "ELSE":
        if n.height() == 0:
            evalError("Item ", pos, ": Improperly nested ELSE.")
        last = n.pop()
        if last != "IF" and last != "NOTIF":
            evalError("Item ", pos, ": Improperly nested ELSE.")
        n.push("ELSE")
    #ENDIF must follow IF or NOTIF or ELSE
    elif c == "ENDIF":
        if n.height() == 0:
            evalError("Item ", pos, ": Improperly nested ENDIF.")
        last = n.pop()
        if last != "IF" and last != "NOTIF" and last != "ELSE":
            evalError("Item ", pos, ": Improperly nested ENDIF.")
    #Push WHILE
    elif c == "WHILE":
        n.push(c)
    #ENDWHILE must follow WHILE
    elif c == "ENDWHILE":
        if n.height() == 0 or n.pop() != "WHILE":
            evalError("Item ", pos, ": Improperly nested ENDWHILE.")
    #Push DO
    elif c == "DO":
        n.push(c)
    #DOWHILE must follow DO
    elif c == "DOWHILE":
        if n.height() == 0 or n.pop() != "DO":
            evalError("Item ", pos, ": Improperly nested DOWHILE.")
if n.height() != 0:
    evalError("End reached with unbalanced nesting for:\n", n.contents())

print "Eval done"
    
#Evaluate
s = Stack() #data stack
n = Stack() #n for Nesting
cp = 0 #Command pointer
skip = False #nop override for IF/ELSE control
while cp < len(commands):
    c = commands[cp]
    print "Eval " + c + " and skip is: " + str(skip)
    #Section
    if c == "NOP":
        pass
    
    elif c == "IF": #Entry
        if skip:
            n.push( (cp, None) )
        else:
            run = 0 != s.pop()
            skip = not run
            n.push( (cp, run) )
    elif c == "NOTIF": #Entry
        if skip:
            n.push( (cp, None) )
        else:
            run = 0 == s.pop()
            skip = not run
            n.push( (cp, run) )
    elif c == "ELSE": #Entry/Exit
        top = n.pop()
        if top[1] == None: #This means we are in nested during nop
            n.push( (cp, None) )
        elif top[1] == False: #This means we are not nested, and our top half DIDN'T run
            skip = False
            n.push( (cp, True) )
        else: #This means we are not nested, and our top half DID run
            skip = True
            n.push( (cp, False) )
    elif c == "ENDIF": #Exit
        top = n.pop()
        if top[1] == None: #Nested during nop
            pass
        #Anything else, and we exit nop
        else:
            skip = False
    elif c == "WHILE": #Entry
        if skip:
            n.push( (cp, None) )
        else:
            run = 0 != s.pop()
            skip = not run
            n.push( (cp, run) )
    elif c == "ENDWHILE": #Exit
        top = n.pop()
        if top[1] == None: #Nested during nop
            pass
        else:
            if top[1]: #While ran, so go again
                cp = top[0] - 1
            else: #While did not run, so exit
                skip = False
    elif c == "DO": #Entry
        n.push( (cp, None) )
    elif c == "DOWHILE": #Exit
        top = n.pop()
        if skip: #Nested during nop
            pass
        else:
            if s.pop() != 0:
                cp = top[0] - 1
    
    elif not skip:
    
    
        #Section
        if c == "DEBUG":
            print "== STACK BOTTOM ==\n" + s.contents() + "== STACK TOP ==\n"
        elif c == "RETURN":
            cp = len(commands) #Terminate
            print "Execution halted " + \
                ( "VALID" if s.peek() != 0 else "INVALID" ) + \
                " with stack:\n== STACK BOTTOM ==\n" + \
                s.contents() + \
                "== STACK TOP ==\n"
        
        #Section
        elif c == "DEPTH":
            s.push( s.height() )
        elif c == "DROP":
            s.pop()
        elif c == "ROT":
            s.rotate( -s.pop() )
        elif c == "REVROT":
            s.rotate( s.pop() )
        elif c == "SWAP":
            t0 = s.pop()
            t1 = s.pop()
            s.push( t0 )
            s.push( t1 )
            comment_bullshit = '''
        #Section
        elif c == "INVERT":
        
        elif c == "AND":
        
        elif c == "OR":
        
        elif c == "XOR":
        
        elif c == "RSHIFT":
        
        elif c == "LSHIFT":
        
        
        #Section
        elif c == "MAX":
        
        elif c == "MIN":
        
        elif c == "GREATERTHANOREQUAL":
        
        elif c == "GREATERTHAN":
        
        elif c == "LESSTHANOREQUAL":
        
        elif c == "LESSTHAN":
        
        elif c == "EQUAL":
        
        elif c == "NOTEQUAL":
        
        
        #Section
        elif c == "BOOLOR":
        
        elif c == "BOOLAND":
            
        elif c == "ONOTEQUAL":
        
        elif c == "NOT":
        '''
        
        #Section
        elif c == "MOD":
            t0 = s.pop()
            t1 = s.pop()
            s.push( t1 % t0 )
        elif c == "DIV":
            t0 = s.pop()
            t1 = s.pop()
            s.push( t1 / t0 )
        elif c == "MUL":
            t0 = s.pop()
            t1 = s.pop()
            s.push( t1 * t0 )
        elif c == "EXP":
            t0 = s.pop()
            t1 = s.pop()
            s.push( t1 ** t0 )
        elif c == "SUB":
            t0 = s.pop()
            t1 = s.pop()
            s.push( t1 - t0 )
        elif c == "ADD":
            t0 = s.pop()
            t1 = s.pop()
            s.push( t1 + t0 )
        elif c == "ABS":
            s.push( abs(s.pop()) )
        elif c == "NEGATE":
            s.push( -s.pop() )
        
        
        else:
            s.push( int(c) )
    
    cp += 1
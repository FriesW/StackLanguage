from Stack import Stack
import re
from pprint import pprint as pp

MAX_STEPS = 10 ** 6
SOURCE = "test.txt"

ops = [
"NOP", "IF", "NOTIF", "ELSE", "ENDIF", "WHILE", "ENDWHILE", "DO", "DOWHILE",
"DEBUG", "RETURN",
"DEPTH", "DROP", "ROT", "REVROT", "SWAP", "DUP", "PICK", "ROLL", "TOALT", "FROMALT", "ALTDEPTH",
"INVERT", "AND", "OR", "XOR", "RSHIFT", "LSHIFT",
"MAX", "MIN", "GREATERTHANOREQUAL", "GREATERTHAN", "LESSTHANOREQUAL", "LESSTHAN", "EQUAL", "NOTEQUAL",
"BOOLOR", "BOOLAND", "ONOTEQUAL",
"NOT", "MOD", "DIV", "MUL", "EXP", "SUB", "ADD", "ABS", "NEGATE"]

#Read in file
f = open(SOURCE, 'r')
data = f.read()
f.close()
#Remove comments
data = re.sub("//(.*?)(\r\n|\r|\n)", '\n', data) #Single line
data = re.sub("/\*((?s).*?)\*/", '\n', data) #Multi-line
if data.find("/*") > 0:
    raise ValueError("Unmatched block comment opening.")
if data.find("*/") > 0:
    raise ValueError("Unmatched block comment closing.")
#Upper case
data = data.upper()
#Remove all extra whitespace
data = re.sub("\s+", ' ', data).strip()
#Explode
commands = data.split(' ')

#pp(commands)

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
alt = Stack() #alternate stack
n = Stack() #n for Nesting
cp = 0 #Command pointer
step_count = 0 #Count total steps
skip = False #nop override for IF/ELSE control
while cp < len(commands):
    c = commands[cp]
    
    #Check for max runtime
    if step_count > MAX_STEPS:
        raise RuntimeWarning("Execution has taken the maximum number of steps (" + format(MAX_STEPS, ',') + "). " + \
            "Check instructions for infinite loops, or increase the maximum step size.")
    step_count += 1
            
    #Control Section
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
        
        
        #Output Section
        if c == "DEBUG":
            print "== STACK BOTTOM ==\n" + s.contents() + "== STACK TOP ==\n"
        elif c == "RETURN":
            cp = len(commands) #Terminate
            print "Execution halted " + \
                ( "VALID" if s.peek() != 0 else "INVALID" ) + \
                " with stack:\n== STACK BOTTOM ==\n" + \
                s.contents() + \
                "== STACK TOP ==\n"
        
        
        #Stack Section
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
        elif c == "DUP":
            s.push( s.peek() )
        elif c == "PICK":
            s.pick( s.pop() )
        elif c == "ROLL":
            s.roll( s.pop() )
        elif c == "TOALT":
            alt.push( s.pop() )
        elif c == "FROMALT":
            s.push( alt.pop() )
        elif c == "ALTDEPTH":
            s.push( alt.height() )
        
        
        #Bitwise Section
        elif c == "INVERT":
            s.push( ~s.pop() )
        elif c == "AND":
            t0 = s.pop()
            t1 = s.pop()
            s.push( t0 & t1 )
        elif c == "OR":
            t0 = s.pop()
            t1 = s.pop()
            s.push( t0 | t1 )
        elif c == "XOR":
            t0 = s.pop()
            t1 = s.pop()
            s.push( t0 ^ t1 )
        elif c == "RSHIFT":
            t0 = s.pop()
            t1 = s.pop()
            s.push( t1 >> t0 )
        elif c == "LSHIFT":
            t0 = s.pop()
            t1 = s.pop()
            s.push( t1 << t0 )
        
        
        #Comparison Section
        elif c == "MAX":
            t0 = s.pop()
            t1 = s.pop()
            s.push( max(t0, t1) )
        elif c == "MIN":
            t0 = s.pop()
            t1 = s.pop()
            s.push( max(t0, t1) )
        elif c == "GREATERTHANOREQUAL":
            t0 = s.pop()
            t1 = s.pop()
            s.push(int( t0 >= t1 ))
        elif c == "GREATERTHAN":
            t0 = s.pop()
            t1 = s.pop()
            s.push(int( t0 > t1 ))
        elif c == "LESSTHANOREQUAL":
            t0 = s.pop()
            t1 = s.pop()
            s.push(int( t0 <= t1 ))
        elif c == "LESSTHAN":
            t0 = s.pop()
            t1 = s.pop()
            s.push(int( t0 < t1 ))
        elif c == "EQUAL":
            t0 = s.pop()
            t1 = s.pop()
            s.push(int( t0 == t1 ))
        elif c == "NOTEQUAL":
            t0 = s.pop()
            t1 = s.pop()
            s.push(int( t0 != t1 ))
        
        
        #Boolean Section
        elif c == "BOOLOR":
            t0 = bool( s.pop() )
            t1 = bool( s.pop() )
            s.push(int( t0 or t1 ))
        elif c == "BOOLAND":
            t0 = bool( s.pop() )
            t1 = bool( s.pop() )
            s.push(int( t0 and t1 ))
        elif c == "ONOTEQUAL":
            t0 = bool( s.pop() )
            s.push(int( t0 ))
        elif c == "NOT":
            t0 = bool( s.pop() )
            s.push(int( not t0 ))
        
        
        #Mathematics Section
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

print "TERMINATED\n"
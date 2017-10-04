from Stack import Stack

ops = [
"NOP", "IF", "NOTIF", "ELSE", "ENDIF", "WHILE", "ENDWHILE", "DO", "DOWHILE",
"DEBUG", "RETURN",
"DEPTH", "DROP", "ROT", "REVROT", "SWAP",
"INVERT", "AND", "OR", "XOR", "RSHIFT", "LSHIFT",
"MAX", "MIN", "GREATERTHANOREQUAL", "GREATERTHAN", "LESSTHANOREQUAL", "LESSTHAN", "EQUAL", "NOTEQUAL",
"BOOLOR", "BOOLAND", "ONOTEQUAL",
"NOT", "MOD", "DIV", "MUL", "EXP", "SUB", "ADD", "ABS", "NEGATE"]

#Read in file

#Remove all extra whitespace


#Validate ops and nesting
def evalError(*args):
    e = ""
    for i in args:
        e += i
    raise ValueError(e)

n = Stack() #n for Nesting
pos = 0
for c in commands:
    pos += 1
    if c not in ops:
        try:
            int(c)
        except:
            evalError("Line ", pos, ": Encountered command which is not an opcode or valid stack item: ", c)
    #Push IF
    elif c == "IF":
        n.push(c)
    #ELSE must follow IF
    elif c == "ELSE":
        if n.height() == 0 or n.pop() != "IF":
            evalError("Line ", pos, ": Improperly nested ELSE.")
    #ENDIF must follow IF or ELSE
    elif c == "ENDIF":
        if n.height() == 0:
            evalError("Line ", pos, ": Improperly nested ENDIF.")
        last = n.pop()
        if last != "IF" or last != "ELSE":
            evalError("Line ", pos, ": Improperly nested ENDIF.")
    #Push WHILE
    elif c == "WHILE":
        n.push(c)
    #ENDWHILE must follow WHILE
    elif c == "WHILE":
        if n.height() == 0 or n.pop() != "WHILE":
            evalError("Line ", pos, ": Improperly nested ENDWHILE.")
    #Push DO
    elif c == "DO":
        n.push(c)
    #DOWHILE must follow DO
    elif c == "DOWHILE":
        if n.height() == 0 or n.pop != "DOWHILE":
            evalError("Line ", pos, ": Improperly nested DOWHILE.")

    
#Evaluate
s = Stack() #data stack
n = Stack() #n for Nesting
cp = 0 #Command pointer
skip = False #nop override for IF/ELSE control
while cp < len(commands):
    c = commands[cp]
    
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
                cp = top[0]
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
                cp = top[0]
            
    
    
    #Section
    elif c == "DEBUG":
        print "== STACK BOTTOM ==\n" + s.contents() + "== STACK TOP ==\n"
    elif c == "RETURN":
    
    
    #Section
    elif c == "DEPTH":
    
    elif c == "DROP":
    
    elif c == "ROT":
    
    elif c == "REVROT":
    
    elif c == "SWAP":
    
    
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
    
    
    #Section
    elif c == "MOD":
    
    elif c == "DIV":
    
    elif c == "MUL":
    
    elif c == "EXP":
    
    elif c == "SUB":
    
    elif c == "ADD":
    
    elif c == "ABS":
    
    elif c == "NEGATE":
    
    else:
        s.push( int(c) )
    
    cp += 1
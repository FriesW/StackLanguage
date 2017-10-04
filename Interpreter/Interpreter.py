from Stack import Stack

ops = [
"NOP", "IF", "NOTIF", "ELSE", "ENDIF", "WHILE", "ENDWHILE", "DO", "DOWHILE",
"DEBUG", "RETURN",
"DEPTH", "DROP", "ROT", "REVROT", "SWAP",
"INVERT", "AND", "OR", "XOR", "RSHIFT", "LSHIFT",
"MAX", "MIN", "GREATERTHANOREQUAL", "GREATERTHAN", "LESSTHANOREQUAL", "LESSTHAN", "EQUAL", "NOTEQUAL",
"BOOLOR", "BOOLAND", "MOD", "DIV", "MUL", "EXP", "SUB", "ADD", "ONOTEQUAL", "NOT", "ABS", "NEGATE"]

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
while cp < len(commands):
    c = commands[cp]
    
    #Section
    if c == "NOP":
        pass
    elif c == "IF":
        n.append( (cp, c, 0 != s.pop()) )
    elif c == "NOTIF":
        n.append( (cp, c, 0 == s.pop()) )
    elif c == "ELSE":
    
    elif c == "ENDIF":
        n.pop()
    elif c == "WHILE":
    
    elif c == "ENDWHILE":
    
    elif c == "DO":
    
    elif c == "DOWHILE":
    
    
    #Section
    elif c == "DEBUG":
    
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
    
    elif c == "MOD":
    
    elif c == "DIV":
    
    elif c == "MUL":
    
    elif c == "EXP":
    
    elif c == "SUB":
    
    elif c == "ADD":
    
    elif c == "ONOTEQUAL":
    
    elif c == "NOT":
    
    elif c == "ABS":
    
    elif c == "NEGATE":
    
    else:
        s.push( int(c) )
    
    cp += 1
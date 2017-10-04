from Stack import Stack

ops = ["NOP", "IF", "NOTIF", "ELSE"]

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
n = Stack() #n for Nesting
cp = 0 #Command pointer
while cp < len(commands):
    c = commands[cp]
    
    
    if c == "NOP":
        pass
    elif c == "IF":
        n.append( (cp, c, 0 != s.pop()) )
    elif c == "NOTIF":
        n.append( (cp, c, 0 == s.pop()) )
    elif c == "ELSE":
    
    elif c == "ENDIF":
        n.pop()
    
    cp += 1
| Opcode | Description | Items Popped | Items Pushed |
| ------ | ----------- | -------------:| ------------:| 
| | **Category: Flow Control** | | |
| `NOP` | Do nothing | 0 | 0 |
| `IF` | Run code until `ELSE` or `ENDIF` if *top* is nonzero | 1 | 0 |
| `NOTIF` | Run code until `ELSE` or `ENDIF` if *top* is zero | 1 | 0 |
| `ELSE` | Run code until `ENDIF` if matching `IF` or `NOTIF` evaluated false | 0 | 0 |
| `ENDIF` | Closes either a matching `IF`, `NOTIF`, or `ELSE` | 0 | 0 |
| `WHILE` | Run code until matching `ENDWHILE` if *top* is nonzero | 1 | 0 |
| `NOTWHILE` | Run code until matching `ENDWHILE` if *top* is zero | 1 | 0 |
| `ENDWHILE` | Exit location for matching `WHILE` | 0 | 0 |
| `DO` | Entry location for matching `DOWHILE` | 0 | 0 |
| `DOWHILE` | Jumps to matching `DO` if *top* is nonzero | 1 | 0 |
| `DONOTWHILE` | Jumps to matching `DO` if *top* is zero | 1 | 0 |
| | **Category: Output and Debug** | | |
| `DEBUG` | Prints the primary stack's contents | 0 | 0 |
| `DEBUGALT` | Prints the alternate stack's contents | 0 | 0 |
| `ECHO` | Pops and prints *top* | 1 | 0 |
| `RETURN` | Halts execution, prints a validity statement based on stack being at least one high with *top* being nonzero | 0 | 0 |
| | **Category: Stack Operations** | | |
| `DEPTH` | Pushes the size of the primary stack to the primary stack | 0 | 1 |
| `DEPTHALT` | Pushes the size of the alternate stack to the primary stack | 0 | 1 |
| `TOALT` | Moves *top* to alternate stack | 1 | 1 alt |
| `FROMALT` | Moves alternate stack top to primary stack | 1 alt | 1 |
| `DROP` | Pops *top* and discards it | 1 | 0 |
| `NIP` | Removes *second* and discards it | 1 | 0 |
| `DUP` | Duplicates *top* | 0 | 1 |
| `OVER` | Copies *second* to top | 0 | 1 |
| `PICK` | Copies the item *top* away from the top to top, negative *top* indexes from bottom | 0 | 1 |
| `ROLL` | Moves the item *top* away from the top to top, negative *top* indexes from bottom | 0 | 1 |
| `2DUP` | Duplicates both *top* and *second*, `t1 t0` &rarr; `t1 t0 t1 t0` | 0 | 2 |
| `3DUP` | Duplicates the top 3 stack items, `t2 t1 t0` &rarr; `t2 t1 t0 t2 t1 t0` | 0 | 3 |
| `ROT` | Top 3 stack items are rotated left, `t2 t1 t0` &rarr; `t1 t0 t2` | 0 | 0 |
| `SWAP` | Swaps *top* and *second* in the stack | 0 | 0 |
| `2ROT` | Fifth and sixth items back are moved to top, `t5 t4 t3 t2 t1 t0` &rarr; `t3 t2 t1 t0 t5 t4` | 0 | 0 |
| `2SWAP` | Swaps the top two pairs, `t3 t2 t1 t0` &rarr; `t1 t0 t3 t2` | 0 | 0 |
| `TUCK` | *top* is copied and inserted before *second*, `t1 t0` &rarr; `t0 t1 t0` | 0 | 1 |
| `2OVER` | Copies the pair two items back to top, `t3 t2 t1 t0` &rarr; `t3 t2 t1 t0 t3 t2` | 0 | 2 |
| `ROTATE` | Rotates the stack by *top*, *top* becomes *bottom* for positive values | 1 | 0 |
| `REVROTATE` | Rotates the stack by *top*, *bottom* becomes *top* for positive values | 1 | 0 |
| | **Category: Bitwise Operations** | | |
| `INVERT` | Bitwise inversion of *top* | 1 | 1 |
| `AND` | Bitwise and of *top* and *second* | 2 | 1 |
| `OR` | Bitwise or of *top* and *second* | 2 | 1 |
| `XOR` | Bitwise xor of *top* and *second* | 2 | 1 |
| `RSHIFT` | Bitshift right *second* by *top* steps | 2 | 1 |
| `LSHIFT` | Bitshift left *second* by *top* steps | 2 | 1 |
| | **Category: Comparisons** | | |
| `MAX` | Discards the smallest of *top* and *second* | 2 | 1 |
| `MIN` | Discards the largest of *top* and *second* | 2 | 1 |
| `GREATERTHANOREQUAL` | Pushes 1 if *top*`>=`*second*, otherwise pushes 0 | 2 | 1 |
| `GREATERTHAN` | Pushes 1 if *top*`>`*second*, otherwise pushes 0 | 2 | 1 |
| `LESSTHANOREQUAL` | Pushes 1 if *top*`<=`*second*, otherwise pushes 0 | 2 | 1 |
| `LESSTHAN` | Pushes 1 if *top*`<`*second*, otherwise pushes 0 | 2 | 1 |
| `EQUAL` | Pushes 1 if *top*`==`*second*, otherwise pushes 0 | 2 | 1 |
| `NOTEQUAL` | Pushes 1 if *top*`!=`*second*, otherwise pushes 0 | 2 | 1 |
| `WITHIN` | Pushes 1 if third from top is within range between *second* and *top*, left-inclusive| 3 | 1 |
| | **Category: Boolean Operations** | | |
| `BOOLOR` | Boolean or of *top* and *second*, where 0 is false and all else is true | 2 | 1 |
| `BOOLAND` | Boolean and of *top* and *second*, where 0 is false and all else is true | 2 | 1 |
| `0NOTEQUAL` | 0 becomes 0, anything else becomes 1 | 1 | 1 |
| `NOT` | 0 becomes 1, anything else becomes 0 | 1 | 1 |
| | **Category: Mathematics Operations** | | |
| `MOD` | *second* % *top* | 2 | 1 |
| `DIV` | *second* / *top* | 2 | 1 |
| `MUL` | *second* \* *top* | 2 | 1 |
| `EXP` | *second* ^ *top* or *second* \*\* *top* | 2 | 1 |
| `SUB` | *second* \- *top* | 2 | 1 |
| `ADD` | *second* \+ *top* | 2 | 1 |
| `ABS` | Absolute value of *top* | 1 | 1 |
| `NEGATE` | Flip the sign of *top* | 1 | 1 |


#### Notes:

 * If stack is not specified, the primary stack is assumed.
 * *top* is the top most item on the primary stack.
 * *second* is the second to top most item on the primary stack.
 * Opcodes are not case sensitive.
 * `OP_` before each opcode is optional.
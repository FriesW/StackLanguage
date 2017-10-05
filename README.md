# StackLanguage

Loosely based upon the [bitcoin scripting language](https://en.bitcoin.it/wiki/Script). This "language" implements a lot of the same concepts and opcodes. There are also some opcodes which I took the liberty to add, as I find them useful or novel.

## Usage

The script is in Python, and has been written and tested in Python 2.7. Will not work in 3.x in its current state.

Script can be invoked from the command line. There are two primary modes in which the script will run. Mode 1 is where no arguments are provided. In this case, the script will look for a default file and execute it. In mode 2 arguments are provided to the script. The arguments are interpreted as immediate opcodes. However, if the argument is not an opcode or number, it is instead treated as the name of a file to be opened and executed.

#### Mode 1
```
python Interpreter.py
```
This will execute the default file specified at the top of the Interpreter.py script. It is most likely "instructions.txt".

#### Mode 2
```
python Interpreter.py 3 5 ADD 152 verify.txt 19 SUBTRACT 1 debug
```
Immediate opcodes: arguments 0, 1, 2, 3, 5, 7, 8

File names: arguments 4, 6


## Notes on code, instructions and runtime

* See the Docs folder for a markdown document of the opcodes.
* Interpreter.py is portable and has no dependencies outside of Python.
* Instructions are not case sensitive.
* Instruction sources support c-like comments: ```// A line comment``` and ```/* A block comment */```
* All flow control opcodes must be properly nested. No overlap is allowed.
* Each sequence of immediate opcodes and each instruction file must contain all matching control flow opcodes.
    * Ex: IF cannot start in one file, and then the matching ENDIF occurs in a different file.
    * Documents are verified separately, then combined.
* I'm pretty sure the inclusion of the WHILE opcode makes this language Turing complete.
* A maximum number of ops can be evaluated before an Exception is thrown. This is to counter runaway loops.
    * The default limit is 10^6 ops. You probably won't hit it with good code. If you do, I'm impressed.
    * The limit is per interpreted sequence (per file, per immediate sequence).
    * The only way to change it is to edit the Interpreter.py file.
* A number of runtime exceptions can occur during execution. Most involve the stack being empty, going past the ends of the stack, or dividing by zero.

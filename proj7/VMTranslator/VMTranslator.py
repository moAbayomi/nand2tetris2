import sys
import os
import glob
from Parser import Parser
from CodeWriter import CodeWriter

VM_FILE = ""
if len(sys.argv) == 2: 
    file_path = sys.argv[-1]
    root, ext = os.path.splitext(file_path)
    if os.path.isfile(file_path) and ext == ".vm":
        print("confirm", file_path)
        VM_FILE = file_path
    else:
        print("omo e no confirm o")
        sys.exit(1)

elif len(sys.argv) == 1:
    glob_file = glob.glob("*.vm")
    file = [f for f in os.listdir(".") if f.endswith(".vm")]
    if file:
        VM_FILE = file[0]
    else:
        sys.exit(1)
        
else:
    print("""
        usage VMTranslator.py <source>
        <source> which is the filepath to the vm file which starts with 
        a uppercase letter.
        omo you dull o.
        just call the function properly nau dawgg. what really 
        is your problem
        """)
    sys.exit(1)

p = Parser(VM_FILE);


c = None
if(VM_FILE):
    output_file = os.path.splitext(VM_FILE)[0] + ".asm"
    c = CodeWriter(output_file)
else:
    print("error : no vm file provided")
    sys.exit(1)

outputLines = []
    
while p.hasMoreLines():
    if p.commandType() == "C_ARITHMETIC":
        stmt = c.writeArithmetic(p.currentInstruction())
        outputLines.extend(stmt)
    elif p.commandType() == "C_PUSH" or p.commandType() == "C_POP":
        cmd = "push" if p.commandType() == "C_PUSH" else "pop"
        segment = p.arg1()
        index = p.arg2()
        stmt = c.writePushPop(cmd, segment, index)
        outputLines.extend(stmt)
        
    p.advance()

if c.file:
    with open(c.file, "w") as f:
        for line in outputLines:
            f.write(line + "\n")
    
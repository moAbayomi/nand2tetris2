class CodeWriter:
    def __init__(self, file):
        self.file = file
        self.label_counter = 0

        self.SEGMENTS = {
            "local": "LCL",
           "argument": "ARG",
           "this": "THIS", 
           "that": "THAT",
        }


    def pushToAddress(self, address):
        return [
            f"@{address}",
            "D=M",
            "@SP",
            "A=M",
            "M=D",
            "@SP",
            "M=M+1"
        ]

    def popFromAddress(self, address):
        return [
            "@SP",
            "M=M-1",
            "A=M",
            "D=M",
            f"@{address}",
            "M=D"
        ]
    
    def writeArithmetic(self, arith):

        output = []
        if arith == "neg":
            return [
                "@SP",
                "M=M-1",
                "A=M",
                "M=-M",
                "@SP",
                "M=M+1"
            ]

        if arith == "not":
            return [
                "@SP",
                "M=M-1",
                "A=M",
                "M=!M",
                "@SP",
                "M=M+1"
            ]

        if arith in ["add", "sub", "and", "or"]:
            output += [
                "@SP",
                "M=M-1",
                "A=M",
                "D=M",
                "@SP",
                "M=M-1",
                "A=M",
            ]

            if arith == "add":
                output.append("M=M+D")
            elif arith == "sub":
                output.append("M=M-D")
            elif arith == "and":
                output.append("M=D&M")
            elif arith == "or":
                output.append("M=D|M")
    
            output += [
                "@SP",
                "M=M+1"
            ]
    
            return output

        if arith in ["lt", "gt", "eq"]:
            labelTrue = f"START_{self.label_counter}"
            labelEnd = f"end_{self.label_counter}"
            self.label_counter += 1
            output += [
                "@SP",
                "M=M-1",
                "A=M",
                "D=M",
                "@SP",
                "M=M-1",
                "A=M",
                "D=M-D",
                f"@{labelTrue}"
            ]
            

            if arith == "lt":
                output.append("D;JLT")
            elif arith == "gt":
                output.append("D;JGT")
            elif arith == "eq":
                output.append("D;JEQ")

            output += [
                        "@SP",
                        "A=M",
                        "M=0",
                        f"@{labelEnd}",
                        "0;JMP",
                        f"({labelTrue})",
                        "@SP",
                        "A=M",
                        "M=-1",
                        f"({labelEnd})",
                        "@SP",
                        "M=M+1",
                    ]
            return output
            
        return output
            

    def writePushPop(self, command, segment, idx):

        idx = int(idx)

        if segment == "constant":
            if command == "push":
                return [
                    f"@{idx}",
                    "D=A",
                    "@SP",
                    "A=M",
                    "M=D",
                    "@SP",
                    "M=M+1"
                ]
            else:
                return []

        if segment == "static":
            symbol = f"@Static.{idx}"
            if command == "push":
                return self.pushToAddress(symbol)
            else:
                return self.popFromAddress(symbol)

        if segment == "temp":
            symbol = 5 + idx
            return self.pushToAddress(symbol) if command == "push" else self.popFromAddress(symbol)

        if segment == "pointer":
            symbol = 3 + idx
            return self.pushToAddress(symbol) if command == "push" else self.popFromAddress(symbol)


        baseSeg = self.SEGMENTS[segment]

        computeAddr = [
            f"@{idx}",
            "D=A",
            f"@{baseSeg}",
            "D=M+D",
            "@addr",
            "M=D",
        ]
        
        if command == "push":
            output = computeAddr +  [
                "@addr",
                "A=M",
                "D=M",
                "@SP",
                "A=M",
                "M=D",
                "@SP",
                "M=M+1"
            ]
        else:
            output = computeAddr + [
                "@SP",
                "M=M-1",
                "A=M",
                "D=M",
                "@addr",
                "A=M",
                "M=D",   
            ]
            
        return output
        
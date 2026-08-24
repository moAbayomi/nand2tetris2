class Parser:
    def __init__(self, file):
        self.curr = 0
        self.file = []
        if file:
            with open(file, "r") as f:
                for line in f:
                    curr_line = line.strip()
                    if curr_line:
                        if "//" in curr_line:
                            slash, rest = curr_line.split("//", 1)
                            if slash != "":
                                self.file.append(slash)
                        else:
                            self.file.append(curr_line)
        else:
            raise FileExistsError("wetin be this gba")


        self.curr_command = self.file[self.curr]



    def currentInstruction(self):
        return self.file[self.curr]
    
    def hasMoreLines(self):
        return self.curr < len(self.file)

    def advance(self):
        self.curr_command = self.currentInstruction()
        self.curr += 1
            

    def commandType(self):
        line = ""
        if self.currentInstruction():
            line = self.currentInstruction()
        else:
            return "null"
        arith_arr = ["add", "sub", "neg", "eq", "gt", "lt", "and", "or", "not"]
        if line in arith_arr:
            return "C_ARITHMETIC"
        elif line.startswith("push"):
            return "C_PUSH"
        elif line.startswith("pop"):
            return "C_POP"

    def arg1(self):
        curr_command = self.currentInstruction()
        if curr_command:
            if self.commandType() == "C_PUSH" or self.commandType() == "C_POP":
                [_, arg1, _] = curr_command.split(" ")
                return arg1
            elif self.commandType() == "C_ARITHMETIC":
                return curr_command

    def arg2(self):
        curr_command = self.currentInstruction()
        if curr_command:
            if self.commandType() == "C_PUSH" or self.commandType() == "C_POP":
                [_, _, arg2] = curr_command.split(" ")
                return arg2
            else: 
                return ""
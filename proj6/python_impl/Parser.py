class Parser:
    def __init__(self, path, symbols_dict):
        self.path = path
        self.file = []
        self.symbols = []
        self.clean_code = []
        self.symbols_dict = symbols_dict
        with open(path) as f:
            for line in f:
                code_part = line.split("//")[0]

                cleaned_line = code_part.strip()
                if cleaned_line == "":
                    continue
                else:
                    self.file.append(cleaned_line)

        self.rom_address = 0
        for cmd in self.file:
            if cmd.startswith("("):
                label_name = cmd.strip("()")
                self.symbols_dict[label_name] = self.rom_address
            else:
                self.clean_code.append(cmd)
                self.rom_address += 1
        self.total_lines = len(self.clean_code)
        self.curr = 0

    def print_file(self):
        return self.clean_code

    def _read_instruction(self):
        return self.clean_code[self.curr]

    def has_more_lines(self):
        return self.curr < self.total_lines

    def advance(self):
        self.curr += 1

    def instruction_type(self, curr_instruction):
        if curr_instruction.startswith("@"):
            return "A_INSTRUCTION"
        else:
            return "C_INSTRUCTION"

    def dest(self, curr_instruction):
        if "=" in curr_instruction:
            return curr_instruction.split("=")[0]
        else:
            return ""

    def comp(self, curr_instruction):
        if "=" in curr_instruction:
            rhs = curr_instruction.split("=")[1]
            if ";" in rhs:
                return rhs.split(";")[0]
            else:
                return rhs
        else:
            return curr_instruction.split(";")[0]

    def jmp(self, curr_instruction):
        if ";" in curr_instruction:
            return curr_instruction.split(";")[1]
        return ""

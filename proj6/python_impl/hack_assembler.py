import os
import sys
from pathlib import Path
from Parser import Parser
from Symbols import SYMBOLS
from Code import Code

length_c = len(sys.argv)


def generate_output_path(path):
    input_path = Path(path)
    output_path = input_path.with_suffix(".hack")

    return output_path


def init():
    if length_c != 2:
        print("""
        Usage: 
        # python hack_assembler.py <filename>
        # this is how. capicshe? or caprisonne
        # or whatever youre into. thank you!
        """)
        return sys.exit(1)
    else:
        file_path = sys.argv[-1]
        is_valid_path = os.path.exists(file_path)
        if is_valid_path:
            file_parser = Parser(file_path, SYMBOLS)

            next_ram_address = 16
            output_bin = []

            while file_parser.has_more_lines():
                curr_instruction = file_parser._read_instruction()
                curr_instruction_type = file_parser.instruction_type(curr_instruction)
                if curr_instruction_type == "A_INSTRUCTION":
                    address_part = curr_instruction[1:]
                    address = ""

                    if address_part.isdigit():
                        address = int(address_part)
                    else:
                        if address_part in file_parser.symbols_dict:
                            address = int(file_parser.symbols_dict[address_part])
                        else:
                            file_parser.symbols_dict[address_part] = str(
                                next_ram_address
                            )
                            address = next_ram_address
                            next_ram_address += 1

                    binary_instruction = format(address, "016b")
                    output_bin.append(binary_instruction)

                else:
                    raw_dest = file_parser.dest(curr_instruction)
                    raw_comp = file_parser.comp(curr_instruction)
                    raw_jmp = file_parser.jmp(curr_instruction)

                    dest = Code(raw_dest).dest()
                    comp = Code(raw_comp).comp()
                    jmp = Code(raw_jmp).jmp()

                    binary_instruction = "111" + comp + dest + jmp
                    output_bin.append(binary_instruction)

                file_parser.advance()
            print(output_bin)

            output_path = generate_output_path(file_path)
            with open(output_path, "w") as f:
                for lines in output_bin:
                    f.write(lines + "\n")


init()

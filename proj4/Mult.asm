// the program computes the 
// product R0 * R1 and stores
// the result in R2


@mult
M=0
@i
M=0
(LOOP)
// if i < R1 goto loop
@R1
D=M
@i
D=D-M
@RES
D;JEQ

@R0
D=M
@mult
M=D+M
@i
M=M+1
@LOOP
0;JMP

(RES)
@mult
D=M
@R2
M=D
@END
0;JMP

(END)
@END
0;JMP


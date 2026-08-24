// push constant 17
17
D=A
// push constant 17
17
D=A
// eq
@SP
AM=M-1
D=M
A=A-1
D=M-D
M=-1
@COMP_{this.labelCount}
D;JEQ
@SP
A=M-1
M=0
(COMP_{this.labelCount})
// push constant 17
17
D=A
// push constant 16
16
D=A
// eq
@SP
AM=M-1
D=M
A=A-1
D=M-D
M=-1
@COMP_{this.labelCount}
D;JEQ
@SP
A=M-1
M=0
(COMP_{this.labelCount})
// push constant 16
16
D=A
// push constant 17
17
D=A
// eq
@SP
AM=M-1
D=M
A=A-1
D=M-D
M=-1
@COMP_{this.labelCount}
D;JEQ
@SP
A=M-1
M=0
(COMP_{this.labelCount})
// push constant 892
892
D=A
// push constant 891
891
D=A
// lt
@SP
AM=M-1
D=M
A=A-1
D=M-D
M=-1
@COMP_{this.labelCount}
D;JLT
@SP
A=M-1
M=0
(COMP_{this.labelCount})
// push constant 891
891
D=A
// push constant 892
892
D=A
// lt
@SP
AM=M-1
D=M
A=A-1
D=M-D
M=-1
@COMP_{this.labelCount}
D;JLT
@SP
A=M-1
M=0
(COMP_{this.labelCount})
// push constant 891
891
D=A
// push constant 891
891
D=A
// lt
@SP
AM=M-1
D=M
A=A-1
D=M-D
M=-1
@COMP_{this.labelCount}
D;JLT
@SP
A=M-1
M=0
(COMP_{this.labelCount})
// push constant 32767
32767
D=A
// push constant 32766
32766
D=A
// gt
@SP
AM=M-1
D=M
A=A-1
D=M-D
M=-1
@COMP_{this.labelCount}
D;JGT
@SP
A=M-1
M=0
(COMP_{this.labelCount})
// push constant 32766
32766
D=A
// push constant 32767
32767
D=A
// gt
@SP
AM=M-1
D=M
A=A-1
D=M-D
M=-1
@COMP_{this.labelCount}
D;JGT
@SP
A=M-1
M=0
(COMP_{this.labelCount})
// push constant 32766
32766
D=A
// push constant 32766
32766
D=A
// gt
@SP
AM=M-1
D=M
A=A-1
D=M-D
M=-1
@COMP_{this.labelCount}
D;JGT
@SP
A=M-1
M=0
(COMP_{this.labelCount})
// push constant 57
57
D=A
// push constant 31
31
D=A
// push constant 53
53
D=A
// add
@SP
AM=M-1
D=M
A=A-1
M=D+M
// push constant 112
112
D=A
// sub
@SP
AM=M-1
D=M
A=A-1
M=M-D
// neg
@SP
A=M-1
M=-M
// and
@SP
AM=M-1
D=M
A=A-1
M=M&D
// push constant 82
82
D=A
// or
@SP
AM=M-1
D=M
A=A-1
M=M|D
// not
@SP
A=M-1
M=!M

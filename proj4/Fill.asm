// this program runs an infinite
// loop that listens to the keyboard
// when a key is pressed, the program
// blackens the screen. when no key is
// pressed, the program clears the screen
// by writing white in every pixel.

(LOOP)

@KBD
D=M
@WHITE
D;JEQ
@BLACK
0;JMP

(WHITE)
@color
M=0
@DRAW
0;JMP

(BLACK)
@color
M=-1
@DRAW
0;JMP

(DRAW)
@SCREEN
D=A
@addr
M=D

(FILL_LOOP)
@color
D=M
@addr
A=M
M=D

@addr
M=M+1

D=M
@KBD
D=A-D
@FILL_LOOP
D;JGT

@LOOP
0;JMP

(color)
(addr)

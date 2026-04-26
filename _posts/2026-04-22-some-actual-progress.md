ROM addressing

The seventeen ROM address bits are allocated as follows:

A16 A15  A14 A13   A12 A11   A10 A9  A8  A7  A6  A5  A4  A3    A2  A1  A0
 R   R     X   X     I   I   I   I   I   I   I   I   I   T     T   T    T

Bits 	Count 	Use 	Source
16..15 	2 	ROM select 	Hardwired

14..4 	11 	Instruction (opcode) 	Instruction Register
3..0 	4 	T Cycle 	Ring Counter


So I think I'll just use the 74ls161 in the whole 4 bit 




### 23APR26 Updates
Flag register, I was going to use the 74hc574, but I've decided on switching over to [2 74hc74's](https://tomnisbet.github.io/nqsap/docs/flags/#flag-registers)


74hc283 x 2 ; 74hct688 x 1

Also stuff I'm ordering -
	74hct194's for shift operations https://fadil-1.github.io/blog/8-bit_breadboard_CPU/alu_&_flags/
	

###  25APR26 Updates

So I've been doing some serious work on the computer today, and trying to figure out how I did some of the things.  Since I apparently didn't document how I did the rom/ram part of the computer [that well](https://thecodingchicken.github.io/2025/05/24/progress.html), and all I have is that one day's worth of stuff, I have to re-figure it out.  Who knows if it even works ¯\\_(ツ)_/¯, but I hope it does.  it looks like I had to use the clock to AND signals together to make things work?  I have no clue.  
But I have 4 control lines, 3 of which select an output from a 74hc138.  The 4th is used as ENABLE_G1(Active LOW), but it also goes into those boards to a AND gate that does who knows what.  The commented out part says `MEM_EN (active high)`, so that's at least a start.  At least when I used grok for this mess, I left this in here.  Not totally stupid.  Apparently it does `2A = 74HC139 2Y0 (RAM_CE), 2B = MEM_EN (control unit), 2Y = Final RAM_CE to 62256 CE, First 74HC08 Gate 3 input A, Second 74HC08 Gate 1 input A`.  Yeah.  And that chat's too old to keep around it seems, or something along that line. 

But this is useful!  
```
Y1 (pin 14): To 74HC04 Gate 1 input (Breadboard 1, MAR_LOAD_L).

Y2 (pin 13): To 74HC04 Gate 2 input (Breadboard 1, MAR_LOAD_H).

Y3 (pin 12): To 74HC04 Gate 3 input (Breadboard 1, READ).

Y4 (pin 11): To 74HC04 Gate 4 input (Breadboard 1, WRITE).
```
So I think the 4th line is used as an overall enable IO for the module, whereas 1-3 allow me to select things.  I believe the way I set it up was that from like 0-4k is rom, and after that it's ram?  I got no clue.  Either way, it's going to the microcode roms now that I know that.  

A12-A14 will stay grounded, for future use(I think).
A0-A3 are Ring Counter bits, A4-A11 are OPCODE, A12-A14 are unused, and A15-A16 are for chip selection bits.  

Y9(Pin10) of right 74hc154 goes to WI(74hc574 of Instruction Register) via AND Gate with clock signal to only load it at the proper time.  
Y8 of right 74hc154 goes to CounterInHigh of the Program counter
Y7 of right 74hc154 goes to CounterInLow of the Program counter
Y8 of left 74HC154 goes to CounterOutHigh of the Program counter
Y7 of left 74hc154 goes to CounterOutLow of the Program counter
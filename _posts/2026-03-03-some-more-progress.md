## Some more progress


I have a couple hours to get things done today, I think the target will be to finish the display outputs from the A&B registers, as well as the ALU output.  That'll allow me to at least start testing basic things, like Can It Count, and my favorite, **What went Wrong**.  Then I just have to start hooking up more testing stuff.  I'm going to follow along with Ben Eater's videos to some degree, mainly for testing and getting bits and pieces to work.  
Unfortunately, I don't have the first build with me, otherwise I'd use it for some things.  But that's life, I only have so much space here with me.  

---
### Arduino for 7 segment displays pins used
Pins D2, D3, D4 : Data Line, Clock, Load respectively
Pins D5, D6, D7, D8 : The 4 digits on each led display
Pin D9  : dataOut -> DS/SER(pin 14) of first 595 (SERial input)
Pin D10 : SRCLK(pin11) of all 3 595s (Shift Register Clock)
Pin D11 : RCLCK(pin12) of all 3 595s (Register Clock)

Q7S (pin 9) of first 595 → DS of second
Q7S of second → DS of third
57A 53B 56F

---
I ended up just stopping for the day, some things weren't working.  
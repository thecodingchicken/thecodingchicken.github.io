## Program counter start

Going to start working on the program counter today, as I can't do the ALU for a while due to not having the 74ls181 chips.  I also can't do the ram, ~~as I don't know what sort of chip I want to settle with, I am going to get both a 62256LP-70 and a CY7C199-35PC, both are 32Kx8 chips, but I don't know which I want to use.~~ as I don't have the 62256LP-70 that I'm going to go with.  

---
### Program counter design.
There's a bunch of 4-bit counters that I could have gone with, but I'm going to settle with the 74hc161, as that's the same as the 74ls161 used in Ben's program.  
Now, I have a 16-bit program counter, which means that I need to have two 74hc245's, for the LOW and HIGH bytes.  I'm going to need to add another breadboard off to the side to show the program counter value, as these 6 chips basically take up the whole board.  I think having this stuff off to the side helps out anyway, it'll keep the main board neater.  

I don't have the 161 yet, but I'm ordering some soonish.  In the meanwhile, I'll just have some placeholder 851 9449 sonar chips, heh.  


---
## Register control screwups.
I just realized that the 74hc574 doesn't have a reset line, which would have been ideal.  As such, I guess I'll have to either program in a reset program, or use something like an atmega(probably) to reset things.  Although, I don't know how necessary this will be for all of these registers, as realisticly if the program will use it, it should be initialized to zero first.  I think programming a reset breadboard would be kinda sweet. 
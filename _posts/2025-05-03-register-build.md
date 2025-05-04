## Building the registers

I think I'm going to start off by building 8 8-bit registers.  I've settled with a 74hc245 and a 74hc574 for the register, as mentioned at the end of [this blog](https://thecodingchicken.github.io/2025/04/29/design-goals-and-starting-the-build.html).
It appears like I can cram 3 registers onto a single chip, which'll work well for the last 6 registers.  The first two will be hooked up like in Ben Eater's SAP-1, that way I can see the values and it'll be easier to integrate with the ALU.  I think I'll plan space on these boards for enamel wiring later on to have led bar displays to show their values.  Enamel wire is kinda a pain, but the insulation is so much thinner, so it'll work better.  Just need another tool just for that to strip it, my thermal stripper doesn't work on that stuff it seems...which is a shame, I hoped it would.  
Anyway, time to build a couple breadboards up.  Doing it on temporary breadboards, and I'll build it for real later.  

### Important
I was debating on how to line them up, and I ended up doing a vertical line.  I'll attach three pictures of my progress on the silly thing.  The lines could have been neater, but it works in the end.  I do need to get some 74hc02 NOR gates, as it seems that I don't have those.  
I need to figure out what are the final things that I need to stop ordering stuff.  LOL.
I'll probably wire it all up as if the NOR's in place, but just can't test it until I get them.  I only have 74ls02's, and maybe 1 74hct02, but I'll need two, for the 6 total registers here.  Not to mention the other two registers for the ALU.  I've just started ordering 10 or 20 of these chips, because I'll probably find a use for them.  Only costs a few bucks more, anyway.  

### Final layout(planned)
So I think the final layout of the board will be 3 breadboards, with the bottom one handling the control logic(3-8 decoding for both inputs and outputs), NOR gates for combining clock and register in controls, and maybe some led stuff.  Or, more likely, space for something else that I'm forgetting.  I do need to implement a shift register somewhere I suppose...don't know how that's gonna happen.
But that's a topic for another day, I need to get some sleep.  

---
### Things to consider for the future
How do I want to implement a shift register?  Jameco doesn't have a 74hc194 4-bit shift register, need to look around for other options.  
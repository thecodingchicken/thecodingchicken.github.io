## More progress, progressively
Might as well work on this stuff while I have time?

Today, I'm going to work on the ring counter, used for the various steps.  This is skipping ahead a bit, but I want to leave the led outputs(which aren't fully operational) for a bit later.  

Anyway, I'm going to be using a 74hc161 and a 74hc138.  The 161 will be the actual counter, and the 138 is really just for display purposes(making it clear to me what step we're on).  Somehow, I don't have a 74hc161.  Apparently I bought 10 74LS161's, so I'm going to have to order some of the hc ones.  But I might just wire it up still, and perhaps test it with the ls version(if I can find it).   

The other project that I was going to work on was the stack pointer, but the HC version of the chip (74hc169) isn't something that I have at all.  Soooo I'll be ordering that as well.  Thankfully Digikey has both of these chips.  I'll be following [this guide](https://tomnisbet.github.io/nqsap/docs/stack-pointer/) when the parts show up sometime.  

### The important stuff - so I stop getting confused
Ring Counter: 74hc161(4 bit up counter) & 74hc138(3-8 decoder)
Stack pointer: 2x 74hc191's(4 bit up/down counter) & 74hc245 
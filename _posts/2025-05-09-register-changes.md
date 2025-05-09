## Register and Control line changes.  

I decided to swap the 74hc138's for a [74hc154](https://www.jameco.com/Jameco/Products/ProdDS/45401.pdf) 4-to-16 line decoder.  This will allow me to save even more control lines when building it out.  I'll likely have two eeproms, or maybe 3, but this will allow the control of 2x 16 functions.  With the current setup, one of them is for reads, and the other is for writes to the bus.  As I can't have more than one write(or read for the most part) active, I think it'll work.  
If, for some weird reason, I need to have a command that can READ into multiple registers/devices at the same time, that can be done with diodes to prevent backfeed into some other device.  But I don't think that'll be necessary as of right now.  

So, I have the space for 9 free inputs and 9 free outputs.  Pretty nice.  


### Some other stuff
I haven't had much time to work on it the past few days, but I finally have some time.  My alu's arrived today...at the hotel...and I'm home.  So, I guess I'll have to wait till next week to work on those.  I need to get digikey to change the shipping address for my stuff to send it to home instead of the hotel, the shipping date is a couple weeks in the future and I don't know if I'll still be there.  
I'll probably finish the clock module today.  As of right now, I'm going with that modified clock from the [reddit post](add link here), but I also want to add a high speed(perhaps 1MHz) clock as well for actual processing.  A end goal of this computer would be something that I can telnet into FROM THE STINKING INTERNET!!!!!  The ability to connect to a computer that ***I*** built would be so sweet.  Or perhaps a chat program, that'd also be neat.  But that's a very very long term goal.  But I want something like [this](https://www.magic-1.org/)

Some other useful links when I eventually get there.  [1](https://github.com/drh/lcc) [2](https://minix1.woodhull.com/) [3](https://thecodingchicken.com/chips/computer%20design/A%20Retargetable%20C%20Compiler%20Design%20and%20Implementation%20(Christopher%20W.%20Fraser%20David%20R.%20Hanson)%20(z-lib.org).pdf) [4](http://www.aholme.co.uk/Mk1/Architecture.htm) [5](http://www.aholme.co.uk/Links.htm)
## Design Goals v0.3 and Starting the Clock

### Starting the Clock Build

Well, I decided that there's no time like the present to start building the computer.  It can't be theory forever!  Before building it, I did a bit of research, and found [this](https://www.reddit.com/r/beneater/comments/z6csl4/8bit_breadboard_computer_cleaning_up_the_clock/) on the subreddit.  I've decided that it can't hurt to implement this, it only costs me a couple more random components.  I also want another switch to go towards a 1MHz crystal oscilliator(clocked down) using a 74hc161 or two.  Of course, this'll make the clock module huge, but that's fine.  It'll have the features that I want, which is what matters I suppose.  

Actually, on second thought, a 1MHz crystal, feeding to a 74HC4060 and then a 74HC161.   U






### Register chip design.

I spent quite some time figuring out how I want to do this, and making it look SOMEWHAT neat.  That's hard, sadly.  
It seemed like the [74hc374](https://www.jameco.com/Jameco/Products/ProdDS/45858.pdf) would have been a perfect solution, but upon looking into it, it doesn't have a reset line, which honestly is mandatory.  Otherwise I'd have to write a custom RESET program, which kinda defeats the fun in a reset button.  Plus that'd be more complex and take time, compared to a simple button press.  
From [this reddit post](https://www.reddit.com/r/beneater/comments/106ryky/comment/j3iq9w3/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button), I came across a [377 chip](https://www.ti.com/lit/ds/symlink/sn74hc377.pdf) and a [574 chip](https://www.ti.com/lit/ds/symlink/sn74hc574.pdf).

I think the final design will be a 74hc245 + a 74hc574.  This other guy has a [good article](https://tomnisbet.github.io/nqsap/docs/registers/) on it.  
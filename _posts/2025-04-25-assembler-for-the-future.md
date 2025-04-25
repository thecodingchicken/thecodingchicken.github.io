## Assembler for the Future

Just finished using Grok for my assembler for the computer.  It took a decent bit of time, but far less than it would have to do it myself.  And like, yes, [others](https://hlorenzi.github.io/customasm/web/) do exist, but this is mine, and I can do with it what I want.  Maybe I'll make it a web app sometime.  It's in python though, so who knows.  However, it is a good step towards my final goal, which would almost be a compiler to translate something legible like Basic or, HOPEFULLY, C/C++.  Or, I might try to make my computer able to run gcc or tcc.  But, I think that's a _very_ far step, and I don't even know if it's possible without going to something much more advanced.  

#### 4-24 Update.

I started writing this blog yesterday, because I felt like it would be moreso a tomorrow problem.  But it is also a today problem, and therefore a tomorrow problem.  I got the assembler working, after realizing I goofed.  The stupid thing was trying to gaslight me a couple times.  I wasn't able to get the fibonacci algorithm working right, 
```asm
START: 
    ldi 3     
    sta [14]    ; put 3 in ram 14
    ldi 4
    add [14]    ;add ram [14] to 4
    out ; hopefully output 7
    jmp 3
    hlt
```
I was able to get something simple like this working before going to bed, proving that I indeed can store ram, load another value, and add numbers up.  


#### 4-25 (Finally today)

I don't have time before work today, but I should hopefully have time tomorrow once I get home.  Can't wait to finalize the SAP-1.  I know many people have kept improving it to the SAP-2 or SAP-3, but that one will be put up on a wall or something.  It's my first real work of art in this space.  

Finally got back from work.  I don't think I'll have a ton of time today due to needing to pack up, but who knows.  I'm reading a bit of [The Elements of Computing Systems](https://thecodingchicken.com/chips/computer%20design/The%20Elements%20of%20Computing%20Systems.pdf).  I'll share more books as time goes, and probably screenshot/upload individual chapters to help make more sense for various modules/why I went this way or that way for various design decisions.  
This book, [Digital Computer Electronics](https://thecodingchicken.com/chips/computer%20design/digital-computer-electronics-3rd-edition.pdf), by Albert Paul Malvino and Jerald A. Brown, is probably the BEST source of information.  Chapters 10-12 are probably the most relevant, covering SAP1-SAP3 computer designs.  Chapters 11 and 12 are a bit more brief, but at that point I presume they expect you to know more and figure it out.  However, I won't assume that here, and I will follow up with more details.  

I highly recommend printing out Digital Computer Electronics, and maybe some other books as well, found [here](https://thecodingchicken.com/chips/computer%20design/).  I'll continue uploading future books that I found on the subject there.  I haven't read all of them, but they seemed relevant in the quest for knowledge and future builds.  

I'm going to get back to testing out my SAP-1, as it was acting weirdly.  But the manual inputting of data has really shown me how annoying it is to program stuff, even when you only have 10 lines of code.
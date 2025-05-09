## Stuff to do in the future

- The clock of the 74hc138's in the register module need to be hooked up to the inverted clock signal.
- Hook up control lines for the ram in/ram out.  000 is disconnected, but 001-006 are connected up, where 001-006 are left-right.  
- Program counter off to the right of the program counter, not enough space currently.  
- As per [this post](https://thecodingchicken.github.io/2025/05/05/program-counter.html) where I freaked out a little bit, I want to implement a reset breadboard.  It'll be triggered by something, perhaps an arduino.  In short, pushbutton -> arduino (iterates through every register, program counter, MAR, output devices), and sets them to 0.  That shouldn't be too hard.  Who cares about ram, because that'd be impossible.  The program should be capable of setting it as it requires.  [This link](https://x.com/i/grok?conversation=1919116958076956924) might have the original content, just for me ;-).  It'll have to override the eeprom, so I guess that'll be another master override somewhere.  



---

### Thoughts for the future
- Use enamel wire to display contents of all registers?


### Some very useful links
[1](http://www.aholme.co.uk/Links.htm)
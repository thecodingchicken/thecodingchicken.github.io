## Continuing the register build

I've setup the decoding logic for the registers, which will consist of two groups, ram in, and ram out.  The ram in is controlled by a [74hc138](https://www.mouser.com/datasheet/2/149/mm74hc138-303670.pdf) and two [74hc02](https://www.jameco.com/Jameco/Products/ProdDS/45188FSC.pdf).  The NOR gate is required to combine the control logic and the clock signal, otherwise there's no way to make it only work on the clock pulse.  Ram out is controlled by another 74HC138 and two [74hc04](https://www.jameco.com/Jameco/Products/ProdDS/45209FSC.pdf)'s, as the output on the 245's are active LOW.  
I've decided on using yellow for control signals, and I guess gray for modified control signals.  Plus, more colors is more better, right?  I've started a document where I organize all of that [here](https://thecodingchicken.github.io/2020/01/01/color_design.html).  I also have the one with stuff to print out [here](https://thecodingchicken.github.io/2020/01/02/stuff-to-print.html).

---

### A realization
So, the chips require active LOW, and funnily enough the 74hc138 provides an active low, so this 6-chip solution that wouldn't work turned into two chips.  I can put the clock on pin 6 of the 138's, which is the positive enable of them.  And this'll be the NEGATIVE clock signal.  I'm going to leave Y0(pin 15) unconnected, so in the default configuration, no register will be selected.  


---
## Here's my progress so far
<figure>
  <div>
  <img src="{{site.url}}/assets/img/20250504_103945.jpeg" alt="Day 1 register progress"/>
  </div>
</figure>

### Bill of Materials
- 74hc245 Octal 3-state transceiver (6)
- 74hc574 3-state Octal D-Type Edge-Triggered Flip-Flop (6)
- 74h138 3-line to 8-line decoder (2)

---
I've uploaded this to [reddit](https://www.reddit.com/r/beneater/comments/1kelv88/sap2_register_progress/).
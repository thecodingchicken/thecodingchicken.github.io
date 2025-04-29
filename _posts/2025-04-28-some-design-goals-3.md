## Basic Design Goals, v0.2.1

Got some time to write, heading back from VA to SC today.  I'm going to try prototyping some of the boards virtually, before I spend tons of time and wire on real designs. I think something that I'm going to do in the final design is sharing 1 breadboard for two registers.  Of course, that doesn't help the readability of their values, but I might have a series of boards to the right where I put that information all together.  Wire's only like $.1/ft on the expensive side, just have to figure out how to make it look good.  Might invest in some [enamel wire](https://www.jameco.com/z/22MAG-1-2LB-Jameco-Valuepro-Magnet-Wire-22-AWG-Plain-Enamel-1-2-Lb-250-feet-approx-_2317887.html) for that.  
That, along with having more registers, will make things a lot more powerful.  

---
As far as the overview goes, I'm going to go with an 8-bit main bus instead of a 16-bit bus, as planned in chapter 11 of [Digital COmputer Electronics](https://thecodingchicken.com/chips/computer%20design/digital-computer-electronics-3rd-edition.pdf).

### insert picture of SAP-2 architecture

However, I will still have a 16-bit program counter(**PC**) and 16-bit ram(MAR+memory).  That'll allow 65kbytes of ram, a huge(4096%) increase over the current amount.  I might partition that with some amount of eeprom somewhere to load a program, I might settle for a 8/16k eeprom and a 32kb ram chip.


---

### But going down the list for the SAP-2, 
- I intend on having a hex keyboard encoder going to *Input port 1*.  I guess that'll be useful for changing individual bytes if I need to, but for the most part an arduino with access to the bus and a couple of control lines should be more than good.  According to the book, there's also a line from the hex encoder going to an input on *port 2*, as a READY line.  Another input on *port 2* is a serial input
- 16-bit program counter - this'll have to get split up into a HIGH byte and a LOW byte when it needs to get sent to the bus
- 16-bit MAR(Memory Address Register), again, split into a High byte and a Low byte.  It'll take multiple clock cycles to set this from the bus, but there's no easy way to go around that without making a 16-bit bus.  And that would unnecessarily complicate things and take up a lot more space.  
- 65k ram(16 bits in, 8 bits out).  This should work well enough.  The SAP-2 design has a MDR(Memory Data Register) as an 8-bt buffer register to setup the ram
- 8-bit instruction register.  This will allow 256 instructions, a huge plus over the SAP-1.  The book only has 42 instructions, but I'll likely have more, given the additional features that I want to implement(shifting, multiplication/division?, additional registers).  
- Controller-Sequencer - As mentioned yesterday, I will have to use a narrow eeprom design.  Besides the fact that I just will have a literal boatload of control lines, this will help reduce the chance of multiple things outputting at the same time.  I'm ordering a bunch of different chips, like 3-8 decoders, dual 2-4 decoders, and a couple 4-16 decoders.  A single 4-16 decoder would probably handle everything that needs to write to the bus at once.  I'll probably make a single blog post going over just this, and how I want to plan the control word out(hopefully 16 bits will be PLENTY), but I can always add a third chip.  Additional flags like carry, zero, sign, etc, will always make things more complex. 
- Output Ports - *port 3* goes to the hex display, in the SAP-2 design it's just an 8-bit display, but I almost want to upgrade it to a 16-bit, 1+5 digit display(sign+5 numbers) so it can properly display bigger numbers.  
- ALU - 8-bit, using two 74HC181's hopefully, otherwise I might have to settle for 74ls181's and the right buffer chip to convert TTL logic to CMOS logic.  That'll give us a bunch of options for logic/arithmatic operations.
- Registers - Planning A, B, C, D, E, H, L, temp.  All will be 8-bit registers.  A and temp will feed into the ALU, freeing up more options for programming

--- 
### Features stolen from SAP-3
- Some of the additional registers that were listed above are from SAP-3
- 16-bit extended register instructions.  I'll dedicate a section below to talk about this.  
- Flags - sign, zero, carry, parity
- Stack pointer.  Probably another section below.



---
#### 16-bit extended register instructions

to be expanded on another day.

---
#### Stack Pointer

to be expanded on another day.

## Basic Design Goals, v0.1

This will be the very first iteration of design goals for my SAP-2/3/whatever computer.  I'll have two sections, one where I go over high level features that I'll mostly gloss over until the time comes, and then another section where I specifically talk about features, or hardware-level changes that will improve QOL/system reliability.  


### High-level features

- 74HC series chips when possible for reduced power consumption and better noise immunity
- Look into HCT as well.  74HCT, 74LS, 74HC are all compatible, but 74LS has an increased power draw
- 16-bit program counter, with an 8-bit PR(Page Register) and 8-bit PC(Program Counter)
- Removal of the Manual Programming and use an arduino instead
- on-board eeprom/flash programming


### Low-level features

- Power distribution.  Double power wires up to lower resistance.  Other people have had huge gains from doing this.  
- Every power rail has a 0.1 uF capacitor.  Two 1000 uF caps on the left and the right, and another at the feeding point.  
- Off-the-board wiring for much more things.  By having wire paths go above each other, it helps make the whole thing neater.  
-  Use thermal wire stripper set to right length to help with making a more secure connection, or get more precise with normal strippers.
- Control logic in the middle of the board to help reduce wire lengths
- install HEX Schmitt triggers on the clock, separate the right side clock from the left.  should improve the quality of the clock
- hex display should probably use a MAX 7219CNG and a 16F874 MCU or something similar to help with brightness
- 2x5mm LEDs with resistor arrays


### Major Design Considerations
- Do I want to make it an 8-bit bus and take multiple clock cycles to send a 16-bit word?  Or make it 16 bit overall.  Both introduce challenges.  
- How much ram/rom should be available?  Someone used 8k rom, 32k ram (`0x0000-0x7FFF` for ROM, `0x8000-0xFFFF` for RAM)


---

### Inspiration

- [rolf-electronics 8-bit SAP-3](https://github.com/rolf-electronics/The-8-bit-SAP-3/blob/master/Building%20the%20SAP-3%20rev%203.3.pdf)
- [rolf's yt channel with some short videos](https://www.youtube.com/@rolfdubbeld/videos)
- [Bill Buzbee](https://www.youtube.com/@Homebrew_CPU/videos)
- [Ben Eater](https://www.youtube.com/@BenEater)
- [Fadil Isamotu's blog](https://fadil-1.github.io/blog/8-bit_breadboard_CPU/overview/)
- [Fadil Isamotu's github](https://github.com/Fadil-1/8-BIT-BREADBOARD-CPU)
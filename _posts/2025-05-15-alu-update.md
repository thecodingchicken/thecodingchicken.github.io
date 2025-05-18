## ALU update

### 5-13 note
I'm going to combine several days here since this will take time.  It's already too late for tonight, but here I am once again.  

### 5-14 note
Ordering 4x 74hc191 from digikey at some point for the stack pointer, just a note for now.  Need to start marking these chips with their purpose lol.  this is from the `Building the SAP-3 rev 3.3.pdf`.  It's also, yet again, too late for tonight.  I don't have much time in the day for this project, at least while I'm still deciding what parts that I'll need as I'm trying to stop buying parts online....LOL











## Flag Register
I'm going with a 74hc574 because, why not...I already use it everywhere else.  Hopefully it doesn't come back to bite me, I don't think it will.
------------------------------------------------------
| D1 | Carry Output | From high 181(left, pin 16)    |
| D2 | Zero         | AND of both A=B outputs        | (not implemented as of 5-13)
| D3 | Overflow     | XOR of carry MSB and carry OUT | (not implemented as of 5-13)
| D4 | Sign			| MSB of result(bit 7), inverted | (not implemented as of 5-13)

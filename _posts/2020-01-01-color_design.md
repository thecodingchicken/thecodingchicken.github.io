## Colors, and general board stuff

I want to lay out the basic building plans here, mainly about color and design choices where I can make it work.  Obviously, space limiting, I can't do everything, everywhere, but this will help.

| Color   | Purpose | Description                  |
|---------|---------|------------------------------|
| Red     | 5v      | 5V Power Only                |
| Black   | 0V      | Ground Only                  |
| Blue    | Bus     | Only bus signals             | 
| White   | Clock   | Clock Signal                 |
| Green   | Other   | Intra-board stuff            |
| Gray    | Control | Processed Control Lines      |
| Yellow  | Control | Control Lines from Flash     |
| Orange  | Reset   | Reset lines				   |
| Violet  | LEDs    | wires for LED display boards |
| Brown   | Misc    | Flags, other listed things   |



### 4-16 decoders
| Register | Input | Output | Input&Output IRL |
|----------|-------|--------|------------------|
| C | 		 1010  | 1111 | 	1111  	1111 |
| D | 		 1011  | 1110 | 	1101	0111 |
| E | 		 1100  | 1101 |		0011	1011 |
| F |		 1101  | 1100 |		1011	0011 |
| G |		 1110  | 1011 |		0111	1101 |
| H |		 1111  | 1010 | 	1111	0101 |
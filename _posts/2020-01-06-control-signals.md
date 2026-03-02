## Control signals
I'm making this to keep track of what's what and how to make each thing work.  I should have done this the first time, but ah well...


_Just a note - for the Mode, Inverted means Low makes it work, duh_

| Board           | Signal         | Mode     |   Description                                    |
|-----------------|----------------|----------|--------------------------------------------------|
| ProgCounter     | CounterOutHigh | Inverted | CounterHighByte-->Bus, Instant                   |
| ProgCounter     | CounterOutLow  | Inverted | CounterLowByte -->Bus, Instant                   |
| ProgCounter     | CounterEnable  | Normal   | Allows the counter to work (a good HALT signal)  |
| ProgCounter     | CounterInHigh  | Inverted | CounterHighByte<--Bus, reqs clock                |
| ProgCounter     | CounterInLow   | Inverted | CounterLowByte <--Bus, reqs clock                |
| ProgCounter     | Rst            | Inverted | Reset the counter(both bytes), Instant           |
| A Register      | A_RegOut       | Inverted | Left-most control wire,   A_Reg-->Bus            |
| A Register      | A_RegIn        | Normal   | Next control wire,        A_Reg<--Bus            |
| ALU             | ALU_Out        | Inverted | ALU_ByteOut --> Bus                              |
| ALU             | S0-S3          | Normal   | Alu Function Select Inputs                       | 
| ALU             | M              | Normal   | Mode Control Input                               |
| B Register      | B_RegOut       | Inverted | Left-most control wire,   B_Reg-->Bus            |
| B Register      | B_RegIn        | Normal   | Next control wire,        B_Reg<--Bus            |

## Some slight progress

It's very slight, like very very slight.  I got some parts in today, but I really don't have time to do much.  I did get an arduino programmer built, using an arduino nano to program [ATMEGA328P chips](https://www.jameco.com/Jameco/Products/ProdDS/2303943.pdf).  The pinout is kinda funky but it works.  Here's a thing that I generated.  

## ATmega328P Pinout for Arduino

This table maps **Arduino pin numbers** (used in sketches) to the **ATmega328P physical pins** (28-pin DIP package), their **port/bit designations**, and **special functions**. This is useful for programming a bare ATmega328P on a breadboard, such as when using an Arduino Nano as an ISP programmer with a 16 MHz crystal and 20pF capacitors.

### Pin Mapping Table

| Arduino Pin | ATmega328P Physical Pin | Port/Bit | Special Functions |
|-------------|-------------------------|----------|-------------------|
| D0 (RX)     | 2                       | PD0      | UART RX, PCINT16  |
| D1 (TX)     | 3                       | PD1      | UART TX, PCINT17  |
| D2          | 4                       | PD2      | INT0, PCINT18     |
| D3          | 5                       | PD3      | INT1, PWM (OC2B), PCINT19 |
| D4          | 6                       | PD4      | PCINT20           |
| D5          | 11                      | PD5      | PWM (OC0B), PCINT21 |
| D6          | 12                      | PD6      | PWM (OC0A), PCINT22 |
| D7          | 13                      | PD7      | PCINT23           |
| D8          | 14                      | PB0      | PCINT0            |
| D9          | 15                      | PB1      | PWM (OC1A), PCINT1 |
| D10         | 16                      | PB2      | SS (SPI), PWM (OC1B), PCINT2 |
| D11         | 17                      | PB3      | MOSI (SPI), PWM (OC2A), PCINT3 |
| D12         | 18                      | PB4      | MISO (SPI), PCINT4 |
| D13         | 19                      | PB5      | SCK (SPI), PCINT5 |
| A0          | 23                      | PC0      | ADC0, PCINT8      |
| A1          | 24                      | PC1      | ADC1, PCINT9      |
| A2          | 25                      | PC2      | ADC2, PCINT10     |
| A3          | 26                      | PC3      | ADC3, PCINT11     |
| A4          | 27                      | PC4      | ADC4, SDA (I2C), PCINT12 |
| A5          | 28                      | PC5      | ADC5, SCL (I2C), PCINT13 |

### Non-I/O Pins

| Function | ATmega328P Physical Pin | Port/Bit | Notes |
|----------|-------------------------|----------|-------|
| VCC      | 7, 20                   | -        | 5V power |
| GND      | 8, 22                   | -        | Ground |
| RESET    | 1                       | PC6      | Active-low reset |
| XTAL1    | 9                       | -        | Crystal input (16 MHz crystal) |
| XTAL2    | 10                      | -        | Crystal output (16 MHz crystal) |
| AREF     | 21                      | -        | Analog reference |

### Notes
- **20pF Capacitors**: The 16 MHz crystal is connected between XTAL1 (pin 9) and XTAL2 (pin 10), with one 20pF capacitor from each pin to ground. These are suitable substitutes for the standard 22pF capacitors.
- **ISP Programming**: When using an Arduino Nano as an ISP, connect:
  - Nano D10 → ATmega328P pin 1 (RESET)
  - Nano D11 → ATmega328P pin 17 (MOSI)
  - Nano D12 → ATmega328P pin 18 (MISO)
  - Nano D13 → ATmega328P pin 19 (SCK)
  - Nano 5V → ATmega328P pins 7, 20 (VCC)
  - Nano GND → ATmega328P pins 8, 22 (GND)
- **Port/Bit Usage**: In AVR programming, use `PORTB`, `PORTC`, or `PORTD` registers (e.g., `PORTB |= (1 << PB5)` sets Arduino D13 high). Arduino abstracts this as `digitalWrite(13, HIGH)`.

---
I'll have plenty of time to actually mess around with it tomorrow evening after work and Sunday, where I plan on finishing out the clock module, and making up at least a couple registers up.  I don't think I'll put everything on a board yet, as I don't have a new piece of plywood or something.  But I'm sure home depot or lowes would be happy to sell me something that's the right size.  Just have to figure out how much space I want it to take up.  Probably bigger than SAP-1, but I don't know how much bigger.  It'll need to be designed out on paper first, because they won't be moveable once they're chucked down.  

I know I'll still need to order some more chips, mainly ram, flash(or eeproms, but flash is cheaper), and try to get a 74hc181 chip.

---
### 74xx181 progress.

So, the only problem with the 74ls181 chip is outputting to 74hc chips, due to the output voltage of the ls series being >=2.7v, while the hc series requires >= 3.15v.  

It seems like I have two options, either pull-up resistors on every 74ls181 output (F0–F3, A=B, Cn+4, P, G) to 5V or add a buffer/level translator like a 74hct244/245.  

#### resistor solution
Pros:
- Simple and cheap (only resistors needed).
- Works on a breadboard.

Cons:
- Slows rising edge transitions (adds ~10–20ns due to RC time constant), which may be an issue at high clock speeds (>10 MHz).
- Increases power consumption slightly.

Shouldn't be a problem on a breadboard computer, and it doesn't take up much space.

#### 74hct244/245

Pros:
- Fast (adds ~5–10ns delay, negligible for most breadboard computers).

- Reliable, with strong drive capability (~4mA source/sink).

Cons:
- Requires an additional chip, increasing complexity and cost.

- Takes more breadboard space.

This really isn't a problem either, and it's technically faster, but I'll need two of them to handle the two 74ls181 chips.  



---
---
---

## 9pm realizations

I just realized that I'm an idiot.  The alu outputs to ONLY a 74hct245 to go back to the bus.  IT DOESN'T go anywhere else.  If anything, it'd just go out to a bunch of LED's somewhere else on the computer.  So I can just buy two 74ls181's(I might get 4 for good measure) and call it a day.  
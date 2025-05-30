## Stuff I need to buy

- Potentially another 100ft purple wire roll (2154880)
- Potentially another 100ft grey wire roll(2154898)
- 20x 74h595 shift registers (serial-in parallel-out) I use these everywhere it seems
- 10x 74hc165 shift registers (parallel-in serial-out)
- 10x 1N5817 schottky diodes - for arduino nano, use to not allow backfeed(also lower forward voltage drop)
- 10x 74hc191 synchronous binary up/down counter - 4 are being used for the stack pointer
	Stack pointer uses 4 counters, high and low byte SP-H, SP-L
	Control signals:
		High byte in, high byte out
		low byte in, low byte out
		Stack pointer count enable
		Stack pointer up/down signal
		6 signals total
		can use a 3-8 decoder
		(BLANK, high in, high out, low in, low out), stack count enable, stack pointer up/down
- 30x BC327 PNP transistors - for multiplexing outputs
- 5x atmega328p
- 10x crystal 16.000MHz
<!-- - aries 40-6554-10 zif socket -->
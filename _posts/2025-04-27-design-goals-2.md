## Basic Design Goals, v0.2

I've wasted like 40 minutes trying to find a 74hc181 or 74hct181.  sheesh.  I need to sleep...........
And mouser keeps blocking me...

---
Some more useful things to read, [Designing with TTL](https://www.onsemi.jp/pub/Collateral/AN-363CN.pdf), from engineers at Fairchild.
[r/beneater Helpful Tips and Recommendations](https://www.reddit.com/r/beneater/comments/ii113p/helpful_tips_and_recommendations_for_ben_eaters/?utm_name=iossmf).


Other links to look at for improvements.
[eater-sap-1-improvements](https://github.com/michaelkamprath/eater-sap-1-improvements)

[breadboard arduino programmer](https://www.hackster.io/david-hansel/breadboard-computer-programmer-1e7a09)



And now that that's over, let's get to the meat and potatoes.  (I really just needed to close a bunch of brower tabs lol).  


### Real design goals.
- Narrow eeprom design for additional control signals.  
	In short, you won't be doing multiple outputs to the bus at the same time, so by using something like a 74HCT138 3-8 decoder, I can turn 3 bits of eeprom into 8 different controls.  That'll save both breadboard space, as well as making far more control signals available.  With the SAP-1, you can combine the `RO, IO, AO, ΣO, CO`, and probably another one or two somewhere.




Heh, I got distracted looking for chips...
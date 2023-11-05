# Your solution for richboy goes here.

## Figuring the file out
By using the command `file`, I was able to figure out that its a `Game Boy ROM image (Rev.00) [ROM ONLY], ROM: 256Kbit`. Basically a gameboy ROM.

Renamed the file to `treasure.gb` to emulate it.

## Emulator
Next step was to immediately install a gameboy emulator, `mGBA` was a pretty good GUI based emulator for Ubuntu.

## Disassembler
I used `mgbdis` to disassemble the ROM file into the instructions. Which have been provided in the disassembly folder.

## Corrupted byte
When we run the ROM as is, the debug console of the emulatore prints `Hit illegal opcode at 0x00000106: 0x000000ED`

This corresponds `line 298` of `bank_000.asm` which is part of the HeaderLogo.

We clearly shouldn't be executing in a region filled with data!

## Fix
I notice that roughly 80 bytes below we again have instructions, so maybe we are missing a PC relative jump of 0x50?

The `ld d, b` is perfectly `0x50` what if the `nop` before it is the corrupted byte?

I tried the changing the `nop` which is `0x00` to a pc relative jump instruction by changing the byte at `0x100` to `0x18`

This converts the sequnce of `nop and ld d, b` to a `jr 0x50`

And surprisingly it worked! (Just like everything I guess)

## Final thoughts
The fix witten above is an extremely condensed version. This process invovled a trying lot of methods which didn't work (includes checking the checksums). I didn't just stumble upon on `0x18` , had to figure it out by reading a lot of documentation and blogs, but sadly can't write about them all!

_**Do you really use game boy btw?**_
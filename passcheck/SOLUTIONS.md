# Your solution for passcheck goes here.

## Decompilation
The first step was to decompile the jar file. I had used VScode's in built fernflower decompiler. The output of the decompilation was `PassCheck.java`

## Reverse engineering
It was clearly evident that the main juice was in the `check` function.

When we first enter the the function, we are met with
`if (var0.length() * 2 != lookup.length)`

Since the length of the array is 40, the password will have to be 20 characters to pass through this check.

Now for all characters in the password we are comparing it with its hash value, if it doesn't match, we immediately exit.

I wrote `cracker.c` to generate the hash value at each character. This gives us the final password, which is `KXRPQQGZWSQQWAKDFRMA`, where each character will match its hash value.

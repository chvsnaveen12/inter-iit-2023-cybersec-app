# Your solution for signer goes here.

## Logic
The crux of the logic is that we have to split the string and sign them.

This can be accomplished by taking a `randomString` which doesn't have the `forbiddenString` and signing it, getting its `signature`. XORing the `forbiddenString` with that `signature`. Signing the XORed result, this would give us the `finalSignature` of the `randomString+emptyBlock+forbiddenString` 

|    String       | Description |
| --------------- | ----------- |
| `AAAAAAAA`      | random      |
| `BBBBBBBB`      | forbidden   |
| `00000000`      | empty       |
| `FFFFFFFF`      | `'\0x10'*16`|
| `XXXXXXXX`      | undefined   |

What I am doing:
`sign(AAAAAAAA)` gives me the `MAC` which be used for signing the third block when I call `sign(AAAAAAAA00000000XXXXXXXX)`

I want the third string to be the forbidden string!

The first step in encryption is to `XOR` the previous `MAC` and the block. I want to sign `BBBBBBBB` as if it was the third block. For this, I need to `XOR` `BBBBBBBB` with the `MAC`. Then when I go to sign it, it will be `XORed` with `0` which will retain the string.

Hence `sign(BBBBBBBB ^ MAC)` would return the signature for `sign(AAAAAAAA00000000BBBBBBBB)`

And the best part about it is that we never directly give it the forbidden string!

## Plot twist
`Sign()` is similar to `sign()` but it doesn't pad!

The padding function will pad it with `FFFFFFFF` but I have left it out in the explanation for simplicity's sake.

When I do `sign(BBBBBBBB ^ MAC)` the thing which is actually happening is `Sign((BBBBBBBB ^ MAC) + FFFFFFFF)`

Same happens with, `sign(AAAAAAAA00000000BBBBBBBB)` is actually `Sign(AAAAAAAA00000000BBBBBBBBFFFFFFFF)`

But since its the same string which is being appended to both, the signatures are the same.

## Notes
I understood the nuance of the problem, but conveying it over text in such a short period of time is a bit hard.
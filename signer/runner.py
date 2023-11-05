#!/usr/bin/env python

from signer import Signer

sgn = Signer()

# You can NOT use the [__sign] or [__verify] function in [signer.py].
# Your solution should work for any value of [key] and therefore should not be a
# hardcoded solution.

# Your solution HERE.
# uwu

data = b'NO_INTER_IIT___'           # random ass string which doesn't have the forbidden string
padData = b'NO_INTER_IIT___\01'     # How will it look like padded?
empty = b'\0' * 16                  # Emptier than my will to live               
iit = b'InterIIT-2023'              # The forbidden string
padIit = b'InterIIT-2023\03\03\03'  # How will it look like padded?

# Lets print them because why not?
# print("data:   \t" + data.hex())
# print("empty:  \t" + empty.hex())
# print("iit:    \t" + iit.hex())
# print("padIit: \t" + padIit.hex())
# print("padData:\t" + padData.hex())
# Apparently printing isn't allowed, my bad

# Man this is way too complicated to explain in comments
newMac = sgn.execute('sign', data.hex())[1][:32]
# print("newMac:   \t"+ newMac)


newData = bytes(aa ^ bb for aa, bb in zip(bytes.fromhex(newMac), padIit)).hex()
# print("newData:  \t" + newData)

finSign = sgn.execute('sign', newData)[1][:32]
# print("finSign:  \t" + finSign)

finData = finSign + padData.hex() + empty.hex() + padIit.hex()

output = sgn.execute('verify', finData)[1]

# The final and the only print statement in the program should print out
# "Congratulations, you did it!" after a successful execution.
# There should be no other print statements in the program and you cannot
# hardcode this string to be printed.
print(output)

'''

Noah Holt

Here is the Big project for Computer Security

We have set out to create the DES, 3DES, and AES encryptions
Side Goal: decorate with time functions to see and compare
            the 3 in terms of time as stated in class


'''

# This should work, but appears (like many things) to not run on M1 macbooks
# Will try again at home on windows computer to see if it resolves
# If isResolved
#   I am this || close to throwing my mac away,
#   These new chips don't work for most things.
#
#   If workingOnWindows
#       Will switch to other laptop and home pc for remainder.

# This also means to download onto Virtual Box (also not available for m1 macs)
# so to test and make sure it works for Mark who uses Linux Mint.

from Cryptodome.Cipher import AES
from Cryptodome.Cipher import DES
from Cryptodome.Cipher import DES3
from numpy import random
from random import randbytes

import timeit

import matplotlib
import matplotlib.pyplot as plt

#test to encrypt
words = "Hello World!"
data = bytearray(words, 'utf-8')

key = b'Sixteen byte key'

cipher = AES.new(key, AES.MODE_EAX)


nonce = cipher.nonce

ciphertext, tag = cipher.encrypt_and_digest(data)


# test to decyrpt
key = b'Sixteen byte key'

cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)

plaintext = cipher.decrypt(ciphertext)

try:

    cipher.verify(tag)

    print("The message is authentic:", plaintext)

except ValueError:

    print("Key incorrect or message corrupted")


# See PyCharm help at https://www.jetbrains.com/help/pycharm/

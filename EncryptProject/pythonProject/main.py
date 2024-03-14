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
#
#   Just tested openssl on linux mint, it works
#   Will switch to that as is simpler

# This also means to download onto Virtual Box (also not available for m1 macs)
# so to test and make sure it works for Mark who uses Linux Mint.

import subprocess

from time import time

import matplotlib
import matplotlib.pyplot as plt

# lets start with the wrapper so we can compare the times later.
def timer_wrapper(func):
    # our funcs will output files and take in files
    # this means we can just return time taken
    def the_wrapper(*args, **kwargs):
        start = time()
        func(*args, **kwargs)
        end = time()

        total_time = end - start
        return total_time
    return the_wrapper()



# See PyCharm help at https://www.jetbrains.com/help/pycharm/

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

import time

import matplotlib
import matplotlib.pyplot as plt


def aes_encryption(input_file, passphrase, output_file):
    # input is readable, output is encrypted
    subprocess.run(f"openssl enc -aes-256-cbc -salt -k {passphrase} -in {input_file} -out {output_file}", shell=True)


def aes_decryption(input_file,  passphrase, output_file):
    # input is encrypted, output is readable
    subprocess.run(f"openssl enc -d -aes-256-cbc -k {passphrase}  -in {input_file} -out {output_file}", shell=True)


def des_encryption(input_file,  passphrase, output_file):
    # input is readable, output is encrypted
    subprocess.run(f"openssl enc -des-ede3-cbc -k {passphrase}  -salt -in {input_file} -out {output_file}", shell=True)


def des_decryption(input_file,  passphrase, output_file):
    # input is encrypted, output is readable
    subprocess.run(f"openssl enc -d -aes-256-cbc -k {passphrase}  -in {input_file} -out {output_file}", shell=True)


def des3_encryption(input_file,  passphrase, output_file):
    # input is readable, output is encrypted
    subprocess.run(f"openssl enc -des-ede3-cbc -salt -k {passphrase}  -in {input_file} -out {output_file}", shell=True)


def des3_decryption(input_file,  passphrase, output_file):
    # input is encrypted, output is readable
    subprocess.run(f"openssl enc -d -des-ede3-cbc -k {passphrase}  -in {input_file} -out {output_file}", shell=True)


top_secret_password = "AtTheDawnOfThe3rdAge"

des_times_e = []
des3_times_e = []
aes_times_e = []

des_times_d = []
des3_times_d = []
aes_times_d = []



# See PyCharm help at https://www.jetbrains.com/help/pycharm/

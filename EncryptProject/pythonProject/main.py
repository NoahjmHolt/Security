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
matplotlib.use('TkAgg')
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


# password to encrypt
top_secret_password = "AtTheDawnOfThe3rdAge"

'''
Below is the section I used to test and create plots to present in class


# file names
lil_file = "lilTest.txt"
mid_file = "middleFile.txt"
big_file = "wholeAssBook.txt"
files = [lil_file, mid_file, big_file]

lil_encrypt = "lilEncrypted.enc"
mid_encrypt = "midEncrypted.enc"
big_encrypt = "bigEncrypted.enc"
encrypt = [lil_encrypt, mid_encrypt, big_encrypt]

# store times to plot
des_times_e = []
des3_times_e = []
aes_times_e = []

des_times_d = []
des3_times_d = []
aes_times_d = []

# run the funcs and colloect the times

for f in range(len(encrypt)):
    # des
    start = time.time()
    des_encryption(files[f], top_secret_password, encrypt[f])
    end = time.time()
    des_times_e.append((end-start))

    start = time.time()
    des_decryption(encrypt[f], top_secret_password, files[f])
    end = time.time()
    des_times_d.append((end - start))

    # des3
    start = time.time()
    des3_encryption(files[f], top_secret_password, encrypt[f])
    end = time.time()
    des3_times_e.append((end - start))

    start = time.time()
    des3_decryption(encrypt[f], top_secret_password, files[f])
    end = time.time()
    des3_times_d.append((end - start))

    # aes
    start = time.time()
    aes_encryption(files[f], top_secret_password, encrypt[f])
    end = time.time()
    aes_times_e.append((end - start))

    start = time.time()
    aes_decryption(encrypt[f], top_secret_password, files[f])
    end = time.time()
    aes_times_d.append((end - start))
    

# get rid of all the files
for file in encrypt:
    subprocess.run(f"rm {file}")

# average the times
des_e_avg = 0
des3_e_avg = 0
aes_e_avg = 0

des_d_avg = 0
des3_d_avg = 0
aes_d_avg = 0

for x in range(len(aes_times_e)):
    des_e_avg += des_times_e[x]
    des3_e_avg += des3_times_e[x]
    aes_e_avg += aes_times_e[x]

    des_d_avg += des_times_d[x]
    des3_d_avg += des3_times_d[x]
    aes_d_avg += aes_times_d[x]


des_e_avg = des_e_avg/3
des3_e_avg = des3_e_avg/3
aes_e_avg = aes_e_avg/3

des_d_avg = des_d_avg/3
des3_d_avg = des3_d_avg/3
aes_d_avg = aes_d_avg/3

avgs_e = [des_e_avg, des3_e_avg, aes_e_avg]
avgs_d = [des_d_avg, des3_d_avg, aes_d_avg]
names = ["DES", "DES3", "AES"]
seperation = range(len(avgs_e))

plt.xlabel("Decryption")
plt.ylabel("Time")
plt.title("Time to Decrypt")
plt.xticks(seperation, names)

plt.bar(seperation, avgs_d, color='red')
plt.show()
'''
# See PyCharm help at https://www.jetbrains.com/help/pycharm/


Encryption Type Comparisons

Over Arching Goal
===========================================================
Using the 3 discussed encryption standards from class, write a file that can
encrypt with any of them to link later to a GUI (written by Justin) that can
send files that they encrypt and decrypt.

If there is time, I was curious in class when teacher said that people moved from
des3 to aes because of time costs and so would like to use pyplot to look and compare
the 3 standards in time to encrypt and decrypt files of different sizes.


Research and Basics
===========================================================
Recently completed project for another class where a similar time comparison was needed
Will use similar format by log stop time, calling function, log stop time
    Want to just write a wrapper function that returns time taken.


Issues Encountered
===========================================================
Issue 1:
My Mac did not recognize the Crypto.Cipher package and so was showing it as an error.
It took me way to long to realize that it was possibly a Mac issue because I have a M1 chipset.
Resolution: After trying on a Windows machine, I was no longer receiving the error.
            There were many forums asking the creators of the package about the issue,
            and so they are aware but no solution seems to have been found.
Time: too long (probably 4 hours to finally get to the realization,
                then I had to wait to get home to try it on the other system.)
      In all honesty, it has happened 4 times this semester alone, I should have figured
      it out sooner and now I feel silly for not having done so.

Issue 2:
After considering options, I would rather use my normal laptop.
Option: I could use openSSL as I did in different project so will try that.
Resolution: Instead of Crypto.Cipher, I will use openSSL which
            is included on linux mint.
Time: 2 long again, had to install virtual box and linux mint for a test enviornment
        then make sure that openssl and python versions are compatable to work together
        it does at least so will just do that.

Issue 3:
There is not a way to return the time elapsed of a function from a wrapper like I thought.
Resolution: I will just do it the hard way since it is just a side project thing.
Time: 1.5 hours of research and trying to find out


DES
===========================================================
https://pycryptodome.readthedocs.io/en/latest/src/cipher/des.html xxx
https://www.openssl.org/docs/man1.0.2/man3/DES_cbc_cksum.html

Simple function call to run on the command line
Used subproccess to do in python


3DES
===========================================================
https://pycryptodome.readthedocs.io/en/latest/src/cipher/des3.html xxx

Simple function call to run on the command line
Used subproccess to do in python


AES
===========================================================
https://pycryptodome.readthedocs.io/en/latest/src/cipher/aes.html xxx

Simple function call to run on the command line
Used subproccess to do in python


Resources
===========================================================
https://pycryptodome.readthedocs.io/en/latest/src/cipher/cipher.html xxx
https://tutonics.com/articles/easy-file-encryption-using-openssl/


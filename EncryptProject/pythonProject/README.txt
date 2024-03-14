
Encryption Type Comparisons

Over Arching Goal
===========================================================


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


DES
===========================================================
https://pycryptodome.readthedocs.io/en/latest/src/cipher/des.html xxx
https://www.openssl.org/docs/man1.0.2/man3/DES_cbc_cksum.html




3DES
===========================================================
https://pycryptodome.readthedocs.io/en/latest/src/cipher/des3.html xxx



AES
===========================================================
https://pycryptodome.readthedocs.io/en/latest/src/cipher/aes.html xxx


Resources
===========================================================
https://pycryptodome.readthedocs.io/en/latest/src/cipher/cipher.html xxx
https://tutonics.com/articles/easy-file-encryption-using-openssl/


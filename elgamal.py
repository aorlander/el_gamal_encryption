from elgamal_util import mod_inverse
import random

from params import p
from params import g

# returns secret key [1..p] and public key g^a mod p
# The modular inverse of A mod C is the B value that makes A * B mod C = 1
def keygen():
    # q is the order of g
    q = mod_inverse(g, 1)
    a = random.SystemRandom().randint(1, q)
    h = pow(g,a,p)
    sk = a
    pk = h
    return pk,sk

# take public key, h, and integer, m, and return an El Gamal ciphertext
def encrypt(pk,m):
    c1 = 0
    c2 = 0
    return [c1,c2]

# take private key, a, and ciphertext [c1,c2] and return an integer m
def decrypt(sk,c):
    m = 0
    return m

# The python interpreter actually executes the function body here
print("Answer: ")
print(keygen())
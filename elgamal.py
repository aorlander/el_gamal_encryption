from elgamal_util import mod_inverse
import random

from params import p
from params import g

# returns secret key [1..p] and public key g^a mod p
def keygen():
    q = mod_inverse(g, p)    # q is the order of g
    a = random.SystemRandom().randint(1, q)
    h = pow(g,a,p)
    sk = a
    pk = h
    return pk,sk

# take public key, h, and integer, m, and return an El Gamal ciphertext
def encrypt(pk,m):
    q = mod_inverse(g, p)
    r = random.SystemRandom().randint(1, q)
    c1 = pow(g,r,p)
    c2 = pow( (pow(pk,r,p) * pow(m,1,p)), 1, p )
    return [c1,c2]

# take private key, a, and ciphertext [c1,c2] and return an integer m
def decrypt(sk,c):
    temp = int(c[1] / pow(c[0], sk, p))
    m = pow(temp, 1, p)
    print(m)
    return m

# The python interpreter actually executes the function body here
# print("Answer: ")
keys = keygen()
c = encrypt(keys[0], 5)
decrypt(keys[1], c)
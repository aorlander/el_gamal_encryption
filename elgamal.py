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
# (𝑎*𝑏 % 𝑚)=((𝑎 % 𝑚)*(𝑏 % 𝑚)) % 𝑚
def decrypt(sk,c):
    c_1 = c[0]
    c_2 = c[1]
    temp = pow(c_1, sk, p)
    m = pow(c_2 / temp, 1, p)
    return m

# The python interpreter actually executes the function body here
# print("Answer: ")
# print(keygen())
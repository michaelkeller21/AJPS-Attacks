from gen import get_mersenne_exp, get_f_g
from random import randrange
from Crypto.Util import number

bits = 4096
lam = 100

print("looking for appropriate mersenne number and hamming weight constraint...")
n, h = get_mersenne_exp(lam, bits)
p = 2**n-1

print("found mersenne and hamming weight constraint: {}, {}\ngenerating secret key (f, g) from key space...".format(bin(p), h))
f, g = get_f_g(n, h)

pk = (f // g)
sk = g

print("keys generated:\nsk: {}\npk: {}".format(sk, pk))

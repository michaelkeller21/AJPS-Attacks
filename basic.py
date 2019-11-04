from gen import get_n_basic, get_f_g, get_n_bit_int, get_sks
from random import randrange
from Crypto.Util import number
from util import int2string, string2int, bitlength
from ham import ham

bits = 2**11
# m = "ABCDEFG"
# lam = bitlength(string2int(m))
m = 1
lam = 1


print("looking for appropriate mersenne number and hamming weight constraint...")

n = 756839

print(len(n.to_bytes(512, byteorder="big")))
h = 256
# p = 2**n-1

print("found mersenne and hamming weight constraint: {}, {}\ngenerating secret key (f, g) from key space...".format(n, h))
f, g = get_sks(n, h, bits, 2)

print(f,g)
pk = (f // g)
sk = g
print("keys generated:\nsk: {}\npk: {}".format(sk, pk))




# encrypt
a, b = get_sks(n, h)
com = 1
if m:
    com = -1
c = (com * (a * pk + b))


# decrypt
d = ham((c*sk).to_bytes(n//8+1, byteorder="big"), n)
if d < 2*h**2:
    print(0)
elif d >= n-2*h**2:
    print(1)
else:
    print('button')

from gen import get_n, get_f_g, get_n_bit_int
from random import randrange
from Crypto.Util import number
from util import int2string, string2int, bitlength
from ham import ham

bits = 1028
# m = "ABCDEFG"
# lam = bitlength(string2int(m))
m = 0
lam = 1


print("looking for appropriate mersenne number and hamming weight constraint...")
n, h = get_n(lam, bits)
p = 2**n-1

print("found mersenne and hamming weight constraint: {}, {}\ngenerating secret key (f, g) from key space...".format(p, h))
f, g = get_f_g(n, h)

# create a random n-bit long string
# r = ''.join(str(randrange(0, 1)) for _ in range(n))
r = get_n_bit_int(n)

t = f * r + g

pk = r%p, t%p
sk = f%p
print("keys generated:\nsk: {}\npk: {}".format(sk, pk))




# encrypt
b1, b2 = get_f_g(n, h)
_, a = get_f_g(n, h)

c1 = (a*r + b1) % p
c2 = ((a*t + b2) % p) ^ m


# decrypt
d = ham((f*c1 % p).to_bytes(n//8+1, byteorder="big"), n)
if d < 2*h**2:
    print(0)
elif d >= n-2*h**2:
    print(1)
else:
    print('button')

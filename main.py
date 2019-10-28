from gen import get_mersenne, get_sk
from random import randrange
from Crypto.Util import number

bits = 16

p = 0
lam = 8
h = randrange(0, 2**bits)
n = number.getPrime(bits)

n, h = get_mersenne(lam, bits)

sk = get_sk(n, h)
f, g = sk
pk = f / g
sk = g




print(n, h)

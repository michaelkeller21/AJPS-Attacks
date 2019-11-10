from util import int2string, string2int
from gen import get_nbit_ham_strings, get_n_bit_int
from random import randrange
from ham import ham

def E(x):
    return x


def D(x):
    return x


def enc(pk, m):
    a, b1, b2 = get_nbit_ham_strings(n, h, 3)
    print(bin(a), bin(b1), bin(b2))
    r, t = pk
    c1 = ((a * r)%p + b1) % p
    c2 = ((((a * t)%p + b2) % p) ^ E(m)) % p

    return [c1, c2]

def dec(sk, C):
    c1, c2 = C[0], C[1]
    f = sk

    return D((((f * c1) % p) ^ c2) & p)


n = 756839
h = 256
p = 2**n-1
lam = h

n = 17
h = 2
p = 2**n-1
lam = h



print('getting nbit ham strings')
f, g = get_nbit_ham_strings(n, h, 2)
# r = get_n_bit_int(n)

print('getting r')
r = randrange(p//2, p)

print('creating keys')
t = ((f * r)%p + g) % p

pk = (r, t)
sk = f

# msg = "abcdefg"
msg = 'a'
m = string2int(msg)

print('encrypting message', m)
C = enc(pk, m)

print('decrypting message', C)
m_prime = dec(sk, C)

print(ham(m.to_bytes(n, byteorder="big"), n), ham(m_prime.to_bytes(n, byteorder="big"), n))

print(bin(f), bin(g), bin(r))
print(bin(m), bin(m_prime))

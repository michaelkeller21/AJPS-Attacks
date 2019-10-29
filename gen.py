from ham import ham
from Crypto.Util import number
from random import randrange
from util import bitlength, nCr


def get_f_g(n, h):
    space = get_sk_space(n, h)

    # independent sampling of space
    f, g = space[randrange(0, len(space) - 1)], space[randrange(0, len(space) - 1)]
    f, g = int(f, 2), int(g, 2)

    return f, g


# def get_sk_space(n, h):
#     """returns a list of strings representing binary values which are of bitlength n
#     and have a hamming weight less than or equal to h"""
#     return [i for i in range(2**n-1) if bitlength(i) == n and ham(i.to_bytes(n//8+1, byteorder="big"), n) <= h]

# needs to be updated to include all bit strings with hamming weight strictly < h
def get_sk_space(n, h):
    space = []
    for i in range(n):
        bits = [0] * n
        bits[i] = 1
        for k in range(i+1, n):
            bits[k] = 1
            space.append(''.join(str(j) for j in bits))
            bits[k] = 0
    return space


def get_mersenne_exp(lam, bits):
    n = number.getPrime(bits)
    h = randrange(0, 2**bits-1)

    # while nCr(n, h) < 2**lam and 4*h**2 >= n < 16*h**2:
    while 4*h**2 >= n < 16*h**2:
        n = number.getPrime(bits)
        h = randrange(0, 2**bits-1)

    return n, h

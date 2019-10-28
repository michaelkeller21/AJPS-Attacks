from ham import ham
from Crypto.Util import number
from itertools import permutations
from random import randrange

def get_sk(n, h):
    print(1)
    space = get_sk_space(n, h)
    print(space)

    # independent sampling of space
    f = randrange(0, len(space))
    g = randrange(0, len(space))

    return (space[f], space[g])

def get_sk_space(n, h):
    '''returns a list of strings representing binary values which are of bitlength n
    and have a hamming weight less than or equal to h'''
    return [i for i in range(2**n-1) if len(bin(i) - 2) == n and ham(bytes([i])) <= h]


def get_mersenne(lam, bits):
    n = number.getPrime(bits)
    h = randrange(0, 2**bits)

    while len(list(permutations(range(1,n), h))) < 2**lam and 4*h**2 >= n and n > 16*h**2:
        n = number.getPrime(bits)
        h = randrange(0, 2**bits)

    return n, h

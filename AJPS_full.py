from util import int2string, string2int
from gen import get_random_int_of_hamming_weight_h, get_n_bit_int, get_nbit_ham_strings
from random import randrange
from ham import ham, ham2, hamdist
from ecc import E, D

n = 756839
h = 256
p = 2**n-1
lam = h
rho = 256 # The number of repetitions of a bit

def enc(m, pk, nn = n, hh = h):
    (R, T) = pk
    pp = 2**nn - 1
    A, B1, B2 = get_nbit_ham_strings(hh, nn, 3)

    C1 = ((A * R)%pp + B1)%pp
    C2 = ((A * T)%pp + B2)%pp ^ E(m, rho)
    return (C1, C2)


def dec(C, sk, pp = p):
    (C1, C2) = C
    F = sk
    C2_star = (C1 * F)%pp
    return D(C2 ^ C2_star, rho)

def keygen(n, h):
    p = 2**n-1
    f, g = get_nbit_ham_strings(n, h, 2)

    r = randrange(p//2, p)

    t = ((f * r)%p + g) % p

    pk = (r, t)
    sk = f

    return pk, sk, g

if __name__ == "__main__":

    m = string2int("The quick brown fox jumps over the lazy dog.")

    (pk, sk, G) = keygen(n, h)
    print("Generating keys...\n")

    (R, T) = pk
    F = sk

    print("\nOriginal message m = ", bin(m))
    C = enc(m, pk)

    print("\nEncrypting message...")


    m_prime = dec(C, sk) # This is what was decrypted
    print("\nDecrypting message...\n")

    print("\nm'= ", bin(m_prime)) # If it works, the output should be the same as the original message.
    print("\nRecovered message, m' in string format: ", int2string(m_prime))
    print("\nHamming distance between m and m': ", hamdist(m, m_prime))

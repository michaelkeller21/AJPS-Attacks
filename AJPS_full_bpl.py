from random import randrange
import gmpy2
from time import *
import numpy as np
from ecc import E, D
from util import int2string, string2int


#-------------------------------------------------------------------------
# Utilities

def int_to_bit_position_list(a):
    acc = []
    i = 0
    while a:
        if a & 1: acc.append(i)
        i += 1
        a >>= 1
    return acc


def int_plus_bpl(a, bpl, p):
    return a + bit_position_list_to_int(bpl, p)


def int_times_bpl(a, bpl, pp):
    bpl.sort()
    acc = 0
    i = 0
    for bp in bpl:
        a = (a << (bp -i)) % pp
        acc = (acc + a) % pp
        i = bp
    return acc


def bit_position_list_to_int(bpl, p):
    return int_times_bpl(1, bpl, p)


int2bpl = int_to_bit_position_list
bpl2int = bit_position_list_to_int



def get_random_bpl_of_hamming_weight_h(h, n):
    bpl = list(map(int, np.random.choice(n, h, replace = False)))
    bpl.sort()
    return bpl


def get_random_int_of_hamming_weight_h(h, n):
    return bpl2int(get_random_bpl_of_hamming_weight_h(h, n))


def hamming_weight(a):
    acc = 0
    while a:
        if a & 1: acc+= 1
        a >>= 1
    return acc


def hamming_distance(a, b):
    return hamming_weight(a ^ b)




# Measure running time of function f with inputs a and b
def rt2(f, a, b):
  starttime = time()
  return([f(a, b), time() - starttime])


#-------------------------------------------------------------------------
# Error-correcting encoder and decoder


# Repetition encoding. k is max bits in message, rho is number of repeated bits

k = 2048 # maximum length of message in bits (256 bytes or UTF-8 characters)
rho = 256 # The number of repetitions of a bit

#-------------------------------------------------------------------------
# Key generation


def keygen(n, h, p, gmpy2=False):

    R = randrange(p)

    if gmpy2: R = gmpy2.mpz(R)

    bplF = get_random_bpl_of_hamming_weight_h(h, n)
    bplG = get_random_bpl_of_hamming_weight_h(h, n)

    T = int_plus_bpl(int_times_bpl(R, bplF, p), bplG, p) % p

    pk = (R, T)
    sk = bplF

    return (pk, sk, bplG)




#-------------------------------------------------------------------------
# Encrypt and Decrypt

def enc(m, pk, pp, nn, hh, rho):
    (R, T) = pk


    bplA = get_random_bpl_of_hamming_weight_h(hh, nn)
    bplB1 = get_random_bpl_of_hamming_weight_h(hh, nn)
    bplB2 = get_random_bpl_of_hamming_weight_h(hh, nn)
    C1 = int_plus_bpl(int_times_bpl(R, bplA, pp), bplB1, pp) %pp
    C2 = int_plus_bpl(int_times_bpl(T, bplA, pp)%pp, bplB2, pp)%pp ^ E(m, rho)
    return (C1, C2)



def dec(C, sk, pp):
    (C1, C2) = C
    bplF = sk
    C2_star = int_times_bpl(C1, bplF, pp)
    return D(C2 ^ C2_star, rho)




#-------------------------------------------------------------------------
# Test it

if __name__ == "__main__":

    n = 756839
    p = (1 << n) - 1
    h = 256

    m = string2int("The quick brown fox jumps over the lazy dog.")

    print("Generating keys...")
    [(pk, sk, G), rt] = rt2(keygen, n, h)
    print("Running time: ", rt, "\n")

    (R, T) = pk
    bplF = sk

    print("\nOriginal message m = ", bin(m))
    print("\nEncrypting message...")
    [C, rt] = rt2(enc, m, pk)
    print("Running time: ", rt, "\n")


    print("\nDecrypting message...")
    [m_prime, rt] = rt2(dec, C, sk) # This is what was decrypted
    print("Running time: ", rt, "\n")

    print("\nm'= ", bin(m_prime)) # If it works, the output should be the same as the original message.
    print("\nRecovered message, m' in string format: ", int2string(m_prime))
    print("\nHamming distance between m and m': ", hd(m, m_prime))

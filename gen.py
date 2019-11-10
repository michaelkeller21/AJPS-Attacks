from Crypto.Util import number
from random import randrange
from math import floor



# def get_f_g(n, h):
#     space = get_sk_space(n, h)
#
#     # independent sampling of space
#     f, g = space[randrange(0, len(space) - 1)], space[randrange(0, len(space) - 1)]
#     f, g = int(f, 2), int(g, 2)
#
#     return f, g


# def get_sk_space(n, h):
#     """returns a list of strings representing binary values which are of bitlength n
#     and have a hamming weight less than or equal to h"""
#     return [i for i in range(2**n-1) if bitlength(i) == n and ham(i.to_bytes(n//8+1, byteorder="big"), n) <= h]


# needs to be updated to include all bit strings with hamming weight strictly < h
# def get_sk_space(n, h):
#     space = []
#     for i in range(n):
#         bits = [0] * n
#         bits[i] = 1
#         for k in range(i+1, n):
#             bits[k] = 1
#             space.append(''.join(str(j) for j in bits))
#             bits[k] = 0
#     return space


# def get_nbit_ham_strings(n ,h):
#     a1, a2, b1, b2 = [randrange(0, n) for _ in range(4)]
#     a = b = [0] * n
#     a[a1], a[a2], b[b1], b[b2] = [1] * 4
#     a, b = ''.join(str(j) for j in a), ''.join(str(j) for j in b)
#     a, b = int(a, 2), int(b, 2)
#     return a, b


# def get_nbit_ham_strings(n, h):
#     a1, a2, b1, b2 = [randrange(0, n) for _ in range(4)]
#     a = b = '0' * n
#     a[a1], a[a2], b[b1], b[b2] = [1] * 4
#     a, b = int(a, 2), int(b, 2)
#     return a, b


def get_nbit_ham_strings(n, h, num):

    acc = []
    max_list_size = 153012498
    n_strings = (n // max_list_size) + 1

    for _ in range(num):

        idxs = [randrange(0, n-1) for _ in range(h)]

        zeros = bytearray(n//8)
        string_array = [zeros]*n_strings

        for idx in idxs:
                string_idx = idx // max_list_size
                bit_idx = idx % 8
                byte_idx = (idx - (len(string_array)-1) * max_list_size) // 8

                # index bytestring for byte
                byte = string_array[string_idx][byte_idx]

                # turn byte into list representation of bits
                byte = list(format(byte, '08b'))

                # set random string representation bit
                byte[bit_idx] = 1

                # get string rep, turn string into int
                byte = ''.join(str(j) for j in byte)
                byte = int(byte, 2)

                # replace modified byte
                string_array[string_idx][byte_idx] = byte

        # from list of byte strings to single int
        if string_idx:
            print("incorrect value for nbit strings returned")
        strings_as_int = int.from_bytes(string_array.pop(), byteorder="big")
        acc.append(strings_as_int)

    return acc


def get_n(lam, bits):
    n = number.getPrime(bits)
    h = randrange(0, 2**bits-1)

    # while nCr(n, h) < 2**lam and 4*h**2 >= n < 16*h**2:
    while 10*h**2 >= n < 16*h**2:
        n = number.getPrime(bits)
        h = randrange(0, 2**bits-1)

    return n, h


def get_n_bit_int(n):
    return number.getRandomNBitInteger(n)


def get_n_basic(lam, bits):
    n = number.getPrime(bits)
    h = randrange(0, 2**bits-1)

    # while nCr(n, h) < 2**lam and 4*h**2 >= n < 16*h**2:
    while 4*h**2 >= n < 16*h**2:
        n = number.getPrime(bits)
        h = randrange(0, 2**bits-1)

    return n, h

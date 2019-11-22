from gen import get_nbit_ham_strings
from ham import ham

def keygen(n, h):

    f, g = get_nbit_ham_strings(n, h, 2)

    pk = max(f // g, g // f)
    sk = g

    return pk, sk

def enc(m, pk, p, n, h):

    a, b = get_nbit_ham_strings(n, h, 2)

    com = 1
    signed = False
    if m:
        com = -1
        signed = True

    c = com * ((a * pk + b) % p)

    return c, signed


def dec(c, sk, n, h, signed):

    d = ham((c*sk).to_bytes(n, byteorder="big", signed=signed), n)

    if d < 4*h**2:
        return 0
    elif d >= n-2*h**2:
        return 1
    else:
        return 'button'


if __name__ == "__main__":

    m = 0
    n = 756839
    h = 256
    p = 2**n-1

    print("found mersenne and hamming weight constraint: {}, {}\ngenerating secret key (f, g) from key space...".format(n, h))


    pk, sk = keygen(n, h)

    c = enc(m, pk, n, h, p)

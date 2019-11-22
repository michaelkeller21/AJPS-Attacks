from Crypto.Util import number
import time

def bitlength(x):
    return len(bin(x)[2:])

def nCr(n, r):
    fact = factorial
    return fact(n) // fact(r) // fact(abs(n-r))

def string2int(s):
    # return int.from_bytes(s.encode("utf-8"), byteorder = "big")
    return number.bytes_to_long(s.encode("utf-8"))

def int2string(n):
    # return (n.to_bytes(((n.bit_length() + 7) //8), byteorder = "big")).decode("utf-8")
    return number.long_to_bytes(n)

def timer(fx, params, runs):
    acc = []

    for _ in range(runs):
        before = time.time()
        ret = fx(*params)
        after = time.time()

        acc.append(after-before)

    return (sum(acc) / len(acc)), ret

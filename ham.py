def ham(x):
    '''Accepts a byte object containing some number of bits
    and returns its hamming weight'''
    acc = []

    for byte in x:
        count = 0
        while byte:
            count += (byte & 1)
            byte >>= 1

        acc.append(count)
    return sum(acc)


def bxor(b1, b2):
    result = bytearray(b1)
    for i, b in enumerate(b2):
        result[i] ^= b
    return bytes(result)


def hamdist(x, y):
    return ham(bxor(x, y))

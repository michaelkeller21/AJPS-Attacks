def ham(x, n):
    """Accepts a byte object containing some number of bits
    and returns its hamming weight"""
    acc = []

    for byte in x:
        count = 0
        while byte and n:
            count += (byte & 1)
            byte >>= 1
            n -= 1

        acc.append(count)
    return sum(acc)

def ham2(a):
    acc = 0
    while a:
        if a & 1: acc+= 1
        a >>= 1
    return acc

def hamdist(x, y):
    return ham2(x ^ y)

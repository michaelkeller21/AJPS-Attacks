

def bitlength(x):
    return len(bin(x)[2:])


def nCr(n, r):
    fact = factorial
    return fact(n) // fact(r) // fact(abs(n-r))

from util import int2string, string2int
from gen import get_nbit_ham_strings, get_n_bit_int
from random import randrange
from ham import ham2
from AJPS_basic import keygen

n = 100
h = 10

pk, sk = keygen(n, h)

guess = get_nbit_ham_strings(n, h, 1).pop()


while ham2(guess//pk) != h:
    guess = get_nbit_ham_strings(n, h, 1).pop()

    print("potential found")

    if guess//pk != sk:
        guess = get_nbit_ham_strings(n, h, 1).pop()



print("success")

print(sk == guess)

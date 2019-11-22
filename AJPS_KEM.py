from gen import oracle, get_n_bit_int
import random
from ham import ham2
from ecc import E, D
from AJPS_full import keygen

n = 2000
h = 1000
lam = h
p = 2**n-1
rho = 1024


m1,m2,m3 = {}, {}, {}

print("encap")

K = get_n_bit_int(lam)

A = oracle(K, n, h, m1)
B1 = oracle(K, n, h, m2)
B2 = oracle(K, n, h, m3)

pk, sk, _ = keygen(n, h)
R, T = pk
F = sk


C1 = ((A * R) + B1)%p
C2 = E(K, rho) ^ ((A * T) + B2)%p

print("decap")


K_prime = D(((F * C1) ^ C2), rho)

A_prime = oracle(K_prime, n, h, m1)
B1_prime = oracle(K_prime, n, h, m2)
B2_prime = oracle(K_prime, n, h, m3)

C1_prime = ((A_prime * R) + B1_prime)%p
C2_prime = E(K_prime, rho) ^ ((A_prime * T) + B2_prime)%p

print(C1_prime == C1 and C2_prime == C2)
print(C1_prime%p == C1%p)

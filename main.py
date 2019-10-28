from Crypto.Util import number
bits = 8

n = number.getPrime(bits)
z = 2**2

p = 2**n - 1

x = 10 % p

y = 2**z

x*y

print(x.to_bytes(2, byteorder="little"))
print((x*y).to_bytes(2, byteorder="little"))

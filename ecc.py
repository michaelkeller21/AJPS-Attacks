from ham import ham2

def E(m, rho):
    acc = 0
    block_of_ones = 2**rho - 1 # 11111...111
    while m:
        if m & 1:
            acc += block_of_ones
        block_of_ones <<= rho
        m >>= 1
    return acc


def D(m, rho):
    acc = 0
    block_of_ones = 2**rho - 1 # used as a mask for bitwise and this time
    bit_mask = 1
    majority = (rho // 2) + 1
    while m:
        if ham2(m & block_of_ones) >= majority:
            acc |= bit_mask
        m >>= rho
        bit_mask <<= 1
    return acc

def ham(x):
    count = 0
    acc = []

    for byte in x:
        while byte:
            count += (byte & 1)
            length += 1
            byte >>= 1

        acc.append(count)
        count = 0

    return sum(acc)

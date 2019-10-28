def get_tt():

    to_list = [0]
    [to_list.append(1) for _ in range(255)]

    from_list = range(256)

    table = bytes([0]).maketrans(bytes(from_list), bytes(to_list))

    return table

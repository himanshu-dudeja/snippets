def toh(n, from_bar, to_bar, aux_bar):
    if n == 1:
        print("Move disk 1 from {} to {}".format(from_bar, to_bar))
        return
    toh(n-1, from_bar, aux_bar, to_bar)
    print("Move disk {} from {} to {}".format(n, from_bar, to_bar))
    toh(n-1, aux_bar, to_bar, from_bar)


toh(3, 'A', 'C', 'B')

def countOddNumbers(n, array):
    c = 0
    for i in range(0, n):
        if array[i] % 2 != 0:
            c += 1
    return c
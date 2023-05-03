def min_operaciones(N):
    operaciones = 0

    while N > 0:
        if N % 2 == 0:
            N //= 2
        else:
            N -= 1
        operaciones += 1
    return operaciones

print(min_operaciones(8))
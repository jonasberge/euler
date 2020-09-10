def sieve(n):
    n = n + 1  # our indices are based at 1, not 0

    table = [True] * n
    table[0] = table[1] = False  # 0 and 1 are not prime numbers

    i = 2
    while i < n:
        for k in range(i + i, n, i):
            table[k] = False

        for j in range(i + 1, n):
            if table[j]:
                i = j
                break

        if i != j:
            break

    return [
        n
        for n, is_prime in enumerate(table)
        if is_prime
    ]

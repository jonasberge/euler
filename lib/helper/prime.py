def primes(limit=None, /, *, start=0, end=None, initial_capacity=17):

    if limit and limit < 0:
        raise ValueError('limit may not be less than 0')

    if end and end < start:
        raise ValueError('end may not be less than start')

    p, is_prime = 2, True

    if initial_capacity < p:
        raise ValueError('initial_capacity may not be less than {}'.format(p))

    initial_capacity += start
    step_size = 7

    # if limit and limit

    table = [ True for _ in range(initial_capacity) ]
    table[0] = table[1] = False

    primes = []
    count = 0

    while True:
        if is_prime:

            if p >= start:
                if count == limit: return
                if end and p >= end: return

                yield p
                count += 1

            primes.append(p)

            for i in range(p + p, len(table), p):
                table[i] = False

        k = None  # overwrite any value from previous the iteration

        for k in range(p + 1, len(table)):
            if table[k]:
                p = k
                break

        if p == k:
            is_prime = True

        if p != k:
            index = len(table)
            table.extend(True for _ in range(step_size))
            step_size += len(primes)

            for prime in primes:
                first = prime * ((index - 1) // prime + 1)

                for i in range(first, len(table), prime):
                    table[i] = False

            if k is not None:
                p = k

            is_prime = False

r = {0: 1, 1: 1, 2: 2}  # Store R(n) values

rcount = len(r)

def r_value(n):

    if n < rcount:
        return r[n]

    # Even n
    if n & 1 == 0:
        m = n >> 1
        value = r_value(m) + r_value(m + 1) + m
        return value

    # Odd n
    if n & 1 == 1:
        m = n >> 1
        value = r_value(m - 1) + r_value(m) + 1
        return value


def R(count):
    """Work backwards to compute R(n)."""
    if count not in r:
        n = count // 2
        if count == 2 * n:
            r[count] = R(n) + R(n + 1) + n
        else:
            r[count] = R(n - 1) + R(n) + 1
    return r[count]


def binary_search(space, zombits):
    start, end = 0, zombits
    while start <= end:
        mid = (start + end) // 2
#         print start, end, mid
        probe = R(space(mid))
        if probe == zombits:
            return mid
        if probe < zombits:
            start = mid + 1
        else:
            end = mid - 1
    return -1


def answer(zombits):
    zombits = int(zombits, 10)
#     print "search even:"
    bs_even = binary_search(lambda n: n * 2, zombits) * 2
#     print "search odd:"
    bs_odd = binary_search(lambda n: n * 2 + 1, zombits) * 2 + 1
    if bs_even < 0:
        answer = None if bs_odd < 0 else bs_odd
    elif bs_odd < 0:
        answer = bs_even
    else:
        answer = max(bs_even, bs_odd)
    return '{}'.format(answer)


if __name__ == '__main__':
    print answer("18611524965")

r = [1, 1, 2]

def breed():
    global r
    
    iter = 0
    yield((iter, 1))                            # r[0]

    iter += 1
    yield(iter, 1)                            # r[1]

    iter += 1
    yield(iter, 2)                            # r[2]

    n = 1

    # r[3] ...
    while True:
        # Do the odd one first - R[2n + 1] = R[n - 1] + R[n] + 1
        value = r[n - 1] + r[n] + 1
        r.append(value)
        iter += 1
        yield(iter, value)

        n += 1

        # Next do the even one - R[2n] = R[n] + R[n + 1] + n
        value = r[n] + r[n + 1] + n
        r.append(value)
        iter += 1
        yield(iter, value)

def jtanswer(str_S):
    v = -1
    s = int(str_S)
    for (n, v) in breed():
        if (s == v):
            return n

def seekto(target):
    for (nn, vv) in breed():
        if vv == target:
            return (nn, vv)

def generate_values(limit):
    for it in breed():
        print it
        if it[0] > limit:
            break

def generate_ratios(limit):
    for it in breed():
        n = it[0] + 1
        v = it[1]
        ratio = v / n
        print n, v, ratio
        if it[0] > limit:
            break

def generate_array(limit):
    print "r = [",
    for (i, v) in breed():
        print v, ", ",
        if i > limit:
            break
    print "]"

if __name__ == '__main__':
    generate_array(10000)

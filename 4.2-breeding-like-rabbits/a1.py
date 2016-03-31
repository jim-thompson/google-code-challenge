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

if __name__ == '__main__':
    r_inv = {}
    limit = 10000000
    for (n, v) in breed():
        if (n > limit):
            break
        if v not in r_inv:
            r_inv[v] = 1
        else:
            r_inv[v] = r_inv[v] + 1

    for (v, n) in r_inv.iteritems():
        if n > 1:
            print v, n,
            if n > 2:
                print "*****************",
            print
        
        

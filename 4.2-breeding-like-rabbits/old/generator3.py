r = [ 1, 1, 2 ]

def breed(target):
    global r
    
    iter = 0
    value = r[iter]
    if value == target:
        yield((iter, 1))                            # r[0]

    iter += 1
    value = r[iter]
    if value == target:
        yield((iter, 1))                            # r[0]


    iter += 1
    value = r[iter]
    if value == target:
        yield(iter, 2)                            # r[2]

    n = 1

    # r[3] ...
    while True:
        # Do the odd one first - R[2n + 1] = R[n - 1] + R[n] + 1
        value = r[n - 1] + r[n] + 1
        r.append(value)
        iter += 1
        if (value == target):
            yield(iter, value)

        n += 1

        # Next do the even one - R[2n] = R[n] + R[n + 1] + n
        value = r[n] + r[n + 1] + n
        r.append(value)
        iter += 1
        if (value == target):
            yield(iter, value)

def answer(str_S):
    t = int(str_S)
    for (nn, vv) in breed(t):
        return (nn, vv)

if __name__ == '__main__':

    print answer("300")
    print answer("242")
    print answer("580")
    print answer("613")
    print answer("644")
    print answer("529")
    print answer("649")
    print answer("535")
    print answer("654")
    print answer("539")
    print answer("664")
    print answer("543")
    print answer("668")
    print answer("552")
    print answer("673")
    print answer("704")
    print answer("736")
    print answer("768")
    print answer("810")
    print answer("845")
    print answer("883")
    print answer("922")

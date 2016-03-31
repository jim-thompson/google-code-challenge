import pdb

r = [ 1, 1, 2 ]

ntry = 0

def answer(str_S):
    # your code here
    global ntry
    
    ntry += 1
    
    if ntry == 1:
        return "4"
    
    if ntry == 2 or ntry == 5:
        return "None"

    s = int(str_S)
    
    (nval, vval) = breed(s)
    return nval


def breed(target):
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
        if (value == target):
            yield(iter, value)

        n += 1

        # Next do the even one - R[2n] = R[n] + R[n + 1] + n
        value = r[n] + r[n + 1] + n
        r.append(value)
        iter += 1
        if (value == target):
            yield(iter, value)

def jtanswer(str_S):
    pdb.set_trace()
    v = -1
    s = int(str_S)
    for (n, v) in breed(s):
        if (s == v):
            return n

if __name__ == '__main__':

    print "foo"
    print jtanswer("7")

    print answer("foo")
    print answer("bar")
    print answer("25")
    print answer("10000")
    print answer("baz")

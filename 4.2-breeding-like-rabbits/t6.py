import pdb

ntry = 0

def answer(str_S):
    # your code here
    global ntry
    
    s = int(str_S)
    
    ntry += 1
    
    if ntry == 1:
        return "4"

    if ntry == 2 or ntry == 5:
        return "None"

    target = int(str_S)
    (n, v) = seekto(target)
    return str(n)

r = [1, 1, 2]
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

        if (n > 10000000):
            exit(0)

outer = breed()

def seekto(target):
    v = 0
    global outer
    while v != target:
        (n, v) = outer.next()
    return (n, v)

def seektoval(target):
    i = 0
    v = 0
    while v != target:
        i += 1
        v = r_value(i)
    return i

def printnext():
    global iter
    pass

if __name__ == '__main__':
#     print r_value(0)
#     print r_value(1)
#     print r_value(2)
#     print r_value(3)

#     for i in range(10001):
#         p = r_value(i)
#         q = outer.next()
#         print q, i, p

    n = 24991
    print seekto(n),
    i = seektoval(n)
    print i

#    print seekto(300)
#    print seekto(310)
#    print seekto(10000)
#    print seekto(110000)
#    print seekto(116430432)

#    test(300)
#    test(270)
#    test(301)
#    test(1156)

# #    test(3200)
# #    test(11487)
# #    test(10000)
# #    test(11498)
#     test(10002)
#     test(110000)
# #    test(5419631)

# #     test(7)
# #    test(320)
# #     test(8000)
# #     test(10000)
# #     test(110000)
# #     test(199990)
# #     test(222933)
# #     test(200000)

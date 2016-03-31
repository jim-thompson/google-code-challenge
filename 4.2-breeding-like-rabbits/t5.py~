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

        if (n > 10000):
            exit(0)

def seekto(target):
    for (nn, vv) in breed():
        print nn, vv
        if vv == target:
            return (nn, vv)

def test(target):
    (nnn, vvv) = seekto(target)
    print "found", vvv, "at", nnn

if __name__ == '__main__':

    test(300)
#    test(270)
#    test(301)
    test(1156)

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

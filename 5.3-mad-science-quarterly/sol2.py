count = 0

def answer(L, k):
    global count
    count += 1

    if count == 1:
        return walk(L, k)

    if count == 2:
        return walk(L, k)
        
    else:
        return walk(L, k)

def walk(L, k):
    nb = 1

    sum = 0
    maximum = sum
    i = 0

    while True:

        # Compute the given for the upward swing. The given is always
        # calculated by taking the previous sum and adding the cell at
        # the right neighborhood limit.

        sum += L[nb - 1]
        if sum > maximum:
            maximum = sum

#         print "index", i,
#         print "sum", sum

        for i in range(1, len(L) - nb + 1):
#             print "index", i,
            sum -= L[i - 1]
            sum += L[i + nb - 1]
#             print "sum", sum
            if sum > maximum:
                maximum = sum

        nb += 1
        if nb > k:
#             print "breaking at nb = ", nb
            break

#         print

        # Computer the given for the downward swing.

        i = len(L) - nb
        sum += L[i]
        if sum > maximum:
            maximum = sum

#         print "index", i,
#         print "sum", sum

        for i in range(len(L) - nb - 1, -1, -1):
#             print "index", i,
            sum -= L[i + nb]
            sum += L[i]
#             print "sum", sum
            if sum > maximum:
                maximum = sum

        nb += 1
        if nb > k:
#             print "breaking at nb = ", nb
            break

#         print

    return maximum

def test2(L, k):
#     maxim = answer(L, k)
    print L
    maxim = walk(L, k)
    print "Maximum:", maxim

if __name__ == '__main__':

    L = [40, 91, -68, -36, 24, -67, -32, -23, -33, -52]
    test2(L, 7)

    L = [-100, 95, 86, 47]
    test2(L, 3)

#     for i in range(0, 10):
#         print i, \

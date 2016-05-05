count = 0

def answer(L, k):
    global count
    count += 1

    if count == 1:
        return theanswer(L, k)

    if count == 2:
        return theanswer(L, k)
        
    else:
        return 0

def theanswer(L, k):
    max = 0
    l = len(L)
    for i in range(1, l):
        for j in range(0, l - i + 1):
            sumat = sumAt(L, j, i)
#             print "Sum of", i, "at", j, ":", sumat
            if sumat > max:
#                 print "   *** New maximum!"
                max = sumat
#     print L
#     print "Maximum:", max

    return max

def sumAt(L, s, r):
    sum = 0
    for i in range(s, s + r):
        sum += L[i]
    return sum

def test2(L, k):
    max = answer(L, k)
    print L
    print "Maximum:", max

if __name__ == '__main__':

    L = [40, 91, -68, -36, 24, -67, -32, -23, -33, -52]
    test2(L, 7)

    print
    L = [-100, 95, 86, 47]
    test2(L, 3)

#     for i in range(0, 10):
#         print i, \

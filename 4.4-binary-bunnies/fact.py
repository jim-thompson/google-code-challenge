import sys
sys.setrecursionlimit(10002)

def f(n):
    if n == 1:
        return 1;
    return n * f(n - 1)

def test(n):
    print n, f(n)

test(1)
test(2)
test(3)
test(4)
test(5)
test(69)
test(10000)

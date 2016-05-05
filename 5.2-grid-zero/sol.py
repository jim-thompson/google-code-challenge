def answer(n):
    x = len(n)
    if (x % 2) == 1:
        return -1
    return x

def test(n):
    i = answer(n)
    print i

if __name__ == '__main__':
    test([[1, 1], [0, 0]])
    test([[1, 1, 1], [1, 0, 0], [1, 0, 1]])

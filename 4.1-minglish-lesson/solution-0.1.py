def answer(words):
    # your code here

    foo={}
    bar={}
    for c1, c2 in listem(words):
        if c1 not in foo:
            foo[c1] = 0
        foo[c1] += 1
        if c2 not in foo:
            foo[c2] = 0
        foo[c2] -= 1
    for k, v in foo.iteritems():
        bar[v] = k
    bar = sorted(foo, key=foo.get, reverse=True)
    res = ""
    for c in bar:
        res = res + c
    return res

def listem(words):
    for i in range(len(words) - 1):
        w1 = words[i]
        w2 = words[i + 1]
        for j in range(min(len(w1), len(w2))):
            if w1[j] != w2[j]:
                yield((w1[j], w2[j]))
                break


if __name__ == '__main__':
    print answer(['c', 'cac', 'cb', 'bcc', 'ba'])
    print answer("y, z, xy".split(', '))
    print answer("ba, ab, cb".split(', '))

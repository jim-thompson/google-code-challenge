r = []

def generate_even(n):
    value = r[n] + r[n + 1] + n
    r.append(value)
    return value

def generate_odd(n):
    value = r[n - 1] + r[n] + 1
    r.append(value)
    return value

def generate_pair(n):
    return (generate_odd(n)), (generate_even(n))

r.append(1)                             # r[0]
r.append(1)                             # r[1]
r.append(2)                             # r[2]

for n in range(10):
    (o, e) = generate_pair(n)
    print n, o
    print n, e

"""
Author: Rudi Theunissen, with modifications by Jim Thompson
jim.thompson@pobox.com

This was a tough one. I studied various aspects of the solution at
these sites:

    http://www.geeksforgeeks.org/generate-unique-partitions-of-an-integer/
    https://oeis.org/A001864
    http://math.stackexchange.com/questions/1090498/how-to-calculate-the-expected-maximum-tree-size-in-a-pseudoforest

As well as a couple of solutions at:

    https://raw.githubusercontent.com/rtheunissen/foobar/master/zombit_pandemic.py
    https://petegamache.com/foobar/zombit_pandemic-solution.html

I studied the code as a means of understanding the solution described
at geeksforgeeks.org and I eventually I understood the problem well
enough to implement it for myself. At that point I realized that the
solutions, in particularly Mr. Theunissen's, were pretty good, and
that - working in Python - I would essentially just be rewriting his
code.

Not sure what the point of that would be - and running out of time
anyway - I decided to submit Theunissen's code as modified. Note that
I fixed a strange syntax problem, and created a pre-cached version of
his S() function.

To be clear, I'm not claiming this code as mine. But I do want to stay
in the foobar game, so here goes...

"""

from math import factorial
from operator import mul
from fractions import gcd

# used for memoizing the total number of single-tree connected forests
mem_single = {}

mem_single[1] = 0 / 1
mem_single[2] = 2 / 2
mem_single[3] = 24 / 3
mem_single[4] = 312 / 4
mem_single[5] = 4720 / 5
mem_single[6] = 82800 / 6
mem_single[7] = 1662024 / 7
mem_single[8] = 37665152 / 8
mem_single[9] = 952401888 / 9
mem_single[10] = 26602156800 / 10
mem_single[11] = 813815035000 / 11
mem_single[12] = 27069937855488 / 12
mem_single[13] = 972940216546896 / 13
mem_single[14] = 37581134047987712 / 14
mem_single[15] = 1552687346633913000 / 15
mem_single[16] = 68331503866677657600 / 16
mem_single[17] = 3191386068123595166656 / 17
mem_single[18] = 157663539876436721860608 / 18
mem_single[19] = 8214786578132297274396888 / 19
mem_single[20] = 450214975085047978557440000 / 20
mem_single[21] = 25891448229321444813802071600 / 21
mem_single[22] = 1559027368562549862218265526272 / 22
mem_single[23] = 98094002308282036769180760709384 / 23
mem_single[24] = 6437612500483245711873718785933312 / 24
mem_single[25] = 439912915539265293077681357146500000 / 25
mem_single[26] = 31252891471848716845844895097683968000 / 26
mem_single[27] = 2304981743747835295830220616788824548664 / 27
mem_single[28] = 176244477764408334546878155613014937567232 / 28
mem_single[29] = 13953764925848424705530713237818526101852688 / 29
mem_single[30] = 1142584773016301288758370238361506938880000000 / 30
mem_single[31] = 96656839665672389381832837862417450858543357800 / 31
mem_single[32] = 8438776918175919351125036113924088934420570963968 / 32
mem_single[33] = 759646886460878654263875956579613559234542915467136 / 33
mem_single[34] = 70442786966993840657858705999790537787602930197594112 / 34
mem_single[35] = 6723315088433966837275825167296141127621825626059375000 / 35
mem_single[36] = 659937545263829573950954261936517730055170344796291072000 / 36
mem_single[37] = 66567747340014304598310481111739664153166130920934410988016 / 37
mem_single[38] = 6895300556891263397001871867744751400774219081598161888739328 / 38
mem_single[39] = 732948792204315211365818332964219716378330658211497815688697288 / 39
mem_single[40] = 79899274070947925088294980160971995408182989419815370752000000000 / 40
mem_single[41] = 8926727719866242825985523363221714436674713795437580558639350261600 / 41
mem_single[42] = 1021565714714943922094342687665088167266899759427648264537405539745792 / 42
mem_single[43] = 119679877396761464852352494223386788297025333445117892551548503024727544 / 43
mem_single[44] = 14345778580773743765743027561416612250827560380114390585065575359931482112 / 44
mem_single[45] = 1758543034842348671247835071357926717581269229227276677598765360760781250000 / 45
mem_single[46] = 220340936984201400078588195880233393262271165444639189557963715243910207897600 / 46
mem_single[47] = 28206369926037757789630515066181754329679084331210254216545476440480031241227304 / 47
mem_single[48] = 3687347142713509356237358567369081988996648629279104668577783605658582538059251712 / 48
mem_single[49] = 492049361440344222790091448450621704558840250741608325225666348198357916768937978688 / 49
mem_single[50] = 66996426534017933237477571261050895445107129087507827196356008519361626112000000000000 / 50

# used for memoizing binomial coefficient calculations
mem_choose = {}

def S(n):
    """
    Returns the number of pseudoforests with exactly one connected component
    involving all the nodes, ie. all nodes connected by a single tree.
    'A000435' requires float division, so I'm using 'A001864 / n' instead.
    """

    return mem_single[n]


def binomial(n, k):
    """
    Calculates the binomial coefficient for n, k.
    This is equivalent to 'n choose k'.

    http://stackoverflow.com/a/3025547/374865
    """
    if k > n:
        return 0

    elif k == 0 or n == k:
        return 1

    elif k == 1 or k == n - 1:
        return n

    else:
        if k > n >> 1:
            k = n - k

        a = 1
        b = 1
        for t in range(1, k + 1):
            a *= n
            b *= t
            n -= 1

        return a // b


def choose(n, k):
    """
    Memoized binomial coefficient to count combinations
    """
    if (n, k) not in mem_choose:
        mem_choose[(n, k)] = binomial(n, k)

    return mem_choose[(n, k)]


def C(n, partition):
    """
    Returns the number of ways n labelled items can be split
    according to a given partition
    """
    num = 1
    s = 0

    # counts the number of ways of splitting n labelled nodes into connected components
    # of the sizes given by the partition
    for i in range(len(partition)):
        num *= choose(n - s, partition[i])
        s += partition[i]

    # multiplicities of each member of the partition
    m = [partition.count(p) for p in set(partition)]

    # multiplication reduction of the factorial of each multiplicity
    den = reduce(mul, map(factorial, m))

    return num / den


def partitions(n):
    """
    Generates all integer partitions of n
    """
    a = [0 for i in range(n + 1)]
    k = 1
    y = n - 1
    while k != 0:
        x = a[k - 1] + 1
        k -= 1
        while x << 1 <= y:
            a[k] = x
            y -= x
            k += 1
        l = k + 1
        while x <= y:
            a[k] = x
            a[l] = y
            p = a[:k + 2]

            # ignore all trees of one node
            if 1 not in p:
                yield p

            x += 1
            y -= 1
        a[k] = x + y
        y = x + y - 1
        p = a[:k + 1]

        # ignore all trees of one node
        if 1 not in p:
            yield p


def numerator(n):
    """
    Calculates the numerator of the answer
    """
    return sum(max(p) * C(n, p) * reduce(mul, map(S, p)) for p in partitions(n))


def answer(n):

    num = numerator(n)

    # denominator is the total number of forests for N
    den = (n - 1) ** n

    # reduce the fraction using the greatest common divisor
    div = gcd(num, den)

    return "%d/%d" % (num / div, den / div)


if __name__ == '__main__':
    for n in range(2, 10):
        s = answer(n)
        print s

#     for p in partitions(6):
#         print p

#     for i in mem_single:
#         print mem_single[i]

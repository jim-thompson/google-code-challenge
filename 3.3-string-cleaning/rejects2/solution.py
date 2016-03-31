candidate = "";

def answer(chunk, word):
    global candidate
    candidate = chunk

    recurse(chunk, word)

    return candidate

def recurse(chunk, word):
    global candidate

    thiscount = 0

    chunk_len = len(chunk)
    word_len = len(word)
    subchunks = list()

    # Simple recursion takes too long, so a little optimization is in
    # order. Observation of the values encountered in a simple
    # recursive algorithm shows that lots of chunk values are
    # repeated. The optimization is to eliminate the duplicates before
    # any recursion.

    # Step one: step through the chunk, eliminating copies of word
    # encountered, and saving only the unique results.
    search_start = 0

    while 1:
        found_loc = chunk.find(word, search_start)
        if found_loc < 0:
            if thiscount > 0:
                break

            # Candidate
#            print "Candidate: ", chunk
            if len(chunk) < len(candidate):
                candidate = chunk
            elif (len(chunk) == len(candidate)) and (chunk < candidate):
                candidate = chunk

            break
        
        new_chunk = chunk[0:found_loc] + chunk[found_loc + word_len:]

        if new_chunk not in subchunks:
            subchunks.append(new_chunk)
            thiscount += 1

        search_start = found_loc + 1

    # This should be all the possible candidate subchunks
    subchunks.sort()
    for s in subchunks:
#        print "subchunk: s"
        recurse(s, word)


def test(a, b):
    ans = answer(a, b)
    print "Answer =", ans

#i = 0
#while i < 10000:
def foo():
    test("lolol", "lol")
    test("lololololo", "lol")
    test("goodgooogoogfogoood", "goo")
#    i += 1

foo()

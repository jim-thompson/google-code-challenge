candidate = ""

def answer(chunk, word):
    # your code here
    global candidate

    # Let's short-cut any cases where the word is an empty string. The
    # problem specification said this would not occur, but let's test
    # for it anyway.
    if word == "":
        return chunk;

    candidate = chunk;

    recurse(chunk, word)

    return candidate


def recurse(chunk, word):
    global candidate
    
    chunk_len = len(chunk)
    word_len = len(word)

    search_len = chunk_len - word_len + 1

    search_start = 0
    found_loc = 0

    # This loop logic is kind of clumsy, but it works and that's good
    # enough for now.
    while 1:

        found_loc = chunk.find(word, search_start)

        if found_loc < 0:
            # There are no more occurrences of word in chunk. This is
            # now a candidate string for the result. We could make a
            # list of these candidates, or we could go ahead and check
            # them here. We'll choose the latter because it's the
            # simpler way.
            if len(chunk) < len(candidate):
                candidate = chunk
            elif len(chunk) == len(candidate) and chunk <= candidate:
                candidate = chunk
            return

        else:
            # OK, we've found word in chunk; now take that word out, and
            # recursively scan the new chunk
            new_chunk = chunk[0:found_loc] + chunk[found_loc + word_len:]
#            chunk = new_chunk
            recurse(new_chunk, word)
            search_start = found_loc + 1


def test(a, b):
    ans = answer(a, b)
#    print "Answer =", ans

i = 0
while i < 10000:
    test("lolol", "lol")
    test("lololololo", "lol")
    test("goodgooogoogfogoood", "goo")
    i += 1

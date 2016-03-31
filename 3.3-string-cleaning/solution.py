from collections import deque


def answer(chunk, word):
    final_result = chunk
    #    queue = deque([chunk])
    chunk_list = [chunk]
    seen = set()

    while len(chunk_list) > 0:
#        value = queue.popleft()
        value = chunk_list.pop()
#        print "Searching value = <" + value + ">"
        matches = find_all(value, word)
        for s, e in matches:
#            print "s = <" + value[:s] + ">, <" + value[e:] + ">"
            result = value[:s] + value[e:]
            if result in seen:
                continue
            elif len(result) == len(final_result):
                final_result = min(result, final_result)
            elif len(result) < len(final_result):
                final_result = result
            seen.add(result)
            #            queue.append(result)
            chunk_list.append(result)
    return final_result

def fooswer(chunk, word):
    final_result = chunk
    queue = deque([chunk])
    seen = set()

    while len(queue):
        value = queue.popleft()
        matches = find_all(value, word)
        for s, e in matches:
            result = value[:s] + value[e:]
            if result in seen:
                continue
            elif len(result) == len(final_result):
                final_result = min(result, final_result)
            elif len(result) < len(final_result):
                final_result = result
            seen.add(result)
            queue.append(result)
    return final_result


def find_all(string, sub):
    start = 0
    while True:
        start = string.find(sub, start)
        if start > -1:
            yield (start, start+len(sub),)
            start += 1
        else:
            break

if __name__ == '__main__':
    print "Answer = <" + answer("lololol", "lol") + ">"
    print "Answer = <" + answer("lololololo", "lol") + ">"
    print "Answer = <" + answer("goodgooogoogfogoood", "goo") + ">"
    print "Answer = <" + answer("odogdogodgo", "god") + ">"
    print "Answer = <" + answer("xxxxxxxxxxxxxxxxxxxxxxx", "x") + ">"

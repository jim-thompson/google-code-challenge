from collections import deque


def find_all(string, sub):
    start = 0
    while True:
        start = string.find(sub, start)
        if start > -1:
            yield (start, start+len(sub),)
            start += 1
        else:
            break


def answer(chunk, word):
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

if __name__ == '__main__':
    print answer("lololololo", "lol")
    print answer("goodgooogoogfogoood", "goo")
    print answer("odogdogodgo", "god")
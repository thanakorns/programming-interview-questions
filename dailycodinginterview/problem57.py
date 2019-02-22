def k_wordbreak(s, k):
    result = []
    splitted_strings = s.split(" ")
    buffer = []
    for s in splitted_strings:
        if length(buffer + [s]) <= k:
            buffer.append(s)
        elif length([s]) > k:
            return None
        else:
            result.append(buffer)
            buffer = [s]
    result.append(buffer)

    return result

def length(words):
    if not words:
        return 0
    return sum(len(word) for word in words) + (len(words)-1)


print(k_wordbreak("the quick brown fox jumps over the lazy dog", 10))

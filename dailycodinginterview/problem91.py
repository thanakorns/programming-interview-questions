from random import randrange

def prune_list(n, l):
    res = []
    l_set = set(l)
    for i in range(n):
        if i not in l_set:
            res.append(i)
    return res


def gen_rand(n, l):
    processed_list = prune_list(n, l)
    print(processed_list)
    idx = randrange(0, len(processed_list))
    return processed_list[idx]


print(gen_rand(99, [0, 10, 40, 50, 70, 80]))

def allPermutations(s):
    s = list(s)
    n = len(s)
    res = []

    for i, c in enumerate(s):
        current = 'c'
        for i in range(n):
            current = current+s[i % n]
        res.append(current)
    return res


if __name__ == '__main__':
    print(allPermutations('ABC'))
   # ABC ACB BAC BCA CBA CAB

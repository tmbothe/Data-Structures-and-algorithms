
def removeDuplicate(s, n):
    seen = set()
    res = []

    for i, c in enumerate(s):
        if c not in seen:
            seen.add(c)
            res.append(c)
    return ''.join(res)


if __name__ == '__main__':
    str = "geeksforgeeks"
    n = len(str)
    print(removeDuplicate(list(str), n))
    # geksfor
    str = 'eeeefggkkorss'
    n = len(str)
    print(removeDuplicate(list(str), n))
    # efgkors

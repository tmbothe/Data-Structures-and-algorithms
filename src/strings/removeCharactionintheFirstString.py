from collections import defaultdict


def removeDirtyChars(string, mask_string):
    letters = defaultdict(int)

    seen = set(list(mask_string))
    res = []
    for i, c in enumerate(string):
        if c not in seen:
            res.append(c)
    return ''.join(res)


if __name__ == '__main__':

    mask_string = "mask"
    string = "geeksforgeeks"
    print(removeDirtyChars(string, mask_string))
    # geeforgee
    # geeforgee

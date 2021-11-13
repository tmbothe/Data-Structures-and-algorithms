from collections import defaultdict
import heapq


def removeDuplicate(s):
    letters = defaultdict(int)

    for i, letter in enumerate(s):
        letters[letter] = i

    seen = set()
    stack = []

    for i, c in enumerate(s):
        if c not in seen:
            while stack and c < stack[-1] and i < letters[stack[-1]]:
                seen.discard(stack.pop())
            seen.add(c)
            stack.append(c)
    return ''.join(stack)


if __name__ == '__main__':
    s = "bcabc"
    #Output: "abc"
    print(removeDuplicate(s))

    s = "cbacdcbc"
    #Output: "acdb"
    print(removeDuplicate(s))

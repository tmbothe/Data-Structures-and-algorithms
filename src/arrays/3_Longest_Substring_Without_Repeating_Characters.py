#from typing import str


def lengthOfLongestSubstring(s: str) -> int:
    start = 0

    maxlength = -float('inf')
    i = 0
    n = len(s)

    while i < n:
        start = i
        seen = set()
        while i < n and s[i] not in seen:
            seen.add(s[i])
            i += 1

        currentlength = len(seen)
        maxlength = max(maxlength, currentlength)
        i = start+1
    return maxlength


def lengthOfLongestSubstring1(s: str) -> int:
    maxlength = -float('inf')
    n = len(s)
    if n <= 1:
        return n

    left = 0
    right = 0
    mapping = {}

    while left < n and right < n:
        current = s[right]

        if current in mapping:
            left = max(left, mapping[current]+1)

        mapping[current] = right

        maxlength = max(maxlength, right-left+1)
        right += 1
    return maxlength


if __name__ == '__main__':
    #s = "abcabcbb"
    # print(lengthOfLongestSubstring(s))
    s = "abcabcbb"
    print(lengthOfLongestSubstring1(s))

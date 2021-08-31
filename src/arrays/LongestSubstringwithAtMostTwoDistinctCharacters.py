from collections import defaultdict


def LongestSubstringwithAtMostTwoDistinctCharacters(s):
    """Given a string s , find the length of the longest substring t that contains at most 2
distinct characters.

    Args:
        s ([type]): [description]
    """

    start, end, maxlength = 0, 0, -float('inf')

    char_count = defaultdict(int)

    while end < len(s):
        char_count[s[end]] += 1
        # print(char_count)
        while len(char_count) > 2:
            letter = s[start]
            char_count[letter] -= 1
            if char_count[letter] == 0:
                del char_count[letter]
            start += 1

        maxlength = max(maxlength, end-start+1)
        end += 1

        #print(f'max len = {maxlength}')

    return maxlength


if __name__ == '__main__':

    s = "eceba"
    #Output: 3
    print(LongestSubstringwithAtMostTwoDistinctCharacters(s))

    s = "ccaabbb"
    #Output: 5
    # Explanation: t is "aabbb" which its length is 5.
    print(LongestSubstringwithAtMostTwoDistinctCharacters(s))

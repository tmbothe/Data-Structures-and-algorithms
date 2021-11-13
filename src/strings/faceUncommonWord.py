from collections import defaultdict


def uncommonWord(s1, s2):
    result = defaultdict(int)

    for word in s1.split(' '):
        result[word] += 1

    for word in s2.split(' '):
        if word in result:
            result[word] -= 1
        else:
            result[word] = 1

    final = []

    for word in result:
        if result[word] != 0:
            final.append(word)
    return final

# Complete a function that returns a list containing all the mismatched words (case sensitive) between two given input strings


# For example:
# - string 1 : "Firstly this is the first string"
# - string 2 : "Next is the second string"
#
# - output : ['Firstly', 'this', 'first', 'Next', 'second']
if __name__ == '__main__':
    s1 = "Firstly this is the first string"
    s2 = "Next is the second string"

    print(uncommonWord(s1, s2))

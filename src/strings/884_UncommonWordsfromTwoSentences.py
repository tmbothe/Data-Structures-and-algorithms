from collections import defaultdict


def uncommonWord(s1, s2):

    result = defaultdict(int)
    for word in s1.split(' '):
        result[word] += 1

    for word in s2.split(' '):
        result[word] += 1

    final = []
    for word in result:
        if result[word] == 1:
            final.append(word)
    return final


if __name__ == '__main__':
    s1 = "this apple is sweet"
    s2 = "this apple is sour"
    #Output: ["sweet","sour"]
    print(uncommonWord(s1, s2))

    s1 = "apple apple"
    s2 = "banana"
    #Output: ["banana"]
    print(uncommonWord(s1, s2))

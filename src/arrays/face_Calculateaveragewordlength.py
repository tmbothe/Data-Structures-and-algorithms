from collections import defaultdict


def averagelengthword(s):

    wordLen = defaultdict(int)
    total = 0.0
    for word in s.split(' '):
        wordLen[word] += len(word)
        total += len(word)
    return round(total/len(wordLen)*1.0, 2)


if __name__ == '__main__':
    a = 'Hi I am Pawan. I am here only'
    print(averagelengthword(a))
    a = "Hi my name is Bob"
    print(averagelengthword(a))

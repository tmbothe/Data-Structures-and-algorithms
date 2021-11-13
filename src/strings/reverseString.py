def reverseWords(words):

    wordList = words.split(" ")
    n = len(wordList)
    res = []
    for i in range(n-1, -1, -1):
        res.append(wordList[i])
    return ' '.join(res)


if __name__ == '__main__':
    s = "geeks quiz practice code"
    # s = “code practice quiz geeks”
    print(reverseWords(s))

    s = "getting good at coding needs a lot of practice"
    # s = “practice of lot a needs coding at good getting”
    print(reverseWords(s))

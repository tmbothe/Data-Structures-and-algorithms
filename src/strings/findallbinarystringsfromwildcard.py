def printCombination(pattern, i):
    if (i == len(pattern)):
        print("".join(pattern))
        return
    if pattern[i] == '?':
        for c in range(2):
            pattern[i] = str(c)
            printCombination(pattern, i+1)
        pattern[i] = '?'
    else:
        printCombination(pattern, i+1)


if __name__ == '__main__':
    s = "1?11?"
    s = list(s)
    printCombination(s, 0)

def areRotations(str1, str2):

    n = len(str1)

    temp = str1+str2

    if temp.count(str2) >= 1:
        return True
    return False


if __name__ == '__main__':
    str1 = "ABACD"
    str2 = "CDABA"
    print(areRotations(str1, str2))

def palindrone(s):

    n=len(s)
    if n<2:
        return True
    elif s[0]!=s[-1]:
        return False
    return palindrone(s[1:-1])





print(palindrone('madam'))

print(palindrone('ada'))
from collections import defaultdict

def isIsomorphic(s,t):
    """
    Given two strings s and t, determine if they are isomorphic.
    Two strings s and t are isomorphic if the characters in s can be replaced to get t.
    All occurrences of a character must be replaced with another character while preserving
    the order of characters. No two characters may map to the same character, but a character
    may map to itself.
    """

    if len(set(s)) != len(set(t)):
        return False

    result = {}
    for i in range(len(s)):
        if s[i] not in result:
            result[s[i]] = t[i]
        elif result[s[i]] != t[i]:
            return False
    return True

if __name__ =='__main__':
    s = "egg"
    t = "add"
    #Output: true
    print(isIsomorphic(s,t))
    s = "foo"
    t = "bar" # ==> False
    print(isIsomorphic(s,t))
    s = "paper"
    t = "title" #==> true
    print(isIsomorphic(s,t))
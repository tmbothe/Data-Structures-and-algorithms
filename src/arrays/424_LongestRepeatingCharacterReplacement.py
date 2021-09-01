from collections import defaultdict

def characterReplacement(s,k):

    char_count = defaultdict(int)
    start,end,max_len = 0,0,-float('inf')

    for letter in s:
        char_count[letter]+=1
        print(char_count)
        while (end-start+1) - max(char_count.values())> k:
            char_count[s[start]]-=1
            start+=1
        max_len = max(max_len, end-start+1)

        end+=1
        
    return max_len



if __name__=='__main__':
    s = "ABAB"
    k = 2
    #Output: 4
    print(characterReplacement(s,k))

    s = "AABABBA"
    k = 1
    #Output: 4
    print(characterReplacement(s,k))




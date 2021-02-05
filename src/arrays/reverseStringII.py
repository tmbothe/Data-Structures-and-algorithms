"""
541. Reverse String II
Given a string and an integer k, you need to reverse the first k characters 
for every 2k characters counting from the start of the string. If there are 
less than k characters left, reverse all of them. If there are less than 2k 
but greater than or equal to k characters, then reverse the first k characters 
and left the other as original.

 1- take first 2k characters from the string
 2- reverse first k (using slicing [::-1])
 3- add this reversed part with the second half of the considered part (2k characters)
 4- call the function again with the remaining string
 5- add the result of this call to your answer

"""


def reverseStr(s,k):
    if len(s) < k : return s[::-1]    
    if len(s) < 2*k : return s[:k][::-1] +s[k:]
    return s[:k][::-1]+s[k:2*k] + reverseStr(s[2*k:],k)

    
    



    
if __name__=='__main__':
    s = "abcdefg"
    k = 2
    print(reverseStr(s,k))  #output: "bacdfeg"

    s = "abcdefg"
    k = 3
    print(reverseStr(s,k)) #output: cbadefg

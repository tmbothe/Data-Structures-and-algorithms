def lengthOfLongestSubstring(s):
        start =0
        maxlen=0
        #s= list(s)
        #print(s)
        if len(s)<=1:
            return len(s)
        for i in range(0,len(s)):
            current=s[start:i+1]
            #print(f"start={start} and i={i}")
            #print(set(current))
            if len(set(current))==len(current):
                #print('here')
                maxlen=max(maxlen,len(current))
            else:
                start+=1
        return maxlen



if __name__=='__main__':
     s = "abcabcbb"
     print(lengthOfLongestSubstring(s))
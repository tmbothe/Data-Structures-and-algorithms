def removeDuplicates(s, k):

    i=1
    n=len(s)
    
    while i < n:
        
        

        if s[i]==s[i-1]:
            start=i-1
            count=1

            while (count<=k) and (i<n+1) and (s[i-1]==s[i]):
                count+=1
                #print(f'Current letter : {s[i]}. i={i},Current count : {count}')
                if count==k:
                    break
                i+=1
            #print(f'before changing s: {s}, count : {count} i: {i}, start: {start}')
            if k==count:
                s=s[:start]+s[i+1:]
                n=len(s)
                i=1
            #print(f'After changing s: {s}')
            if len(s)<k:
                return s
        else:
            i+=1
    return s
            

def removeDuplicates2(s, k):

    stack = []
    
    for letter in s:
        if stack and stack[-1][0]==letter:
            stack[-1][1]+=1
        else:
            stack.append([letter,1])

        if stack[-1][1]==k:
            stack.pop()

    output =''
    for element in stack:
        output+=element[0]*element[1]
    return output



if __name__ == '__main__':

    s = "deeedbbcccbdaa"
    k = 3
    #Output: "aa"
    print(removeDuplicates(s, k))

    print('With Stack')

    print(removeDuplicates2(s, k))
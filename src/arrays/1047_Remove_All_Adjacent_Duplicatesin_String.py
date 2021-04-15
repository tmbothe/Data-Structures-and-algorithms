
def removeDuplicates(S):

    stack =[]

    for letter in S:
        if stack and stack[-1][0]==letter:
            stack[-1][1]+=1
        else:
            stack.append([letter,1])

        if stack[-1][1]>1:
            stack.pop()

    output=''

    for element in stack:
        output+= element[0]*element[1]

    return output


if __name__ =='__main__':

    S=  "abbaca"
    #Output: "ca"
    print(removeDuplicates(S))

    


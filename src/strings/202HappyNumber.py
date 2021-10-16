def isHappy(n):

    if len(str(n))==1 and n==1:
        return True
    
    seen=set()    
    while n!=1:
        num = str(n)
        n=0
        for i in range(len(num)):
            n +=int(num[i])**2
        if n not in seen:
            seen.add(n)
        else:
            return False
    return True







if __name__=='__main__':
    n= 19
    print(isHappy(n))

    n = 2
    print(isHappy(n))
    #Output: false
    n = 7
    print(isHappy(n))
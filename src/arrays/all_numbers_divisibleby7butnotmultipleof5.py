def divisibleby7notmultipleof5(start,end):
    
    result=[]
    for num in range(start,end):
        if num%7==0 and num%5!=0:
            result.append(num)

    return result



if __name__=='__main__':
    print(divisibleby7notmultipleof5(2000, 3201))
def isHappy(n):
   mem = set()
   while n!=1:
       n = sum([int(i)**2 for i in str(n)])
       if n in mem:
           return False
       else:
            mem.add(n)
   print(mem)
   return True
        


if  __name__=='__main__':
    n = 19
    print(isHappy(n))

            
         


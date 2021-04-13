def is_prime(n):
    
    for i in range(2,n//2):
        if n%i==0:
            return False
        return True

def check_primes(start,end):
    result=[]
    for i in range(start,end+1):
        if is_prime(i):
            result.append(i)
    return result



if __name__=='__main__':
    print(check_primes(100,200))

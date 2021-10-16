'''
Given a list of ints, balance the list so that each int appears equally in the list. Return a dictionary where the key is the int and the value is the count needed to balance the list.

[1, 1, 2] => {2: 1}
[1, 1, 1, 5, 3, 2, 2] => {5: 2, 3: 2, 2: 1}

'''
from collections import defaultdict
def balanceint(nums):
    
    numsdict=defaultdict(int)
    
    result = defaultdict(int)
    for num in nums:
        numsdict[num]+=1
    
    maxcount = max(numsdict.values())
    
    for num in numsdict:
        if numsdict[num]!=maxcount:
            result[num] =maxcount-numsdict[num]
    return result
    
    
    
    
    
    
if __name__=='__main__':
    nums = [1, 1, 2] #=> {2: 1}
    print(balanceint(nums))
    nums = [1, 1, 1, 5, 3, 2, 2] #=> {5: 2, 3: 2, 2: 1}
    print(balanceint(nums))
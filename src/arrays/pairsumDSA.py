"""
Given an array A[] and a number x, check for pair in A[] with sum as x
"""
from collections import defaultdict
    
def pairsum(nums, target):
    
    if len(nums)<2:
        return None
    seen = set()
    
    for num in nums:
        if target-num in seen:
            return [target-num,num]
        else:
            seen.add(num)
    return 'No valid pair exists'
    
    
def sortedPairsum(nums,target):
    
    if len(nums)<2:
        return
    start,end = 0,len(nums)-1
    
    nums.sort()
    print(nums, end)
    while start< end:
        print(f'start={start} end={end} current={nums[start]}+{nums[end]}')
        current = nums[start]+nums[end]
        if start<end and current == target:
            return (nums[start],nums[end])
        elif start<end and current>target:
            end-=1
        elif start<end and  current<target:
            start+=1
    return 'No such pair exists'
    
  
if __name__=='__main__':
    arr = [0, -1, 2, -3, 1]
    #sum = -2
    #Output: -3, 1
    print( pairsum(arr,-2))
    
    arr= [1, -2, 1, 0, 5]
    sum = 0
    
    print(pairsum(arr,sum))
    
    arr = [1, 4, 45, 6, 10, -8] 
    sum = 16
    print(pairsum(arr,sum))
    
    print('=========Evaluating two pointers techniques=============')
    
    arr = [0, -1, 2, -3, 1]
    print( sortedPairsum(arr,-2))
    
    arr= [1, -2, 1, 0, 5]
    sum = 0
    
    print(sortedPairsum(arr,sum))
    
    arr = [1, 4, 45, 6, 10, -8] 
    sum = 16
    print(sortedPairsum(arr,sum))
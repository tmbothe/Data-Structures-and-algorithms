"""
Given an array of integers, find if the array contains any duplicates.
Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.
"""

def containsDuplicate(nums):
    
    n= len(nums)
    
    if n < 2:
        return False
    
    numberCount = {}
    
    for i in range (n):
        if nums[i] in numberCount:
            numberCount[nums[i]]+=1
        else:
            numberCount[nums[i]]=1
            
    for num in numberCount:
        if numberCount[num] >1:
            return True
    return False


if __name__=='__main__':

    nums = [1,2,3,1]  #Output: true
    print(containsDuplicate(nums))

    nums = [1,2,3,4] #Output: false
    print(containsDuplicate(nums))

    nums = [1,1,1,3,3,4,3,2,4,2] #Output: true
    print(containsDuplicate(nums))
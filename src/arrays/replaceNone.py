def replaceNone(nums):
    """replace None in the List with previous value"""
    if len(nums)<2:
        return
    
    previous = nums[0]
    
    for i in range(1,len(nums)):
        if nums[i] is None:
            nums[i]=previous
        else:
            previous=nums[i]
            
    return nums
    








if __name__=='__main__':
    nums = [None, None, 1, 2, None, None, 3, 4, None, 5, None, None]
    print(replaceNone(nums))
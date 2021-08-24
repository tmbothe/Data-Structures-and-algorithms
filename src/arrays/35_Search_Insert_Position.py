def searchInsert(nums,target):

    pass

def binarysearch(nums,low,high,target):

    if low==high:
        return None

    while low <= high:
        mid = (low+high)//2
        #print(mid)
        

        if nums[mid] == target:
            return mid
        if nums[mid-1] < target and  nums[mid+1] >target:
            return mid
        elif nums[mid]>target:
            high = mid-1
        elif nums[mid]<target:
            low = mid+1
        
        #print(f'low = {low}, high={high} and mid = {mid}, value mid = {nums[mid]}')




if  __name__ =='__main__':
    nums = [1,3,5,6]
    target = 5
    #Output: 2
    print(binarysearch(nums,0,len(nums),target))
    nums = [1,3,5,6]
    target = 2
    print(binarysearch(nums,0,len(nums),target))
    #Output: 1
    nums = [1,3,5,6]
    target = 7
    #Output: 4
    print(binarysearch(nums,0,len(nums),target))

    nums = [1,3,5,6]
    target = 0
    #Output: 0
    #print(binarysearch(nums,0,len(nums),target))

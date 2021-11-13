def searchInsert(nums, target):

    pass


def binarysearch(nums, low, high, target):
    low = 0
    if low == high:
        return None

    while low <= high:
        mid = low+(-low+high)//2
        print(f'mid== {mid}, value ={nums[mid]}')
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            high = mid-1
        elif nums[mid] < target:
            low = mid+1
    return low

    #print(f'low = {low}, high={high} and mid = {mid}, value mid = {nums[mid]}')


def searchInsert(nums, target):
    low, high = 0, len(nums)

    while low < high:
        mid = (low+high)//2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid+1
        else:
            high = mid-1
    return low


if __name__ == '__main__':
    nums = [1, 3, 5, 6]
    target = 5
    #Output: 2
    #print(binarysearch(nums, 0, len(nums), target))
    nums = [1, 3, 5, 6]
    target = 2
    # print(binarysearch(nums,0,len(nums),target))
    #Output: 1
    nums = [1, 3, 5, 6]
    target = 7
    #Output: 4
    # print(binarysearch(nums,0,len(nums)-1,target))

    nums = [1, 3, 5, 6]
    target = 0
    #Output: 0
    # print(binarysearch(nums,0,len(nums),target))

    print("===============second===============")
    nums = [1, 3, 5, 6]
    target = 5
    #Output: 2
    print(searchInsert(nums, target))
    nums = [1, 3, 5, 6]
    target = 2
    print(searchInsert(nums, target))
    #Output: 1
    nums = [1, 3, 5, 6]
    target = 7
    #Output: 4
    print(searchInsert(nums, target))

    nums = [1, 3, 5, 6]
    target = 0
    #Output: 0
    print(searchInsert(nums, target))


def sort_array(nums):
    n= len(nums)

    for i in range(n):
        for j in range(i+1,n):
            if nums[i]>nums[j]:
                nums[i],nums[j] = nums[j],nums[i]
    return nums


if __name__=='__main__':
    
    nums = [2, 1, 4, 3, 5]
    print(sort_array(nums))
def isMonotonic(nums):

    decreasing, increasing = 0, 0

    for i in range(1, len(nums)):
        if nums[i] == nums[i-1]:
            continue
        elif nums[i] < nums[i-1]:
            decreasing = 1
        else:
            increasing = 1
    if increasing == decreasing == 1:
        return False
    return True


if __name__ == '__main__':
    nums = [1, 2, 2, 3]
    print(isMonotonic(nums))
    #Output: true

    Input: nums = [6, 5, 4, 4]
    #Output: true
    print(isMonotonic(nums))

    nums = [1, 3, 2]
    #Output: false
    print(isMonotonic(nums))

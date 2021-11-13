def missingNumber(nums):

    n = len(nums)
    for i in range(n):
        if i < nums[i] and i < n:
            return i
        elif nums[i] == n-1:
            return i+1
        elif i > nums[i] and i < n:
            return i-1


if __name__ == '__main__':
    nums = [0, 1, 2, 6, 9]  # , n = 5, m = 10
    #Output: 3
    print(missingNumber(nums))

    nums = [4, 5, 10, 11]  # , n = 4, m = 12
    #Output: 0
    print(missingNumber(nums))
    nums = [0, 1, 2, 3]  # , n = 4, m = 5
    #Output: 4
    print(missingNumber(nums))
    nums = [0, 1, 2, 3, 4, 5, 6, 7, 10]  # , n = 9, m = 11
    #Output: 8
    print(missingNumber(nums))

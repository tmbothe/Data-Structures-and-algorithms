

def minSubArrayLen(target, nums):
    end, start, n = 0, 0, len(nums)

    total = 0
    minlen = float('inf')

    for end in range(n):
        total += nums[end]

        while total >= target:
            minlen = min(minlen, end-start+1)
            total -= nums[start]
            start += 1
    if minlen == float('inf'):
        return 0
    return minlen


if __name__ == '__main__':
    target = 7
    nums = [2, 3, 1, 2, 4, 3]
    print(minSubArrayLen(target, nums))
    #Output: 2
    target = 4
    nums = [1, 4, 4]
    print(minSubArrayLen(target, nums))
    #Output: 1

    target = 11
    nums = [1, 1, 1, 1, 1, 1, 1, 1]
    print(minSubArrayLen(target, nums))
    #Output: 0

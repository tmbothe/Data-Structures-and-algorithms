def maxSubArrayLen(nums, k):
    n = len(nums)
    seen = {}

    maxlen = -float('inf')
    total = 0
    for end in range(n):
        total += nums[end]

        if total == k:
            maxlen = end+1
        if total-k in seen:
            maxlen = max(maxlen, end-seen[total-k])
        if total not in seen:
            seen[total] = end

    if maxlen == -float('inf'):
        return 0
    return maxlen


if __name__ == '__main__':
    nums = [1, -1, 5, -2, 3]
    k = 3
    #Output: 4
    # Explanation: The subarray [1, -1, 5, -2] sums to 3 and is the longest.
    print(maxSubArrayLen(nums, k))
    nums = [-2, -1, 2, 1]
    k = 1
    #Output: 2
    print(maxSubArrayLen(nums, k))

    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    k = 6
    print(maxSubArrayLen(nums, k))

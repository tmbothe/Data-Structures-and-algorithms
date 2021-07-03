def maximumSum(arr, k):
    n = len(arr)

    if k > n:
        return
    maxSum = sum(arr[:k])

    for i in range(n-k):
        current = maxSum - arr[i] + arr[i+k]
        maxSum = max(current, maxSum)
    return maxSum


if __name__ == '__main__':
    arr = [80, -50, 90, 100]
    k = 2
    print(maximumSum(arr, k))

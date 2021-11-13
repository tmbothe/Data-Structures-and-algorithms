def productArray(nums, n):

    right = [0]*n
    left = [0]*n

    left[0] = 1
    right[n-1] = 1

    prod = [0]*n
    for i in range(1, n):
        left[i] = left[i-1]*nums[i-1]
    for i in range(n-2, -1, -1):
        right[i] = right[i+1]*arr[i+1]

    for i in range(n):
        prod[i] = left[i]*right[i]

    return prod


if __name__ == '__main__':
    arr = [10, 3, 5, 6, 2]
    n = len(arr)
    print("The product array is: n")
    print(productArray(arr, n))
    # 180 600 360 300 900

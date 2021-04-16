def reverseArray(arr):

    n = len(arr)
    if n == 0:
        return arr
    n = n-1
    i = 0

    while i <= n:
        arr[i], arr[n] = arr[n], arr[i]

        i += 1
        n -= 1

    return arr


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5]
    # then the output is [5,4,3,2,1]
    print(reverseArray(arr))

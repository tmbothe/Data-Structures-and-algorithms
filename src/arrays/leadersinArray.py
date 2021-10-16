def leadersInArray(arr):

    max_right = arr[-1]
    result=[max_right]

    for i in range(len(arr)-2,-1,-1):
        if arr[i]>max_right:
            result.append(arr[i])
            max_right=arr[i]

    return result







if __name__ =='__main__':
    arr = [16, 17, 4, 3, 5, 2]
    #leaders are 17, 5 and 2.]
    print(leadersInArray(arr))
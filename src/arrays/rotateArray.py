

def rotateArray(nums):
    end   = len(nums)-1
    start = 0 
    #print(nums)
    while start <= end :
        nums[start],nums[end] = nums[end],nums[start]
        start+=1
        end -=1
    return nums

def rotate_element(nums,d):
    A = rotateArray(nums[:d+1])
    B = rotateArray(nums[d+1:])
    return rotateArray(A+B)


def rototate_array2(nums,k):
    """
     This is an alternative solution using and extra array and recopying everything at the end.
     We use the modulo to move element to the end
    """

    n = len(nums)
    temp = [0] * n
    for i in range(n):
        temp[ (i+k)%n] = nums[i]
    nums[:] = temp
    return nums




if __name__ == '__main__':
    
    nums= [1, 2, 3, 4, 5, 6, 7] 
    print(rotate_element(nums,3))

    print(rototate_array2(nums,3))
def min_sub_array_length(nums,sum):
    min_length = float("inf")
    #print(min_length)

    for start_idx in range(len(nums)):
        subarray_sum = 0
        for end_idx in range(start_idx,len(nums)):
            subarray_sum+=nums[end_idx]
            if subarray_sum>=sum:
                min_length=min(min_length,(end_idx-start_idx+1))

    return min_length if min_length !=float('inf') else min_length


def opt_min_sub_array_length(nums,sum):
    min_length = float("inf")

    start_idx = end_idx = 0
    n= len(nums)
    i=0

    while i<n:
        start_idx = i
        current_sum=0
        current =[]

        while i<n and current_sum<sum:
            current_sum +=nums[i]
            current.append(nums[i])
            i+=1

        min_length = min(min_length,i-start_idx+1)
        print(f'i value is {i}')
        print(current)
        i += 1

    return min_length if min_length !=float('inf') else min_length


def minb_sub_array_length(nums, sum):
    min_length = float("inf")
    for start_idx in range(len(nums)):
        subarray_sum = 0
        for end_idx in range(start_idx, len(nums)):
            subarray_sum += nums[end_idx]
            if subarray_sum >= sum:
                min_length = min(min_length, end_idx - start_idx + 1)
                continue
        print(f'Current start {start_idx}. current end {end_idx}')
        print(f'sum is {subarray_sum}')
        print(f'minimum is {min_length}')
       
    return min_length if min_length != float("inf") else 0


def mintwo_sub_array_length(nums, sum):

    start_idx  = 0
    min_length = float("inf")
    sum_array  = 0

    for end_idx in range(len(nums)):
        sum_array+=nums[end_idx]
        while sum_array >= sum:
            min_length = min(min_length,(end_idx-start_idx+1))
            sum_array -= nums[start_idx]
            start_idx +=1
            print(f'In loop Current start {start_idx}. current end {end_idx}')
            print(f'In loop sum is {sum_array}')
            print(f'In Lopp minimum is {min_length}')
            

        print(f'Current start {start_idx}. current end {end_idx}')
        print(f'sum is {sum_array}')
        print(f'minimum is {min_length}')

    return min_length if min_length != float("inf") else 0


        







if __name__ == '__main__':
    #print(min_sub_array_length([2,3,1,2,4,3], 7))
    #print(opt_min_sub_array_length([2,3,1,2,4,3], 7))
    #print(minb_sub_array_length([2,3,1,2,4,3], 7))
    print(mintwo_sub_array_length([2,3,1,2,4,3], 7))


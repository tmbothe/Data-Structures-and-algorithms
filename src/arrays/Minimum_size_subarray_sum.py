'''
Given an array of n positive integers and a positive integer s, find the minimal 
length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.
min_sub_array_length([2,3,1,2,4,3], 7)
result = 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.
'''

# Solution 1 ==> Brute force

def min_sub_array_length_brute(nums, target):
    min_length = float("inf")
    
    for start_idx in range(len(nums)):
        for end_index in range(len(nums)):
            currentsum = get_sum(nums,start_idx,end_index)
            if currentsum>=target:
                min_length=min(min_length,end_index-start_idx+1)
    return min_length if min_length != float("inf") else 0

def get_sum(nums,start_index,end_index):
    result =0
    for i in range(start_index,end_index+1):
        result+=nums[i]
    return result


def min_sub_array_length(nums,target):
    min_length = float("inf")

    for start_idx in range(len(nums)):
        current_sum=0
        for end_idx in range(start_idx,len(nums)):
            current_sum +=nums[end_idx]
            if current_sum >= target:
                min_length=min(min_length,end_idx-start_idx+1)
                continue
    return min_length if min_length != float("inf") else 0


def min_sub_array_length_two_pointer(nums,target):
    min_length = float("inf")

    current_sum=0
    start_idx=0
    for end_idx in range(len(nums)):
        current_sum+=nums[end_idx]
        while current_sum>=target:
            min_length=min(min_length,end_idx-start_idx+1)
            current_sum-=nums[start_idx]
            start_idx+=1
    return min_length if min_length != float("inf") else 0

if __name__=='__main__':
    nums = [2,3,1,2,4,3]
    target = 7

    print(min_sub_array_length_brute(nums, target))

    print(min_sub_array_length(nums, target))
    print(min_sub_array_length_two_pointer(nums,target))
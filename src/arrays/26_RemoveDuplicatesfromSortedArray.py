"""
  Given a sorted array nums, remove the duplicates in-place such that each element appears only once and returns the new length.
  Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory

  https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/727/

  For this problem, we define two pointers: a slow pointer that keeps the count of different (non duplicates) values
  and a fast pointer that iterate thoughout the array. Whenever we see a different value, we update its place in the
  array. at the end, the size of the slow pointer is the size of the final array
"""


def removeDuplicates(nums):
    if len(nums)<=1:
        return nums
    
    i=0
    n=len(nums)
    #print(nums)

    for j in range(1,n):
        #print(f'Here is the value of i={i} and j={j}')
        #print(f'The current array is nums = {nums}')
        if nums[i] != nums[j]:
            i+=1
            nums[i]=nums[j]
    print(i)
    return nums[:i+1]
        


if __name__=='__main__':
    nums = [1,1,2]
    print(removeDuplicates(nums))

    nums = [0,0,1,1,1,2,2,3,3,4]

    print(removeDuplicates(nums))




    

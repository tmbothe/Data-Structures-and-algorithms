"""
Given a non-empty array of decimal digits representing a non-negative integer, increment one to the integer.
The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.
You may assume the integer does not contain any leading zero, except the number 0 itself.
"""

def plusOne(digits):

    n = len(digits)
    
    for i in range(n):
        idx = n-1-i
        # if digits is 9 replace all with 0
        if digits[idx]==9:
            digits[idx]=0
        else:
            #if right number is not 9, add 1 and exit
            digits[idx]+=1
            return digits
    #if all numbers are 9 add one at the beginning
    return [1] + digits


if __name__ =='__main__':
    digits = [1,2,3] #Output: [1,2,4]
    print(plusOne(digits))
  
    digits = [4,3,2,1] #Output: [4,3,2,2]
    print(plusOne(digits))
    
    digits = [0]  #Output: [1]
    print(plusOne(digits))
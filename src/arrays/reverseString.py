"""
Write a function that reverses a string. The input string is given as an array of characters char[].
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
You may assume all the characters consist of printable ascii characters.
"""
from nose.tools import assert_equal

def reverseString(arr):
    n = len(arr)

    #checking if the len of the array is null or less than 2
    if n < 2:
        return arr

    i = 0

    while i < n-1:
        arr[i], arr[n-1] = arr[n-1],arr[i]
        i+=1
        n-=1

    return arr


class ReverseStringTest(object):
    def test(self, sol):
        assert_equal(sol(["h","e","l","l","o"]), ["o","l","l","e","h"])
        assert_equal(sol( ["H","a","n","n","a","h"]), ["h","a","n","n","a","H"])
  
        print('ALL TEST CASES PASSED')


if __name__== '__main__':

    t = ReverseStringTest()
    t.test(reverseString)


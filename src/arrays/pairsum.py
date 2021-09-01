"""
RUN THIS CELL TO TEST YOUR SOLUTION
"""
from nose.tools import assert_equal

def pair_sum(arr,k):

    if len(arr)<2:
        return False

    result = set()
    seen = set()

    for num in arr:
        if k-num in seen:
            result.add((num,k-num))
        elif num not in seen:
            seen.add(num)
    print(result)
    return len(result)

print(pair_sum([1,3,2,2],4))





def pairsum2(arr,target):
    seen = set()

    result=[]

    for num in arr:
        if num not in seen:
            seen.add(num)
        if target-num in seen:
            result.append((target-num,num))
    return result
            



"""
RUN THIS CELL TO TEST YOUR SOLUTION
"""
from nose.tools import assert_equal

class TestPair(object):
    
    def test(self,sol):
        assert_equal(sol([1,9,2,8,3,7,4,6,5,5,13,14,11,13,-1],10),6)
        assert_equal(sol([1,2,3,1],3),1)
        assert_equal(sol([1,3,2,2],4),2)
        print ('ALL TEST CASES PASSED')
        
#Run tests
t = TestPair()
t.test(pair_sum)


arr = [0, -1, 2, -3, 1]
target = -2

print(pairsum2(arr,target))

arr = [1, -2, 1, 0, 5]
target = 0

print(pairsum2(arr,target))

arr = [1, 4, 45, 6, 10, -8]
target = 16
print(pairsum2(arr,target))
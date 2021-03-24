from nose.tools import assert_equal

def anagram(s1,s2):
    
    s1= s1.lower().replace(" ","")
    s2= s2.lower().replace(" ","")

    if len(s1)==0 or len(s2) ==0:
        return False
    elif len(s1) != len(s2):
        return False

    result={}
    for letter in s1:
        if letter in result:
            result[letter]+=1
        else:
            result[letter]=1

    for letter in s2:
        if letter in result:
            result[letter]-=1
        else:
            result[letter]=1

    for letter in result:
        if result[letter] !=0:
            return False
    return True
        

class AnagramTest(object):
    
    def test(self,sol):
        assert_equal(sol('go go go','gggooo'),True)
        assert_equal(sol('abc','cba'),True)
        assert_equal(sol('hi man','hi     man'),True)
        assert_equal(sol('aabbcc','aabbc'),False)
        assert_equal(sol('123','1 2'),False)
        print("ALL TEST CASES PASSED")

# Run Tests
t = AnagramTest()
t.test(anagram)
from typing import List

def validateStackSequences(pushed: List[int], popped: List[int]) -> bool:
    """
      Given two sequences pushed and popped with distinct values, return true if and only if this could have been 
      the result of a sequence of push and pop operations on an initially empty stack.
    """

    i = 0
    stack = []

    for num in pushed:
        stack.append(num)
        while stack and i < len(popped) and stack[-1]==popped[i]:
            stack.pop()
            i+=1
    return i == len(popped)











if __name__ =='__main__':
    pushed = [1,2,3,4,5]
    popped = [4,5,3,2,1]  #Output: true
    print(validateStackSequences(pushed,popped))


    pushed = [1,2,3,4,5]
    popped = [4,3,5,1,2]
    print(validateStackSequences(pushed,popped))





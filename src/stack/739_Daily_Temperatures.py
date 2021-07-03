def dailyTemperatures(temperatures):
    if not temperatures:
        return []
    result = [0]*len(temperatures)

    s = [(0, temperatures[0])]

    for i, temp in enumerate(temperatures[1:]):
        # print(s)
        print(result)
        while s and s[-1][1] < temp:
            low = s[-1][0]
            diff = i-low
            result[low] = diff
            s.pop()
        s.append((i, temp))

    return result


if __name__ == '__main__':
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    #Output: [1,1,4,2,1,1,0,0]
    print(dailyTemperatures(temperatures))

    """
    def dailyTemperatures(self, temperatures):
        answer = [0 for _ in temperatures]
        stack = [(0, temperatures[0])]
        for i, t in enumerate(temperatures):
            while stack and stack[-1][1] < t:
                low_i = stack[-1][0]
                answer[low_i] = i - low_i
                stack.pop()
            stack.append((i,t))

        return answer
    """

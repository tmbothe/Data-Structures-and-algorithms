def dailyTemperatures(temperatures):
    i, j = 0, 0

    result = [0]*len(temperatures)

    n = len(temperatures)
    for i in range(len(temperatures)):
        j = i+1
        while j < n:
            if temperatures[j] > temperatures[i]:
                result[i] = j-i
                break
            j += 1

    return result


if __name__ == '__main__':
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    #Output: [1,1,4,2,1,1,0,0]
    print(dailyTemperatures(temperatures))

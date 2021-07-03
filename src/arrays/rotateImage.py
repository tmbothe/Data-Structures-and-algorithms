
def rotatingArray(matix):
    n = len(matix)
    result = []
    for i in range(n):
        result.append([])
        for j in range(n-1, -1, -1):
            result[i].append(matix[j][i])
    return result


if __name__ == '__main__':
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]
    print(rotatingArray(matrix))

    #Output: [[7,4,1],[8,5,2],[9,6,3]]

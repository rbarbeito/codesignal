def solution(inputArray):
    product = inputArray[0]*inputArray[1]
    for i in range(1, len(inputArray)-1):

        if inputArray[i]*inputArray[i+1] > product:
            product = inputArray[i]*inputArray[i+1]

    return (product)


print(solution([3, 6, -2, -5, 7, 3]))

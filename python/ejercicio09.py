def solution(inputArray):
    outputArray = []
    mayor = 0

    for i in inputArray:
        if len(i) > mayor:
            mayor = len(i)

    if len(inputArray) == 1:
        outputArray.append(i)
        return outputArray
    for i in inputArray:
        if len(i) == mayor:
            outputArray.append(i)

    return outputArray

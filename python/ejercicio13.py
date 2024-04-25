def solution(inputString):
    inicial = 0
    final = 0
    count = inputString.count("(")

    while count != 0:
        for i in range(len(inputString)):
            if inputString[i] == "(":
                inicial = i
                continue
            if inputString[i] == ")":
                final = i
                break

        nueva = inputString[inicial+1:final][::-1]

        inputString = inputString[:inicial]+nueva+inputString[final+1:]
        count -= 1

    return inputString

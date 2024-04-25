def solution(inputString):
    count = 0
    for i in range(len(inputString)):
        if inputString[i] != inputString[len(inputString)-i-1]:
            count += 1
            break

    return (count == 0)


print(solution("aavaa"))

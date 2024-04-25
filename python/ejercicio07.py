def solution(secuencia):
    contador = 0
    index = -1

    for i in range(1, len(secuencia)):
        if secuencia[i] <= secuencia[i - 1]:
            contador += 1
            index = i

    if contador == 0:
        return True
    elif contador == 1:

        if index == 1 or index == len(secuencia) - 1 or secuencia[index - 2] < secuencia[index] or secuencia[index - 1] < secuencia[index + 1]:
            return True

    return False

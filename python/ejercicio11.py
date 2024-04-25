def solution(n):
    numero = str(n)
    inicio = 0
    final = 0
    for i in range(len(numero)//2):
       inicio += int(numero[i])
       final += int(numero[len(numero)-i-1])

    return inicio == final

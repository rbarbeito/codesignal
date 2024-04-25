def solution(a):
    numero=0
    suma_inicial=0

    for i in a:
        sum=0
        for j in range(len(a)):
            sum+=abs(a[j]-i)
        
        if suma_inicial==0 or sum<suma_inicial:
            numero=i
            suma_inicial=sum

    return numero
    


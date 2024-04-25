def solution(a):

    for i in range(len(a)-1):
        if a[i] == -1:
            continue
        for j in range(i+1, len(a)):
            if a[j] == -1:
                continue

            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]

    return a

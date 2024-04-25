def solution(statues):
    statues.sort()
    count = 0

    for i in range(statues[0], statues[len(statues)-1]):
        if i not in statues:
            statues.insert(statues.index(i-1)+1, i)
            count += 1

    return count

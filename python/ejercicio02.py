def solution(year):
    resp = year//100 + 1
    if year % 100 == 0:
        resp -= 1
    return resp


print(solution(1905))

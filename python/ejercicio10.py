def solution(s1, s2):
    counter_s1 = {}
    counter_s2 = {}

    for letter in s1:
        counter_s1[letter] = counter_s1.get(letter, 0)+1

    for letter in s2:
        counter_s2[letter] = counter_s2.get(letter, 0)+1

    new = 0
    for x in counter_s1:
        if x in counter_s2:
           diff = min(counter_s1[x], counter_s2[x])
           new += diff

    return new

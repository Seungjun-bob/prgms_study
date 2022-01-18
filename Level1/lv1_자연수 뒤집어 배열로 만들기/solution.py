def solution(n):
    temp = list(str(n))
    temp = temp[::-1]
    return list(map(int, temp))
def solution(n):
    temp = list(map(int, str(n)))
    result = 0
    for i in temp:
        result += i
    return result
def solution(d, budget):
    d = sorted(d)
    answer = 0
    k = 0
    for i in d:
        k += i

        if k <= budget:
            answer += 1
            pass
        else:
            break
    return answer
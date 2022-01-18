def solution(n):
    n_list = list(map(str,str(n)))
    answer = sorted(n_list,reverse=True)
    return int(''.join(answer))
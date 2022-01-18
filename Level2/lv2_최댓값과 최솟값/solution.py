def solution(s):
    tmp = list(s.split(" "))
    tmp = list(map(int, tmp))
    return "".join(str(min(tmp))+" "+str(max(tmp)))
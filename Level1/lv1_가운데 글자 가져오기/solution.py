def solution(s):
    s= list(s)
    if len(s)%2 == 0:
        return ''.join(s[len(s)//2-1:len(s)//2+1])
    else:
        return s[len(s)//2]
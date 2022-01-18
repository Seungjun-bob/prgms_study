def solution(s):
    s = sorted(s.lower(),reverse=True)
    y_num = 0
    p_num = 0
    for i in range(len(s)):
        if s[i] == "y":
            y_num += 1
        if s[i] == "p":
            p_num += 1
    if y_num == 0 and p_num == 0:
        return True
    elif y_num == p_num :
        return True
    else:
        return False
        
    return s
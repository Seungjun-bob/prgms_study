def solution(s):
    s = s.split(" ")
    All = []
    for i in s:
        each = []
        for j in range(len(i)):
            
            if j%2==0:
                each.append(i[j].upper())
            else:
                each.append(i[j].lower())
        each = ''.join(each)
        All.append(each)
    answer = ' '.join(All)
    return answer
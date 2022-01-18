def solution(x):
    num = str(x)
    result = []
    sumnum = 0
    for i in num:
        result.append(i)
    for i in result:
        sumnum += int(i)
        
    if x%sumnum == 0:
        return True
    else:
        return False
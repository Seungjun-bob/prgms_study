def solution(seoul):
    for i in range(len(seoul)+1):
        if "Kim" == seoul[i]:
            return("김서방은 %d에 있다"%i)
    return seoul
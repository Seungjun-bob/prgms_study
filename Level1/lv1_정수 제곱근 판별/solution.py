import math
def solution(n):
    temp = math.sqrt(n)
    if temp == int(temp):
        return math.pow(int(temp)+1,2)
    else:
        return -1
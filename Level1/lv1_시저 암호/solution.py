def solution(s, n):
    a = 65
    answer = []
    for i in s:
        temp = int(ord(i)) + n
        
        if 65<= ord(i) <= 90: # 대문자 인경우
            if 90 < temp:
                answer.append(chr(temp-26))
            else:
                answer.append(chr(temp))
                
        if 96<= ord(i) <= 122: # 소문자인 경우
            if 122 < temp:
                answer.append(chr(temp-26))
            else:
                answer.append(chr(temp))
        if i == " ":
            answer.append(" ")      
        
            
    return ''.join(answer)
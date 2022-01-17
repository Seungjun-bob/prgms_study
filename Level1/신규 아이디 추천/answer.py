import re
def solution(new_id):
    # 소문자
    answer = new_id.lower()
    # 특수문자
    char = '~!@#$%^&*()=+[{]}:?,<>/'
    for i in char:
        if i in answer:
            answer = answer.replace(i,"")
    # 마침표
    answer = re.sub('\.\.+', '.', answer)
    # 4단계 : 양 끝 마침표 제거
    answer = re.sub('^\.|\.$', '', answer)
    # 5단계
    if answer == "":
        answer = "a"
    # 6단계
    answer = re.sub('\.$','',answer[0:15])
    # 7단계
    while len(answer) < 3:
         answer += answer[-1:]
    return answer
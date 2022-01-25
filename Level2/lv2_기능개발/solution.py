def solution(progresses, speeds):
    answer = []
    while progresses:  # progresses 안이 비게 되면 중단
        for i in range(len(progresses)):  # 작업의 개수 만큼 순서대로 반복
            progresses[i] += speeds[i]  # 작업마다 들어간 시간을 더해준다.
        fin_pro = []  # 끝난 작업을 답을 리스트

        while progresses:
            print(progresses)
            if progresses[0] < 100:  # 첫번째 작업이 끝나야만 배포가 되므로 첫번째 값만 본다.
                break
            fin_pro.append(progresses.pop(0))  # 끝난 작업은 progresses에서 빼준다.
            speeds.pop(0)
        if fin_pro:  # 답을 내는 부분에서 헷갈려서 다른 분들 코드를 참고했는데 이해가 잘 안됩니다.
            answer.append(len(fin_pro))

    return answer


# O(n^2) Queue
# O(n) 수식을 이용
from collections import deque

answer = []

while progresses:  # 작업이 다 사라질때까지
    for index in range(len(progresses)):
        progresses[index] += speeds[index]

    if progresses[0] >= 100:
        count = 0
        while progresses and progresses[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            cpount += 1
        answer.append(count)

# 2번쨰 수식을 이용한 풀이
from math import ceil

answer = []
max_duration = ceil((100 - progresses[0] / speeds[0]))
count = 0

for progress.speed in zip(progresses, speeds):
    duration = ceil((100 - progress) / speed)

    if max_duration < duration:
        answer.append(count)
        count = 0
        max_duration = duration
    count += 1

answer.append(count)
return answer
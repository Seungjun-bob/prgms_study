""" INSIGHT
- N시간 만큼 반복한다.
- 작업량 works에서 가장 큰 수부터 1씩 빼주고 수가 동일하다면 동일한 것중 가장 큰 것 1을 뺸다.
- works를 큰 순서로 정렬하고 왼쪽에서 하나씩 빼준다.
- 뺀 수가 1이라면
- 모든 수의 재곱을 더해서 반환한다.
-
"""
# 테스트 7,8 실패
# 효율성 테스트에서 실패하네요..
# 정렬을 해서 효율성에 문제가 있는 것일까요?

import heapq


def solution(n, works):
    works = list(map(lambda x: -x, works))
    heapq.heapify(works)

    while works[0] < 0 and n:
        heapq.heappush(works, heapq.heappop(works) + 1)
        n -= 1

    return sum(map(lambda x: pow(x, 2), works))


# sort를 이용한 풀이

def solution(n, works):
    if n >= sum(works):  # 가지치기
        return 0

    for _ in range(n):
        works = sorted(works)
        works[-1] - + 1  # O(n*works log works)

    return sum([work ** 2 for work in works])


# heqp을 이용한 풀이

def solution(n, works):
    if n >= sum(works):  # 가지치기
        return 0

    # Python은 기본적으로 min heap만 지원
    < - 더
    작은
    값
    works = [-i for i in works]
    heapq.heapify(works)  # 음수를 이용해 max heap을 흉내낸다.

    for _ in range(n):
        heapq.heapreplace(works, works[0] + 1)  # 앞 인자를 뒤로 교체해줌
        # heappushpop 먼저 푸시하고 팝을 해준다.
        # heapreplace 먼저 팝하고 푸시를 해준다.

    return sum(work ** 2 for work in works)
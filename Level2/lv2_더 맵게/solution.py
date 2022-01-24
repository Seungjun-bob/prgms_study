"""
인사이트
1. while 반복문 사용
2. scoville 정렬
3. 섞은 음식 계산
4. K 이상인지 확인
"""

import heapq


def solution(scoville, K):
    cnt = 0
    heapq.heapify(scoville)
    while scoville[0] < K:
        if len(scoville) == 1 and scoville[0] < K:
            return -1

        mix_scoville = heapq.heappop(scoville) + (heapq.heappop(scoville) * 2)
        heapq.heappush(scoville, mix_scoville)
        cnt += 1
    return cnt


# 매번 정렬이 필요하다 -> heap으로 푸는 문제

from heapq import heapift, heappush, heappop


def solution(scoville, K):
    heapify(scoville)
    count = 0

    while scoville[0] < K:
        try:
            heappush(scoville, heappop(scoville) + heappop(scoville) * 2)
        except IndexError:  # pop을 할 수 없으면 에러가 생긴다.
            return -1
        count += 1
    return count
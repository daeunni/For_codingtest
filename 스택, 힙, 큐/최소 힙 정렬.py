"""
힙 예제 (힙 정렬)
  - 주로 우선순위 큐(ex. 다익스트라)를 이용할 때 heapq로 구현한다
  - 파이썬에서는 <최소 힙 - Min heap > 만 구현하므로, 최대힙은 부호를 바꾸어 계산한다
"""

import heapq

def heapsort(array):
  h = []         # 적재할 힙
  result = []    # 정렬된 값

  # 모든 원소를 힙에 삽입 : heapq.heappush() 사용
  for value in array :
    heapq.heappush(h, value)

  # 힙에 삽입된 모든 원소를 차례대로 꺼내 result에 담기 : heapq.heappop() 사용
  for i in range(len(h)):
    result.append(heapq.heappop(h))

  return result
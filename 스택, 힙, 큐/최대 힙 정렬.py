"""
힙 예제 (최대 힙 - Max Heap 정렬)
  - 최대힙은 부호를 바꾸어 계산한다
"""

import heapq

def Maxheapsort(array):
  h = []
  result = []

  # 힙에 삽입
  for value in array:
    heapq.heappush(h, -value)     # 마이너스해서 삽입 (python은 최소힙만 지원하므로)

  # 힙에서 꺼내 담기
  for i in range(len(h)):
    result.append(-heapq.heappop(h))  # 다시 마이너스해서 부호 되돌려주기
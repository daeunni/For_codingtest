"""
Triangle
  - 리스트 내 3개의 요소를 골라, 3가지 조건을 만족하는지 확인하는 유형 
  - 정렬을 하면, 나머지 두개의 조건이 저절로 만족되므로, 하나의 조건만 체크하면 됨!
"""


def solution(A):
  result = 0 

  if len(A) < 3 : 
    return result 

  # 우선 정렬하면, 나머지 3개 조건을 만족하게 됨 
  A.sort()     # 오름차순 정렬

  for i in range(len(A)-2):
    if A[i] + A[i+1] > A[i+2] :   # 하나의 조건만 체크 !
      result = 1
      break

  return result

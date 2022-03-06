"""
 MaxProductOfThree
  - 리스트 내 원소 3개 곱의 최댓값 찾기 
  - sorting을 활용해 모든 경우의 수에 적용되는 <절대규칙>을 찾는 문제 !

"""

def solution(A):
  A.sort()         # 오름차순 정렬 
  return max(A[-1]*A[-2]*A[-3], A[0]*A[1]*A[-1])

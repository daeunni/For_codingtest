"""
Rotation Array
  - 오른쪽으로 K번 이동한 뒤 리스트 반환 

  1) 간단히 인덱싱으로 해결 
  2) 단, 꼭꼭 리스트가 비어있을 때 예외처리 해주기 !!!!!!!!!!!
"""

def solution(A, K):
    if len(A)==0:
      return A
    for _ in range(K):
        A = [A[-1]] + A[:len(A)-1]
    return A

solution([], 3)

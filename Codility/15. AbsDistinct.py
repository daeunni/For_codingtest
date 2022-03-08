"""
AbsDistinct
  - 리스트 내 고유한 절댓값 수 구하기 
  - 원소를 모두 제곱한 후 set의 len을 구한다 (단순하지만 효율도 좋음 )
"""

def solution(A):
    return len(set([x**2 for x in A]))    # unique한 제곱값 뽑기

"""
FrogJmp
  - 현재부터 도착지점까지 최소 점프수 반환
  - 몫, 나머지로 접근하되 예외처리를 잘 해주자 ! (나누어 떨어질 때와 나누어 떨어지지 않을 때)
"""

def solution(X, Y, D):
  if X==Y : 
    return 0 

  return (Y-X) // D if (Y-X) % D == 0 else (Y-X) // D + 1

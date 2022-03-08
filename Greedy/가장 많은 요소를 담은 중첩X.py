"""
MaxNonoverlappingSegments
  - 전형적인 그리디의 스케쥴링 문제 
  - 제일 첫 선분의 끝점을 기준점으로 잡고, 이 후 시작점이 기준점보다 크면 num + 1 후 끝점 업데이트 
"""


def solution(A, B):
    
    # 예외 1) 둘 중 하나 리스트가 비어있을 때 / 예외 2) 두 리스트 길이 다를 때 
    if len(A) == 0 or len(B) == 0 or len(A) != len(B) :
        return 0 

    end_point = B[0]
    num = 1    # 이미 start 선분은 하나 적재했다고 가정 

    for i in range(1, len(A)):

        if A[i] > end_point:
            num += 1
            end_point = B[i]   # end_point 업데이트 
    
    return num

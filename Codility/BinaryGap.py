"""
Binary Gap 
  : 정수를 이진수 표현으로 바꾸고, 1로 둘러싸인 연속적인 0부분 중 가장 길이가 긴 length 출력하기
  
1) 이진수 표현으로 바꾸기 > format(정수, 'b') 이용
2) 1 사이의 수만 가져와야하므로 맨 앞, 맨 뒤의 0은 버리기 > strip('0') 이용
3) 1 구분자로 쪼개서 가장 큰 length 구하기 > split('1') 이용
  
"""

def solution(N):
  return max( len(x) for x in format(N, 'b').strip('0').split('1'))


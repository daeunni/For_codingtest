"""
약수
  - 1과 자기자신을 제외한 "진짜 약수"의 개수 구하기 
"""
num = int(input())   # 진짜약수의 개수
real = list(map(int, input().split()))

print(min(real) * max(real))

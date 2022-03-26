"""
보물
  - 같은 인덱스끼리 곱해서 더한 값의 최솟값 출력하기 (A만 재배열 가능)
  - b의 작은 값은 a의 작은값과 곱해지도록 a를 b에 맞춰서 재배열하면 될 듯 
"""
import sys
# input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

new = [0 for _ in range(n)]
answer = 0 

b_idx = sorted(range(len(b)), key = lambda k: b[k])   # 인덱스 크기순 정렬 
a_new = sorted(a, reverse=True)    # 내림차순 정렬 

# a 정렬하기 
for i in range(n):
  new[b_idx[i]] = a_new[i]

for i in range(n):
  answer += new[i] * b[i]

print(answer)

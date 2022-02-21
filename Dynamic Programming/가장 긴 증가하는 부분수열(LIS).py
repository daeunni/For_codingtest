"""
가장 긴 증가하는 부분수열 (LIS)
  - DP의 대표적인 유형
"""

n = int(input())                        # 수열의 길이
arr = list(map(int, input().split()))   # 수열 = 리스트에 저장
d = [1 for _ in range(n)]               # dp 테이블 (i번째 원소를 마지막으로 하는 LIS의 길이) > 자기 자신의 LIS는 1이므로 1로 채우기!

for i in range(n):
  for j in range(i):
    if arr[i] > arr[j]:
      d[i] = max(d[i], d[j] + 1)     # dp 테이블 갱신

print(max(d))
"""
부분수열의 합 
  - N개의 수로 이루어진 수열에서 그 수열의 원소를 다 더한 값이 S가 되는 경우의 수를 구하기 
  - 백트래킹은 처음이라.. 
"""
import sys
input = sys.stdin.readline
# 얘네 위에 선언하면 아래 함수에서 자유롭게 사용할 수 있음!!
n, s = map(int, input().split())   
nums = list(map(int, input().split()))
result = 0 

def back(idx, sub_sum):
  global result

  # 백트래킹 재귀함수 탈출 조건 
  if idx >= n :
    return 

  sub_sum += nums[idx]
  if sub_sum == s : 
    result += 1

  # 1. 현재 nums[idx]를 선택한 경우 
  back(idx+1, sub_sum)

  # 2. 현재 nums[idx]를 선택하지 않은 경우 (다시 빼준다) 
  back(idx+1, sub_sum - nums[idx])

back(0, 0)
print(result)

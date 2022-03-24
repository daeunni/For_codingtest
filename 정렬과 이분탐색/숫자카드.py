"""
숫자 카드 
  - 숫자 카드를 상근이가 가지고 있는지 아닌지 반환 
  - find 문제이므로 이진탐색 이용하기 
"""
import sys
n = int(input())
cards = list(map(int, input().split()))
m = int(input())
have = list(map(int, input().split()))

# 이진탐색 이용하기 
cards.sort()      # 우선 오름차순 정렬 

def binary_search(start, end, target, array):
  if start > end : 
    return None
  mid = (start + end) // 2

  if array[mid] == target : 
    return mid 

  elif array[mid] > target : 
    end = mid - 1

  else : 
    start = mid + 1

  return binary_search(start, end, target, array)

for sang in have : 
  if binary_search(0, n-1, sang, cards) != None :
    print(1)    
  else:
    print(0)

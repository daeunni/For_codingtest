"""
수 찾기
  - 이진탐색 이용 
"""

# 이진탐색 : target 원소의 idx 찾기 
def binary_search(start, end, target, array):     # array : 정렬되어 있어야함 
  if start > end : 
    return None
  mid = (start + end) // 2
  
  if array[mid] == target : 
    return mid
  
  # mid 원소가 target 원소보다 작으면 > 오른쪽 큰 범위에서만 다시 탐색 
  elif array[mid] < target : 
    return binary_search(mid+1, end, target, array)
  
  # mid 원소가 target 원소보다 크면 > 왼쪽 작은 범위에서만 다시 탐색 
  else:
    return binary_search(start, mid-1, target, array)


n = int(input())
A = list(map(int, input().split()))   
m = int(input())
exist = list(map(int, input().split()))

A.sort()    # 우선 오름차순 정렬 

for i in exist : 
  if binary_search(0, n-1, i, A) == None : 
    print(0)
  else:
    print(1)

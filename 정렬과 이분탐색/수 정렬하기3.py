"""
수 정렬하기3 (메모리제한이 빡쎔. 8mb면 완전 빡쎈 수준인 것 같아!)
  - 모든 입력을 배열에 저장하면 메모리 초과가 난다! 
    > 모든 입력을 배열에 저장하지 않고 푸는 방법을 생각할 것 

  - checklist를 만들어서 이 인덱스에 적재한 후 그 인덱스를 반환하도록 
"""
import sys
n = int(sys.stdin.readline())
check = [0 for _ in range(10001)]    # 10000개까지밖에 존재하지 않으므로

# 모든 입력을 배열에 저장하면 메모리 초과가 난다! 
for _ in range(n):
  num = int(sys.stdin.readline())    # 이게 check 리스트의 인덱스
  check[num] += 1      # 해당 숫자 등장할 때마다 1을 더함 

for c in range(len(check)) : 
  if check[c] != 0 : 
    for j in range(check[c]):     # 적재된 해당 숫자만큼 반복 
      print(c)

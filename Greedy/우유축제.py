"""
[0, 1, 2] 3개씩 패턴이 반복되므로 3으로 나누었을 때의 나머지를 떠올려야 함
"""

N = int(input())     # # of milk store
stores = list(map(int, input().split()))    # store
max_num = 0      # max num of milk

# 0 : strawberry / 1 : choco  / 2 : banana

for i in range(N):
    if stores[i] == max_num % 3 :
        max_num += 1
print(max_num)






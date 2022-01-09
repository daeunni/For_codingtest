## 500, 100, 50, 10, 5, 1엔
## 개수가 가장 적게 거스름돈 반환

m = int(input())    # 지불할 돈
re = 1000 - m    # 거스름돈 금액
coin = [500, 100, 50, 10, 5, 1]
count = 0

for i in coin :
  count += re // i
  re %= i

print(count)
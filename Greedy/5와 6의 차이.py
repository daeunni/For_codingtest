a, b = map(str, input().split())    # 주어지는 두 수
min = 0 ; max = 0    # 리턴할 최대, 최솟값

## 아... 5가 있으면 무조건 작은거고 6이 있으면 무조건 큰거구나..

min = int(a.replace('6', '5')) + int(b.replace('6', '5'))
max = int(a.replace('5', '6')) + int(b.replace('5', '6'))

print(min, max)
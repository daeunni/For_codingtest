## 주어진 수를 M번 더해서 가장 큰 수를 만드는데 연속해서 K번까지 밖에 못더함
## > 가장 큰 수를 K번 더하고 두번째로 큰 수를 그 다음에 한번 더하고 이걸 반복한다 !!

n, m, k = map(int, input().split())
num = list(map(int, input().split()))     # N개의 자연수가 주어짐

count = 0
max_val = 0  # 반환할 최댓값
num.sort(reverse=True)  # 내림차순 정렬

while count < m:
    max_count = 0

    while max_count < k:
        max_val += num[0]  # 가장 큰 수
        max_count += 1
        count += 1

    max_val += num[1]  # 두번째로 큰 수
    count += 1

print(max_val)
# return function
def return_coin(input_coin):
    results = []
    coins = [25, 10, 5, 1]

    for i in coins:
        results.append(int(input_coin // i))
        input_coin %= i

    print(*results)  # 리스트 원소 모두 출력


T = int(input())  # 개수

for _ in range(T):
    return_coin(int(input()))




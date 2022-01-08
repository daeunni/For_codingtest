## input test case의 개수가 정해지지 않았기 때문에 while 문을 사용한다 
while True : 

  # input이 주어질 때 
  try : 
    a, b, c = map(int, input().split())    # 세 캥거루의 위치 
    result = max(b-a, c-b)    # 두 사이 중 가장 큰 값을 result에 할당 
    print(result - 1)

  # input이 주어지지 않을 때 
  except : 
    break
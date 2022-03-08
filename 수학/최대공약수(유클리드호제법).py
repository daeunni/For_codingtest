def solution(N, M):
    # write your code in Python 3.6
    
    a, b = N, M
    
    # 최대공약수(gcd)를 구하는 유클리드호제법 이용 
    while (b):
        a, b = b, a % b    # 계속 나머지를 구하다보면 언젠간 0이 나오는 시점이 있음. 그때 멈추기 
    
    # 최대공약수 
    gcd = a
    answer = N // gcd      # 최대공약수의 배수 구하기 
    return answer 

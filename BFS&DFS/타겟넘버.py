## 문제 및 설명 : https://daeun-computer-uneasy.tistory.com/69

## BFS

def solution(numbers, target):
  leaves = [0]          # 모든 계산 결과를 담자      
  count = 0 

  for num in numbers : 
    temp = []
	
    # 자손 노드 
    for leaf in leaves : 
      temp.append(leaf + num)    # 더하는 경우 
      temp.append(leaf - num)    # 빼는 경우 

    leaves = temp 

  # 모든 경우의 수 계산 후 target과 같은지 확인 
  for leaf in leaves : 
    if leaf == target : 
      count += 1

  return count


## DFS
def dfs(numbers, target, idx, values):     # idx : 깊이 / values : 더하고 뺄 특정 leaf 값 
	
    global cnt
    cnt = 0 
	
    # 깊이가 끝까지 닿았으면 
    if idx == len(numbers) & values == target : 
    	cnt += 1
        return 
  
    # 끝까지 탐색했는데 sum이 target과 다르다면 그냥 넘어간다
    elif idx == len(numbers) : 
    	return 
    
    # 재귀함수로 구현 
    dfs(numbers, target, idx+1, values + numbers[idx])   # 새로운 value 값 세팅   
    dfs(numbers, target, idx+1, values - numbers[idx])
 
 def solution(numbers, target) : 
 	
    global cnt
    dfs(numbers, target, 0, 0)
    
    return cnt

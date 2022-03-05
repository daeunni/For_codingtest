"""
FrogRiverOne
  - 주어진 X 길이 만큼 1~X까지 원소가 모두 등장했는지 확인해야하는 유형 
  
1) 어떻게 확인하지? > BFS 처럼 visited 리스트를 만들어 등장하면 0에서 1로 바꿔주는 방식 사용
2) visited가 모두 1로 바뀐 것 체크 
  > 처음에는 sum을 사용했고, 그 다음에는 모두 1은 check list를 만들어 같음을 확인했다. (첫 복잡도는 O(N^2), 두번째는 O(N))
    하지만 가장 깔끔한 방법은 check_sum 변수를 만들어 이게 X랑 같은지 비교하는 것 
3) 너무 예외처리를 주저리주저리 if로 하려고 하지 말자!

"""



def solution(X, A):
  visited = [0 for i in range(X)] 
  check_sum = 0 
  result = None

  for idx in range(len(A)):
    leaf = A[idx]

    # 아직 방문하지 않았으면 
    if visited[leaf-1] == 0 : 
      visited[leaf-1] = 1
      check_sum += 1
    
      # 음 근데 이렇게 되면 for문 반복마다 계속 sum을 해줘야하네 > 여기 수정해야할듯 
      if check_sum == X : 
        return idx

  return -1 

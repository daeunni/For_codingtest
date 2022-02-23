# For_codingtest
BAEKJOON problem by daeun✨        
[참고하면 도움이 되는 자잘한 tip들 ! ](https://github.com/daeunni/For_codingtest/blob/main/tips.md)

## 0. My goals
- [ ] 2월까지 백준 100문제 풀기 


## 1. Greedy 

- 현재 상황에서 가장 좋아보이는 것을 선택 

  > 문제에서 '가장 큰, 작은 순서대로' 라는 기준을 제시하는 경우가 많음 

- 그리디 해법이 정당한지 검토해야함 
  > ex) 거스름돈 문제는 동전의 큰 단위가 항상 작은 단위의 배수이므로, 작은 단위의 동전을 종합해 다른 해가 나올 수 없기 때문에 그리디가 성립 

- My solution

      - 몫과 나머지를 잘 이용하자 
      - 몫과 나머지로 반복되는 패턴을 찾아보자 ! 


## 2. Graph (BFS, DFS) 

- **단방향** 그래프 나타내기 : 2차원리스트로 node별 연결된 edge 연결리스트를 만든다 

- **BFS** : 큐(선입선출)를 이용하기 
  > 모든 edge의 weight가 **같을 때** 최단거리를 구하기 

- **DFS** : 스택(후입선출)을 이용하기 + **재귀함수** 이용 ! 

- My solution 

      - 상하좌우 이동 유형이 자주 출제됨 


## 3. Dynamic Programming 

- 큰 문제를 작은 문제로 나눌 수 있고, 작은 문제의 해답을 재탕할 수 있을 때 
- 하향식(Top-Down) : 큰 문제에서 작은 문제 ➡️ **재귀함수** 이용 (메모이제이션, memoization)
- 상향식(Bottom-Up) : 작은 문제에서 큰문제 ➡️ **반복문** 이용 (결과 저장용 DP 테이블 이용) 

  > DP 문제인지 아는게 중요함 ! 중복여부를 확인하자 !



## 4. Shortest path

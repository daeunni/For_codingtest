"""
적록색약
  - 음료수 얼려먹기 문제와 비슷하게 상하좌우 dfs로 접근
  - 음료수 얼려먹기 문제는 1의 영역만 파악했다면, 이 유형은 R, G, B의 유형을 각각 파악해야함 >> 색별로 영역 count 해주기
  - 색맹인 사람과 아닌사람의 값을 구분해서 출력해줘야 했음
"""

n = int(input())
picture = []
count = []

for i in range(n):
  picture.append(list(map(str, input())))


def dfs(x,y,color):
    if x < 0 or  x > n-1 or y < 0 or y > n-1:
        return False

    ## 색깔별로 count
    if picture[x][y] == color:

        ## 체킹을 다르게 함
        if picture[x][y] == 'R' or picture[x][y] =='G':
            picture[x][y] = 'RG'
        else:
            picture[x][y] = 'v'

        dfs(x-1,y,color)
        dfs(x+1,y,color)
        dfs(x,y-1,color)
        dfs(x,y+1,color)

        return True
    else:
        return False

for color in ['R','G','B','RG']:       # 색깔별로 영역 개수 세기
    temp = 0

    for i in range(n):
        for j in range(n):

            if dfs(i,j,color) == True:
                temp += 1

    count.append(temp)

print(sum(count[:3]), sum(count[2:]))
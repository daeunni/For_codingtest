"""

- 큐 : 대기줄 (선입선출)
  * collections 모듈의 deque 사용

"""

from collections import deque

q = deque()    # deque 객체 > list 변환도 가능
q.append(5)
q.append(2)
q.append(3)
q.append(7)

q.popleft()    # 가장 먼저 들어온 5가 삭제된다

q.append(1)
q.append(4)

q.popleft()    # 그 다음 들어온 2가 삭제된다

print(q)       # 먼저 들어온 순서대로 출력된다
q.reverse()

print(q)    # 가장 최근에 들어온 순서대로 출력된다

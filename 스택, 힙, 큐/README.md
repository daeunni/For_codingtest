# 자료구조 모음🧸

### 1. 스택(stack)
- **선입후출**의 구조. 쌓인 상자를 생각하자 
- python에서는 `리스트`로 단순 구현된다! (`append`, `pop()`)



### 2. 큐(Queue)
- **선입선출의** 구조. 놀이기구 줄서기를 생각하자
- python에서는 `from collections import deque` 라이브러리로 구현된다! (`append`, `popleft()`)
- 참고로 이 라이브러리의 `deque` 객체는 **리스트**와 비슷하게 작동한다. (len, 인덱싱 등)


### 2.5. 원형 큐(CircularQueue)    
- 원형 큐도 손쉽게 `from collections import deque`로 구현 가능하다
- 우선 deque를 똑같이 생성한 후, `popleft()`한 원소를 큐에 `append` 해주면 맨 왼쪽 원소가 맨 오른쪽으로 오면서 원형 큐와 같은 효과를 낼 수 있다




### 3. 덱(Deque)
- 양쪽에서 삽입, 삭제를 할 수 있는 자료구조 
- python에서는 큐와 같이 `from collections import deque` 라이브러리로 구현된다! (큐의 확장된 형태)
> 앞에서 삽입, 삭제하면 `appendleft`, `popleft()`          
> 뒤에서 삽입, 삭제하면 `append`, `pop()`

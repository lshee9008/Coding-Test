# [백준/Python] 10845번: 큐

### 문제 링크
[백준 10845번: 큐](https://www.acmicpc.net/problem/10845)

### 문제 설명
정수를 저장하는 큐(Queue)를 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하는 문제입니다. 구현해야 할 명령은 총 6가지입니다.
* `push X`: 정수 X를 큐에 넣는 연산
* `pop`: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력 (비어있으면 -1 출력)
* `size`: 큐에 들어있는 정수의 개수를 출력
* `empty`: 큐가 비어있으면 1, 아니면 0을 출력
* `front`: 큐의 가장 앞에 있는 정수를 출력 (비어있으면 -1 출력)
* `back`: 큐의 가장 뒤에 있는 정수를 출력 (비어있으면 -1 출력)

### 제출 코드

```python
import sys
from collections import deque

def implement_queue():
    # 명령의 수 N 입력
    n = int(sys.stdin.readline())
    queue = deque()
    
    for _ in range(n):
        # 명령어를 입력받고 공백을 기준으로 분리
        command = sys.stdin.readline().split()
        
        if command[0] == 'push':
            queue.append(command[1])
            
        elif command[0] == 'pop':
            if queue:
                # 큐의 가장 앞(왼쪽)에 있는 요소를 제거하고 반환
                print(queue.popleft())
            else:
                print(-1)
                
        elif command[0] == 'size':
            print(len(queue))
            
        elif command[0] == 'empty':
            if queue:
                print(0)
            else:
                print(1)
                
        elif command[0] == 'front':
            if queue:
                # 큐의 가장 앞에 있는 요소 (인덱스 0)
                print(queue[0])
            else:
                print(-1)
                
        elif command[0] == 'back':
            if queue:
                # 큐의 가장 뒤에 있는 요소 (인덱스 -1)
                print(queue[-1])
            else:
                print(-1)

if __name__ == '__main__':
    implement_queue()
```

### 코드 분석

큐는 스택의 후입선출(LIFO)과 반대되는 선입선출(FIFO, First-In-First-Out) 구조를 가집니다. 파이썬에서는 큐를 구현할 때 `collections` 모듈의 `deque`(Double-Ended Queue)를 사용하는 것이 성능상 가장 유리합니다.

**1. 입력 처리 및 문자열 파싱**
```python
import sys
command = sys.stdin.readline().split()
```
명령의 수 N이 최대 10,000개이므로 `sys.stdin.readline()`을 사용하여 입력 속도를 높였습니다. `push 1`과 같은 명령어는 `.split()`을 통해 리스트 형태로 분리하여 인덱스로 접근할 수 있도록 처리했습니다.

**2. deque를 활용한 pop 연산 최적화**
```python
elif command[0] == 'pop':
    if queue:
        print(queue.popleft())
```
파이썬의 일반 리스트(List)로도 큐를 구현할 수는 있지만, 리스트의 첫 번째 요소를 제거하는 `pop(0)`은 남아있는 모든 데이터를 한 칸씩 앞으로 이동시켜야 하므로 시간 복잡도가 O(N)이 됩니다. 반면 `deque`를 사용하고 `popleft()` 메서드를 호출하면, 양방향 입출력에 최적화된 내부 구조 덕분에 O(1)의 시간 복잡도로 가장 앞에 있는 데이터를 즉시 빼낼 수 있습니다.

**3. 양방향 데이터 접근 (front, back)**
```python
print(queue[0])  # front
print(queue[-1]) # back
```
`deque` 역시 일반 리스트처럼 인덱싱을 지원합니다. 가장 먼저 들어와서 대기열의 맨 앞에 있는 데이터는 인덱스 `0`으로, 가장 마지막에 들어와서 대기열의 맨 뒤에 있는 데이터는 인덱스 `-1`로 간단하게 접근하여 출력할 수 있습니다.

### 파이썬 최적화 팁 (포인터를 활용한 리스트 구현)

만약 외부 모듈인 `collections.deque`를 사용할 수 없는 제한적인 환경이라면, 큐의 삽입(push)과 삭제(pop) 위치를 가리키는 포인터 역할을 할 정수 변수를 두고 리스트로 구현할 수도 있습니다.

```python
# deque 없이 리스트와 포인터로 구현하는 팁
queue = []
head = 0  # 팝(pop)할 위치의 인덱스

# ...중략...

elif command[0] == 'pop':
    if len(queue) > head:
        print(queue[head])
        head += 1  # 데이터를 지우지 않고 시작 위치만 한 칸 뒤로 미룸
    else:
        print(-1)
```

위 방식은 실제로 메모리에서 데이터를 삭제하지 않고 시작점만 옮기는 방식이므로, 리스트를 사용하면서도 pop 연산을 O(1)에 처리할 수 있게 해줍니다. 하지만 파이썬에서는 `deque`가 워낙 강력하고 표준적인 도구이므로 개념만 이해해 두시면 충분합니다.

# [백준/Python] 10828번: 스택

### 문제 링크
[백준 10828번: 스택](https://www.acmicpc.net/problem/10828)

### 문제 설명
정수를 저장하는 스택을 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하는 문제입니다. 구현해야 할 명령은 총 5가지입니다.
- `push X`: 정수 X를 스택에 넣는 연산
- `pop`: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력 (비어있으면 -1 출력)
- `size`: 스택에 들어있는 정수의 개수를 출력
- `empty`: 스택이 비어있으면 1, 아니면 0을 출력
- `top`: 스택의 가장 위에 있는 정수를 출력 (비어있으면 -1 출력)

### 제출 코드

```python
import sys

def implement_stack():
    # 명령의 수 N 입력
    n = int(sys.stdin.readline())
    stack = []
    
    for _ in range(n):
        # 명령어를 입력받고 공백을 기준으로 분리
        command = sys.stdin.readline().split()
        
        if command[0] == 'push':
            stack.append(command[1])
            
        elif command[0] == 'pop':
            if stack:
                print(stack.pop())
            else:
                print(-1)
                
        elif command[0] == 'size':
            print(len(stack))
            
        elif command[0] == 'empty':
            if stack:
                print(0)
            else:
                print(1)
                
        elif command[0] == 'top':
            if stack:
                print(stack[-1])
            else:
                print(-1)

if __name__ == '__main__':
    implement_stack()
```

### 코드 분석

파이썬의 기본 자료형인 리스트(List)의 내장 함수를 활용하여 스택의 LIFO(Last In First Out) 구조를 완벽하게 모사할 수 있습니다.

**1. 빠른 입출력을 통한 시간 초과 방지**
```python
import sys
n = int(sys.stdin.readline())
```
명령의 수 N이 최대 10,000개까지 주어질 수 있으므로, 입출력 속도가 느린 `input()` 대신 `sys.stdin.readline()`을 사용해야 시간 초과(Time Limit Exceeded) 판정을 피할 수 있습니다.

**2. 문자열 파싱 (push 처리)**
```python
command = sys.stdin.readline().split()
if command[0] == 'push':
    stack.append(command[1])
```
`push 1`과 같이 명령어와 숫자가 공백으로 구분되어 입력됩니다. `.split()` 함수를 사용하면 `['push', '1']` 형태의 리스트로 분리되므로, 인덱스 0번은 명령어로, 인덱스 1번은 스택에 넣을 값으로 나누어 쉽게 처리할 수 있습니다. 리스트의 `append()` 메서드는 스택의 push 연산과 정확히 동일하게 동작하여 배열의 맨 끝에 요소를 추가합니다.

**3. 예외 처리 및 조건 분기 (pop, top, empty 등)**
```python
elif command[0] == 'pop':
    if stack:
        print(stack.pop())
    else:
        print(-1)
```
파이썬에서는 리스트 자체가 비어있으면 조건문에서 `False`로, 요소가 하나라도 있으면 `True`로 평가됩니다. 이를 활용하여 `if stack:` 구문으로 스택이 비어있는지 직관적으로 확인하고, 요구사항에 맞춰 비어있을 경우 -1을 출력하도록 예외 처리를 구성했습니다. `pop()` 메서드는 리스트의 가장 마지막 요소를 제거함과 동시에 반환해주므로 스택의 pop 연산을 완벽히 수행합니다.

### 파이썬 최적화 팁 (리스트의 시간 복잡도)

파이썬 리스트를 사용하여 스택을 구현할 때 주의해야 할 점은 **데이터를 추가하고 빼는 위치**입니다.
리스트의 맨 끝에서 일어나는 연산인 `append()`와 `pop()`은 시간 복잡도가 `O(1)`로 매우 빠릅니다. 따라서 현재 코드는 스택을 구현하는 데 있어 최적의 효율을 냅니다.

하지만 만약 리스트의 맨 앞(인덱스 0)에서 데이터를 넣거나 빼려고 한다면, 뒤에 있는 모든 데이터가 한 칸씩 이동해야 하므로 시간 복잡도가 `O(N)`으로 크게 늘어납니다. 스택이나 큐를 리스트로 구현할 때는 이 부분의 시간 복잡도를 인지하고 방향을 설정하는 것이 중요합니다.

# [백준/Python] 1874번: 스택 수열

### 문제 링크
[백준 1874번: 스택 수열](https://www.acmicpc.net/problem/1874)

### 문제 설명
1부터 N까지의 수를 오름차순으로 스택에 넣었다가 뽑아 늘어놓음으로써, 입력으로 주어지는 특정 수열을 만들 수 있는지 확인하는 문제입니다. 
스택에 값을 넣는 연산(push)은 `+`로, 스택에서 값을 빼는 연산(pop)은 `-`로 표현하며, 만약 주어진 수열을 스택을 이용해 만들 수 없다면 `NO`를 출력해야 합니다.

### 제출 코드

```python
import sys

def stack_sequence():
    # 수열의 길이 N 입력
    n = int(sys.stdin.readline())
    
    stack = []
    result = []
    current_num = 1
    possible = True
    
    for _ in range(n):
        target = int(sys.stdin.readline())
        
        # 입력받은 목표 수(target)에 도달할 때까지 오름차순으로 스택에 push
        while current_num <= target:
            stack.append(current_num)
            result.append('+')
            current_num += 1
            
        # 스택의 맨 위 숫자가 target과 같다면 pop
        if stack[-1] == target:
            stack.pop()
            result.append('-')
            
        # 스택의 맨 위 숫자가 target과 다르다면 해당 수열은 생성 불가
        else:
            possible = False
            break
            
    # 결과 출력
    if possible:
        for op in result:
            print(op)
    else:
        print("NO")

if __name__ == '__main__':
    stack_sequence()
```

### 코드 분석

이 문제의 핵심은 **스택에 들어가는 수는 반드시 1부터 N까지 오름차순이어야 한다는 조건**을 코드로 어떻게 구현할 것인가입니다. 이를 위해 `current_num`이라는 변수를 사용하여 스택에 넣을 차례인 숫자를 추적합니다.

**1. 오름차순 Push 로직**
```python
while current_num <= target:
    stack.append(current_num)
    result.append('+')
    current_num += 1
```
입력받은 수열의 숫자(`target`)를 만들기 위해서는, 스택에 적어도 `target`까지의 숫자가 들어가 있어야 합니다. 따라서 현재 스택에 넣을 숫자(`current_num`)가 `target`과 같아질 때까지 반복해서 `push` 연산을 수행하고 `+` 기호를 결과 리스트에 담습니다.

**2. Pop 연산 및 수열 생성 가능 여부 검증**
```python
if stack[-1] == target:
    stack.pop()
    result.append('-')
else:
    possible = False
    break
```
필요한 만큼 스택에 숫자를 넣었다면, 이제 스택의 최상단 요소(`stack[-1]`)를 확인합니다. 최상단 요소가 `target`과 일치한다면 정상적으로 값을 빼내어 수열을 구성할 수 있으므로 `pop` 연산을 수행하고 `-`를 기록합니다.

하지만 최상단 요소가 `target`과 다르다면 문제가 발생한 것입니다. 스택은 후입선출(LIFO) 구조이므로, 중간에 있는 값을 빼내기 위해서는 그 위에 있는 값들을 먼저 빼내야만 합니다. 즉, 원하는 숫자가 최상단에 없다면 주어진 오름차순 push 규칙으로는 해당 수열을 절대 만들 수 없음을 의미하므로, 검증 변수(`possible`)를 `False`로 변경하고 탐색을 즉시 종료(`break`)합니다.

**3. 결과 출력 분기**
```python
if possible:
    for op in result:
        print(op)
else:
    print("NO")
```
모든 수열 탐색을 마친 후, 플래그 변수인 `possible`의 상태에 따라 누적된 연산 기호들을 줄바꿈하여 차례대로 출력하거나, 불가능한 경우 `NO`를 출력하여 프로그램을 마무리합니다.

### 알고리즘 핵심 팁

이 문제는 단순한 스택 구현을 넘어, 시뮬레이션(Simulation) 기법이 결합된 문제입니다. 입력 데이터를 배열에 미리 다 받아두고 이중 반복문으로 위치를 찾는 접근법을 생각하기 쉽지만, 그렇게 하면 구현이 매우 복잡해지고 시간 초과가 발생할 위험이 있습니다. 

위 코드처럼 **'현재 스택에 넣을 오름차순 숫자 추적 변수(`current_num`)'**를 하나 두고, 입력으로 들어오는 목표 숫자에 맞춰 능동적으로 스택을 변화시키는 방식으로 접근하는 것이 이 문제의 가장 깔끔한 해답입니다. 

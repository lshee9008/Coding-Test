# [백준/Python] 9012번: 괄호

### 문제 링크
[백준 9012번: 괄호](https://www.acmicpc.net/problem/9012)

### 문제 설명
주어진 괄호 문자열이 올바른 괄호 문자열(VPS, Valid Parenthesis String)인지 판별하는 문제입니다.
여는 괄호 `(` 와 닫는 괄호 `)` 가 올바르게 짝을 지어 구성되어 있어야 하며, 정상적인 VPS라면 "YES", 아니라면 "NO"를 출력합니다.

### 제출 코드

```python
import sys

def check_vps():
    # 입력 속도 최적화를 위해 sys.stdin.readline 사용
    t = int(sys.stdin.readline())
    
    for _ in range(t):
        ps = sys.stdin.readline().strip()
        stack = []
        is_valid = True
        
        for char in ps:
            if char == '(':
                stack.append(char)
            elif char == ')':
                # 스택이 비어있는데 닫는 괄호가 나온 경우
                if not stack:
                    is_valid = False
                    break
                # 스택에 여는 괄호가 있다면 pop으로 제거
                else:
                    stack.pop()
        
        # 순회를 마친 후 스택이 비어있고, is_valid가 True인 경우만 YES
        if not stack and is_valid:
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    check_vps()
```

### 코드 분석

이 문제는 후입선출(LIFO) 특징을 가진 **스택(Stack)** 자료구조를 활용하여 해결하는 것이 핵심입니다. 파이썬에서는 기본 자료형인 리스트(List)가 스택의 역할을 완벽히 수행할 수 있습니다.

**1. 입력 처리 최적화**
```python
import sys
t = int(sys.stdin.readline())
```
여러 줄의 입력을 받아야 하는 문제 특성상, 파이썬의 내장 함수인 `input()` 대신 `sys.stdin.readline()`을 사용하여 입력 처리 속도를 크게 단축했습니다. 문자열 끝의 줄바꿈 문자(`\n`)를 제거하기 위해 `.strip()`을 함께 사용했습니다.

**2. 스택을 이용한 괄호 짝 맞추기**
```python
if char == '(':
    stack.append(char)
elif char == ')':
    if not stack:
        is_valid = False
        break
    else:
        stack.pop()
```
문자열을 순회하며 여는 괄호 `(` 를 만나면 스택에 쌓고(append), 닫는 괄호 `)` 를 만나면 스택에서 여는 괄호를 빼냅니다(pop). 만약 닫는 괄호를 만났는데 스택이 비어있다면, 짝이 맞지 않는 것이므로 즉시 검증 실패(`is_valid = False`) 처리하고 반복문을 탈출(`break`)합니다.

**3. 최종 검증 로직**
```python
if not stack and is_valid:
```
문자열 순회가 끝난 후, 스택에 남아있는 여는 괄호가 없어야(`not stack`) 하며, 순회 도중 닫는 괄호가 초과하여 검증에 실패한 이력이 없어야(`is_valid == True`) 완벽한 VPS로 판별하고 "YES"를 출력합니다.

### 💡 파이썬 최적화 팁 (정수 카운터 활용)

스택 자료구조를 사용하는 것이 정석이지만, 이 문제는 괄호의 종류가 단 한 가지(`()`) 뿐이므로 굳이 리스트 메모리를 할당하지 않고 **정수형 변수를 카운터로 사용하여 공간 복잡도를 최적화**할 수 있습니다.

```python
# 정수형 카운터를 이용한 최적화 코드 일부
count = 0
for char in ps:
    if char == '(':
        count += 1
    elif char == ')':
        count -= 1
        
    # 여는 괄호보다 닫는 괄호가 먼저 많이 나온 경우
    if count < 0:
        break

if count == 0:
    print("YES")
else:
    print("NO")
```

위와 같이 `count` 변수 하나만으로 여는 괄호(+1)와 닫는 괄호(-1)의 누적합을 계산하면, 리스트의 `append`, `pop` 연산 없이도 동일한 논리를 훨씬 가볍고 빠르게 구현할 수 있습니다.

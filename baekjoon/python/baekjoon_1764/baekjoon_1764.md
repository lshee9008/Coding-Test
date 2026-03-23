# [백준/Python] 1764번: 듣보잡

### 문제 링크
[백준 1764번: 듣보잡](https://www.acmicpc.net/problem/1764)

### 문제 설명
듣도 못한 사람의 명단과 보도 못한 사람의 명단이 주어질 때, 듣도 보도 못한 사람(두 명단에 모두 포함된 사람)의 수와 그 명단을 사전순으로 정렬하여 출력하는 문제입니다.

### 제출 코드

```python
import sys

def find_unknowns():
    # 입력 속도 최적화
    input_data = sys.stdin.readline
    
    # N(듣도 못한 사람의 수), M(보도 못한 사람의 수) 입력
    n, m = map(int, input_data().split())
    
    # 듣도 못한 사람을 Set(집합)으로 입력받음
    unheard = set()
    for _ in range(n):
        unheard.add(input_data().strip())
        
    # 보도 못한 사람을 Set(집합)으로 입력받음
    unseen = set()
    for _ in range(m):
        unseen.add(input_data().strip())
        
    # 두 집합의 교집합을 구하고 리스트로 변환한 뒤 사전순 정렬
    result = sorted(list(unheard & unseen))
    
    # 결과 출력
    print(len(result))
    for name in result:
        print(name)

if __name__ == '__main__':
    find_unknowns()
```

### 코드 분석

이 문제는 탐색 횟수와 데이터의 크기가 크기 때문에(최대 500,000) 리스트를 사용하여 비교하면 시간 초과가 발생합니다. 따라서 파이썬의 **집합(Set)** 자료구조와 연산자를 활용하는 것이 핵심입니다.

**1. 시간 초과를 막는 Set 자료구조**
1920번 '수 찾기' 문제와 마찬가지로, 데이터를 저장하고 탐색할 때 리스트 대신 Set을 사용했습니다. Set은 내부적으로 해시 테이블로 구현되어 있어 데이터 탐색에 $O(1)$의 시간 복잡도를 가집니다.

**2. 문자열 전처리 (`strip`)**
```python
unheard.add(input_data().strip())
```
`sys.stdin.readline`을 사용하여 문자열을 입력받을 때는 끝에 줄바꿈 문자(`\n`)가 함께 들어옵니다. 이름 자체만 정확하게 비교하기 위해 `.strip()` 메서드를 사용하여 양옆의 공백과 줄바꿈 문자를 제거한 후 집합에 추가했습니다.

**3. Set의 교집합 연산과 정렬**
```python
result = sorted(list(unheard & unseen))
```
파이썬의 Set은 수학의 집합 연산을 그대로 지원합니다. `&` 연산자(또는 `.intersection()` 메서드)를 사용하면 두 집합에 공통으로 들어있는 원소들만 추출하여 새로운 집합을 만들어 줍니다.
문제의 조건에서 '사전순으로 출력'하라고 명시했으므로, 교집합 결과를 리스트로 변환한 뒤 `sorted()` 함수를 사용하여 알파벳 순서대로 정렬했습니다.

### 💡 파이썬 최적화 팁 (Comprehension 활용)

위 코드도 이미 충분히 효율적이고 가독성이 좋지만, 파이썬 특유의 문법인 **컴프리헨션(Comprehension)**을 사용하면 코드를 더욱 간결하게 줄일 수 있습니다. 반복문을 통해 `add()`로 하나씩 추가하는 과정을 한 줄로 처리할 수 있습니다.

```python
import sys

def optimized_find_unknowns():
    input_data = sys.stdin.readline
    n, m = map(int, input_data().split())
    
    # Set Comprehension을 이용한 간결한 입력
    unheard = {input_data().strip() for _ in range(n)}
    unseen = {input_data().strip() for _ in range(m)}
    
    result = sorted(unheard & unseen)
    
    print(len(result))
    # 언패킹(*)을 활용한 출력 (리스트의 요소를 줄바꿈하여 출력)
    print('\n'.join(result))
```
특히 마지막의 `print('\n'.join(result))` 구문은 `for`문을 돌며 하나씩 `print()`를 호출하는 것보다 I/O 호출 횟수를 줄여주어 실행 속도를 미세하게 더 단축시킬 수 있는 유용한 테크닉입니다.

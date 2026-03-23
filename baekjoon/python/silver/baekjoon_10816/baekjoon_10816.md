# [백준/Python] 10816번: 숫자 카드 2

### 문제 링크
[백준 10816번: 숫자 카드 2](https://www.acmicpc.net/problem/10816)

### 문제 설명
숫자 카드 N개가 주어졌을 때, 입력으로 주어지는 M개의 정수에 대해 각각 해당 숫자가 적힌 카드를 상근이가 몇 개 가지고 있는지 구하는 문제입니다. 1920번 '수 찾기' 문제와 유사하지만 존재 여부를 넘어 중복된 카드의 개수까지 정확히 카운트해야 합니다.

### 제출 코드

```python
import sys
from collections import Counter

def count_cards():
    # N 입력 (사용하지 않음)
    n = int(sys.stdin.readline())
    
    # N개의 카드 번호를 입력받음
    # int로 변환하지 않고 문자열 그대로 활용하여 속도 최적화
    cards = sys.stdin.readline().split()
    
    # M 입력 (사용하지 않음)
    m = int(sys.stdin.readline())
    
    # 찾고자 하는 M개의 카드 번호 입력
    targets = sys.stdin.readline().split()
    
    # Counter를 활용해 카드별 개수를 해시 테이블 형태로 계산
    card_counts = Counter(cards)
    
    # 결과 저장용 리스트
    result = []
    
    for target in targets:
        # 딕셔너리에 target이 있으면 그 개수를, 없으면 0을 반환
        result.append(str(card_counts[target]))
        
    # 결과를 공백으로 구분하여 한 줄로 출력
    print(' '.join(result))

if __name__ == '__main__':
    count_cards()
```

### 코드 분석

이 문제 역시 N과 M이 최대 500,000까지 주어지므로, 시간 복잡도를 철저히 관리해야 합니다. 리스트의 `count()` 함수를 사용하면 O(N) 탐색을 M번 수행하여 O(NM)이 되므로 무조건 시간 초과가 발생합니다.

**1. 해시를 이용한 카운팅 (collections.Counter)**
```python
from collections import Counter
card_counts = Counter(cards)
```
파이썬에서 리스트 요소의 빈도수를 측정할 때 가장 강력하고 효율적인 도구인 `Counter`를 사용했습니다. `Counter`는 내부적으로 딕셔너리(해시 테이블)로 구현되어 있어, O(N)의 시간 복잡도로 배열 내 모든 원소의 개수를 단번에 셉니다. 이후 조회할 때는 O(1)의 시간이 걸리므로 탐색 속도를 극대화할 수 있습니다.

**2. 딕셔너리의 특성 활용**
```python
result.append(str(card_counts[target]))
```
파이썬의 일반 딕셔너리는 존재하지 않는 키(Key)를 조회할 때 `KeyError`를 발생시키지만, `Counter` 객체는 해당 원소가 존재하지 않으면 에러 대신 `0`을 반환하는 매우 유용한 특성을 가집니다. 덕분에 값이 존재하는지 체크하는 `if`문을 생략하고 직관적으로 코드를 작성할 수 있습니다.

**3. 데이터 타입 유지 및 출력 최적화**
숫자의 크기를 비교하는 것이 아니라 '같은 문자인지' 매칭만 하면 되므로 `int()` 변환 과정을 생략했습니다. 또한 매번 `print()`를 호출하는 것보다 결과값을 리스트에 모은 뒤 `' '.join(result)`를 사용해 한 번에 출력하는 것이 입출력 속도 측면에서 훨씬 유리합니다.

### 💡 파이썬 최적화 팁 (이분 탐색 활용법)

해시(딕셔너리)를 사용하는 것이 파이썬의 장점을 가장 잘 살린 풀이 방식이지만, 이 문제의 또 다른 출제 의도인 **이분 탐색(Binary Search)**으로도 접근할 수 있습니다. 

파이썬의 `bisect` 모듈을 사용하면 정렬된 배열 안에서 특정 범위의 개수를 O(log N)만에 구할 수 있습니다. `bisect_right`에서 `bisect_left`를 뺀 값이 곧 해당 원소의 개수가 됩니다. (단, 이분 탐색을 하려면 반드시 카드를 숫자로 변환하고 정렬하는 과정이 필요합니다.)

```python
import sys
from bisect import bisect_left, bisect_right

def using_binary_search():
    # 입력 및 정수 변환 후 정렬
    n = int(sys.stdin.readline())
    cards = sorted(list(map(int, sys.stdin.readline().split())))
    m = int(sys.stdin.readline())
    targets = list(map(int, sys.stdin.readline().split()))
    
    result = []
    for target in targets:
        # target이 들어갈 가장 오른쪽 인덱스에서 가장 왼쪽 인덱스를 뺌 = 원소의 개수
        count = bisect_right(cards, target) - bisect_left(cards, target)
        result.append(str(count))
        
    print(' '.join(result))
```

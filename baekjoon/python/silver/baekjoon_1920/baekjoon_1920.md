# [백준/Python] 1920번: 수 찾기

### 문제 링크
[백준 1920번: 수 찾기](https://www.acmicpc.net/problem/1920)

### 문제 설명
$N$개의 정수가 주어져 있을 때, 이 안에 $X$라는 정수가 존재하는지 알아내는 문제입니다.
기준이 되는 $N$개의 정수 배열이 주어지고, 이후 탐색해야 할 $M$개의 정수들이 주어지면 각각의 숫자가 배열 안에 존재하는지 확인하여 존재하면 1, 존재하지 않으면 0을 출력합니다.

### 제출 코드

```python
import sys

def find_numbers():
    # N 입력 (사용하지 않으므로 변수 할당만 함)
    n = int(sys.stdin.readline())
    
    # N개의 정수를 입력받아 Set(집합) 자료형으로 저장
    # split()으로 나눈 문자열 상태 그대로 저장하여 탐색 속도 최적화
    n_set = set(sys.stdin.readline().split())
    
    # M 입력
    m = int(sys.stdin.readline())
    
    # 탐색할 M개의 정수 리스트 입력
    m_list = sys.stdin.readline().split()
    
    # 탐색 및 결과 출력
    for num in m_list:
        if num in n_set:
            print(1)
        else:
            print(0)

if __name__ == '__main__':
    find_numbers()
```

### 코드 분석

이 문제의 핵심은 **시간 초과(Time Limit Exceeded)를 어떻게 방지할 것인가**입니다. $N$과 $M$의 범위가 각각 최대 100,000이므로, 단순한 이중 반복문을 사용하면 최악의 경우 100억 번의 연산이 발생하여 파이썬에서는 무조건 시간 초과가 발생합니다.

**1. 리스트(List) 대신 집합(Set) 자료형 사용**
```python
n_set = set(sys.stdin.readline().split())
```
파이썬에서 리스트의 `in` 연산자는 내부적으로 처음부터 끝까지 하나씩 요소를 확인하는 선형 탐색을 수행하므로 시간 복잡도가 $O(N)$입니다. $M$개의 숫자를 찾으려면 총 $O(N \times M)$의 시간이 걸립니다.
반면, 집합(`set`) 자료형은 내부적으로 해시 테이블(Hash Table)을 사용하여 구현되어 있습니다. 따라서 `in` 연산자를 통한 탐색의 평균 시간 복잡도가 $O(1)$입니다. 이를 통해 전체 탐색 시간을 $O(M)$ 수준으로 획기적으로 줄일 수 있습니다.

**2. 입력 데이터 타입 유지**
숫자의 대소 비교가 아니라 단순히 '존재 여부'만 확인하면 되므로, 굳이 `int()`를 사용하여 정수형으로 변환하는 과정을 거치지 않았습니다. 문자열 상태 그대로 해싱하여 `set`에 넣고 문자열끼리 비교함으로써 불필요한 형변환 연산 시간을 절약했습니다.

**3. 빠른 입출력 함수 사용**
```python
sys.stdin.readline()
```
입력 데이터의 개수가 최대 10만 개 단위로 주어지기 때문에, 이전 스택 문제들과 마찬가지로 `sys.stdin.readline()`을 사용하여 입출력 병목 현상을 제거했습니다.

### 💡 파이썬 최적화 팁 (이분 탐색 관점)

파이썬에서는 `set`과 `dict`라는 강력한 해시 기반 자료구조를 기본으로 제공하기 때문에 위와 같이 푸는 것이 가장 빠르고 간결합니다. 하지만 이 문제의 출제 의도는 **이분 탐색(Binary Search)** 알고리즘의 구현 능력을 평가하는 것입니다.

알고리즘적 관점을 넓히기 위해 이분 탐색으로 접근한다면 다음과 같은 흐름으로 풀이할 수 있습니다.
1. 주어진 $N$개의 배열을 오름차순으로 정렬합니다. (정렬 시간 복잡도: $O(N \log N)$)
2. 찾고자 하는 $M$개의 값을 정렬된 배열에서 중간값과 비교하며 탐색 범위를 반씩 줄여나갑니다. (탐색 시간 복잡도: $O(M \log N)$)

파이썬의 내장 모듈인 `bisect`를 활용하면 이분 탐색을 직접 구현하지 않고도 아래와 같이 쉽게 해결할 수 있습니다. 다른 언어(C++, Java 등)로 알고리즘을 공부하실 때는 해시보다는 이분 탐색으로 접근하는 것이 정석입니다.

```python
import sys
from bisect import bisect_left, bisect_right

def using_binary_search():
    n = int(sys.stdin.readline())
    # 이분 탐색을 위해 반드시 정렬해야 함 (이때는 정수형 변환 필요)
    n_list = sorted(list(map(int, sys.stdin.readline().split())))
    m = int(sys.stdin.readline())
    m_list = list(map(int, sys.stdin.readline().split()))
    
    for num in m_list:
        # bisect를 이용해 값이 들어갈 인덱스 탐색
        index = bisect_left(n_list, num)
        # 해당 인덱스가 배열 범위 내에 있고, 실제 값이 num과 일치하는지 확인
        if index < len(n_list) and n_list[index] == num:
            print(1)
        else:
            print(0)
```

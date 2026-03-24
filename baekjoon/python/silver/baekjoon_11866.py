import sys
from collections import deque

def josephus_problem():
    n, k = map(int, sys.stdin.readline().split())

    queue = deque(range(1, n + 1))
    result = []
    
    while queue:
        for _ in range(k - 1):
            queue.append(queue.popleft())

        result.append(str(queue.popleft()))

    print("<" + ", ".join(result) + ">")

if __name__ == '__main__':
    josephus_problem()
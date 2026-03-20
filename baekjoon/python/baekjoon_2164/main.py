import sys
from collections import deque

def find_last_card():
    n = int(sys.stdin.readline())

    cards = deque(range(1, n + 1))

    while len(cards) > 1:
        cards.popleft()

        cards.append(cards.popleft())

    print(cards[0])

if __name__ == '__main__':
    find_last_card()
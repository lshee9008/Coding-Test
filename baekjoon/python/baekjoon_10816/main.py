import sys
from collections import Counter

def count_cards():
    n = int(sys.stdin.readline())

    cards = sys.stdin.readline().split()

    m = int(sys.stdin.readline())

    targets = sys.stdin.readline().split()

    card_counts = Counter(cards)

    result = []

    for target in targets:
        result.append(str(card_counts[target]))

    print(' '.join(result))

if __name__ == '__main__':
    count_cards()

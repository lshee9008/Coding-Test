import sys


def find_unknowns():
    input_data = sys.stdin.readline

    n, m = map(int, input_data().split())

    unheard = set()
    for _ in range(n):
        unheard.add(input_data().strip())

    unseen = set()
    for _ in range(m):
        unseen.add(input_data().strip())

    result = sorted(list(unheard & unseen))

    print(len(result))
    for name in result:
        print(name)


if __name__ == '__main__':
    find_unknowns()

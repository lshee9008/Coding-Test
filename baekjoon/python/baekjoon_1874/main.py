import sys

def calculate_ledger():
    k = int(sys.stdin.readline())
    stack = []

    for _ in range(k):
        num = int(sys.stdin.readline())

        if num == 0:
            stack.pop()
        else:
            stack.append(num)

    print(sum(stack))


if __name__ == '__main__':
    calculate_ledger()
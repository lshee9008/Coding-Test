import sys


def stack_sequence():
    n = int(sys.stdin.readline())

    stack = []
    result = []
    current_num = 1
    possible = True

    for _ in range(n):
        target = int(sys.stdin.readline())

        while current_num <= target:
            stack.append(current_num)
            result.append('+')
            current_num += 1

        if stack[-1] == target:
            stack.pop()
            result.append('-')

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
import sys

def josephus_problem():
    n, k = map(int, sys.stdin.readline().split())

    people = list(range(1, n + 1))
    result = []

    index = 0

    while people:
        index = (index + k - 1) % len(people)

        result.append(str(people.pop(index)))

    print("<" + ", ".join(result) + ">")



if __name__ == '__main__':
    josephus_problem()
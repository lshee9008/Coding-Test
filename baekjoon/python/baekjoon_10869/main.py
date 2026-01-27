def calculation():
    lst = list(map(int, input().split()))

    print(lst[0] + lst[1])
    print(lst[0] - lst[1])
    print(lst[0] * lst[1])
    print(lst[0] // lst[1])
    print(lst[0] % lst[1])

if __name__ == '__main__':
    calculation()
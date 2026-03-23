def compare():
    A, B = map(int, input().split())
    if A > B:
        print('>')
    elif A < B:
        print('<')
    elif A == B:
        print('==')

if __name__ == '__main__':
    compare()
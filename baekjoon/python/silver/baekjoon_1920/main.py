import sys

def find_numbers():
    n = int(sys.stdin.readline())

    n_set = set(sys.stdin.readline().split())

    m = int(sys.stdin.readline())

    m_list = sys.stdin.readline().split()

    for num in m_list:
        if num in n_set:
            print(1)
        else:
            print(0)

if __name__ == '__main__':
    find_numbers()
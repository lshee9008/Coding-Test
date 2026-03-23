import sys

def check_vps():
    t = int(sys.stdin.readline())

    for _ in range(t):
        ps = sys.stdin.readline().strip()
        stack = []
        is_valid = True

        for char in ps:
            if char == '(':
                stack.append(char)
            elif char == ')':
                if not stack:
                    is_valid = False
                    break
                else:
                    stack.pop()
        if not stack and is_valid:
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    check_vps()
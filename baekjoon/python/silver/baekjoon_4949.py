import sys

def check_balanced_world():
    while True:
        line = sys.stdin.readline().rstrip()

        if line == '.':
            break

        stack = []
        is_balanced = True

        for char in line:
            if char == '(' or char == '[':
                stack.append(char)

            elif char == ')':
                if not stack or stack[-1] != '(':
                    is_balanced = False
                    break
                stack.pop()
            elif char == ']':
                if not stack or stack[-1] != '[':
                    is_balanced = False
                    break
                stack.pop()

        if is_balanced and not stack:
            print("yes")
        else:
            print("no")

if __name__ == '__main__':
    check_balanced_world()
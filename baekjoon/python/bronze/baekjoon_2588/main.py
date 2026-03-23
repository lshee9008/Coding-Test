def multiple():
    A = input()
    B = input()
    A = int(A)
    B = int(B)
    B_list = [(B // 100), (B // 10) % 10, (B % 10)]
    print(A * B_list[2])
    print(A * B_list[1])
    print(A * B_list[0])
    print(A * B)

if __name__ == "__main__":
    multiple()
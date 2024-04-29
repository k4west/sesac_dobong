# 점화식 풀이
def fibo(n):
    a = b = 1
    for _ in range(n):
        a, b = b, a + b
    return a


print(fibo(int(input())))

########################################################
# 아래는 확장..?


# 행렬곱 풀이
# 1차원 리스트
def mul(A: list, B: list) -> list:
    return [
        A[0] * B[0] + A[1] * B[1],
        A[0] * B[1] + A[1] * B[2],
        A[1] * B[1] + A[2] * B[2],
    ]


# 2차원 리스트
# def mul(A: list, B: list) -> list:
#     return [
#         [A[0][0] * B[0][0] + A[0][1] * B[1][0], A[0][0] * B[0][1] + A[0][1] * B[1][1]],
#         [A[1][0] * B[0][0] + A[1][1] * B[1][0], A[1][0] * B[0][1] + A[1][1] * B[1][1]],
#     ]


# 분할 정복
def sol(n, A):
    if n == 1:
        return A
    elif n % 2:
        return mul(mul(sol(n // 2, A), sol(n // 2, A)), [1, 1, 0])
    else:
        return mul(sol(n // 2, A), sol(n // 2, A))


# 그냥
# print(sol(int(input()), [1, 1, 0])[1])

# 도가뉴 항등식 n -> n^.5까지 구하면 됨..
n = int(input())
A = sol((n + 1) // 2, [1, 1, 0])
if n % 2:
    print(A[1] ** 2 + A[2] ** 2)
else:
    print(A[0] ** 2 - A[2] ** 2)

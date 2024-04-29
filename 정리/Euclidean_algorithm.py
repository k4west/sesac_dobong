# 유클리드 호제법(euclidean algorithm)
# 두 수의 gcd(최대공약수)를 구하는 알고리즘
# gcd를 이용해서 lcm(최소 공배수) 구하기

# 내장된 math의 gcd, lcm 함수를 사용해도 됨
# import math
# math.gcd()
# math.lcm()


def gcd(A: int, B: int) -> int:
    while A % B:
        A, B = B, A % B
        return B


def lcm(A: int, B: int) -> int:
    return A * B * gcd(A, B)


# 확장된 유클리드 알고리즘(exteded euclidean algorithm)
# a와 b의 gcd 외에 다음과 같은 s, t를 구하는 알고리즘 : a*s + b*t = GCD(a, b)

# a와 b가 서로소일때, gcd(a, b) = 1 이므로 as ≡ 1 (mod b), bt ≡ 1(mod a)
# 즉 s는 모듈러 b의 곱 연산에서 a의 역원이고,
# t는 모듈러 a의 곱 연산에서 b의 역원이다.


def EEA(A: int, B: int) -> int:
    s1, s2, t1, t2 = 1, 0, 0, 1
    while A % B:
        q, r = A // B, A % B  # q, r = divmod(A, B)
        A, B = B, r
        s, t = s1 - q * s2, t1 - q * t2
        s1, s2, t1, t2 = s2, s, t2, t
    return r, s, t  # r = gcd(A, B) = A*s + B*t

# 에라토스테네스의 체
# 주어진 범위 내에서 소수를 찾는 알고리즘

# 소수 : 1과 자신만을 약수로 가지는 수
# 2, 3, 5, 7, 11, ...


# 루트 값 이하의 정수로 나누어떨어지지 않은지 확인해서 소수인지 판별하는 알고리즘
def isPrime(n: int) -> bool:
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


# 소수의 배수를 제외해서 소수인지 판별하는 알고리즘
# (0)2부터 N 사이의 정수 중 소수인 인텍스에 True, 소수가 아닌 정수 인덱스에는 False를 담아서 반환
def isPrime(N):
    primes = [False, False] + [True] * (N - 1)  # 0, 1은 소수가 아님
    for i in range(2, int(N**0.5) + 1):  # root N 이하인 정수까지만 확인하면 됨 ... *
        if primes[i]:
            for j in range(i * i, N + 1, i):  # 소수의 배수는 합성수 -> 소수 x
                primes[j] = False
    return primes  # 소수 인덱스에는 True를 이 외에는 False를 갖는 리스트


# * N 이하인 어떤 수(=n)의 n이 아닌 약수(=d)가 root N 초과라면
# e라는 정수가 존재해서 e = N/d 입니다.
# 여기서 e는 root N 보다 작아서 for i in range(2, int(N**.5) + 1)
# 위 for문에서 이미 탐색이 이루어졌습니다.

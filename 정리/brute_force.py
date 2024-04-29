# 완전 탐색(Brute-Force/ Exhaustive Search)
# 가능한 후보를 모두 탐색하는 알고리즘
# for문이나 while문으로 가능한 경우를 모두 탐색함


# 가능한 후보를 모두 탐색하는 완전 탐색 알고리즘 예
def brute_force(candidates, target):
    for n in candidates:
        if n == target:
            print(n)
            break
    else:
        print(0)

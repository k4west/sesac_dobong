# 이분/이진 탐색(Binary Search)
# (오름차순으로) 정렬된 리스트에서
# 초기 시작(s, low)과 마지막(e, high) 인덱스 설정
# 탐색할 인덱스(m) = (시작 + 마지막 // 2)
# s <= e 동안 아래 과정을 반복 (while문)
# 탐색한 값이 목표 값보다 작으면 (더 큰 값을 찾아야 함)
# s = m + 1
# 탐색한 값이 목표 값보다 크면 (더 작은 값을 찾아야 함)
# e = m - 1
# 목표 값을 찾으면 return을 하거나, 문제를 풀기 위해 추가적인 조취를 취하면 됨

# 위 과정을 recurssive하게 dfs 알고리즘을 적용해서 진행할 수도 있다.


# 이진 검색 알고리즘으로 arr(오름차순 정렬됨) 내에서 target의 인덱스 구하는 함수
# 없으면 -1 반환


# While 문
def binary_search(arr, target, s, e):
    while s <= e:
        m = (s + e) // 2
        if arr[m] > target:
            e = m - 1
        elif arr[m] < target:
            s = m + 1
        else:
            return m
    return -1


# 재귀 함수, dfs 알고리즘
def binary_search(arr, target, s, e):
    if s > e:
        return -1
    m = (s + e) // 2
    if arr[m] > target:
        binary_search(arr, target, s, m - 1)
    elif arr[m] < target:
        binary_search(arr, target, m + 1, e)
    else:
        return m

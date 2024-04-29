"""lambda 공부해야할 코드1"""
# 내가 삽질한 코드
# def sort_by_last
# _letter(names):
#         names.sort(key= lambda x : names[i][len(x)] for i in range(len(names)))

#     names.sort(reverse=True)
#     return names


# gpt가 알려준 코드 진짜 깔끔하다 !
# def sort_by_last_letter(names):
#     names.sort(key=lambda x: x[-1])
#     return names

# sort_by_last_letter(["Jessie", "Paul", "John"])


#################################################
"""lambda 공부해야할 코드2"""
# gpt 참고
# def filter_air_quality(data, threshold):
#     result = filter(lambda x: x > threshold, data)
#     RESULT = list(result)
#     print(RESULT)
#     return RESULT


# filter_air_quality([50, 40, 60, 90, 30], 50)


"""lambda에 관하여"""
# def add_lists(list1, list2):
#     plus = lambda x, y: x + y
#     result = []
#     for i in range(len(list1)):
#         result.append(plus(list1[i], list2[i]))

#     print(result)
#     return result


# add_lists([1, 2, 3], [4, 5, 6])


# def add_lists(list1, list2):
#     result = list(map(lambda x, y: x + y, list1, list2))


# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
# print(even_numbers)


# map(), filter,() sorted() 이런애들이랑 lambda가 잘쓰인다.. 왜냐면 그 iterable에 들어가는 요소들을 lambda랑 같이 쓰면
# 한번에 대입하는 등 굉장히 편리해지기 때문이다. 거의 함수정의해서 그 인자값 바로 받는 매개변수 역할을 하는 듯?
"""""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """"""
# def solution(a, b):
#     plus = lambda x, y: int(str(x) + str(y))

#     result = max(plus(a, b), 2 * a * b)

#     print(result)

#     return result


# solution(5, 6)

# plus = lambda x, y: int(str(x) + str(y))
# result = max(lambda x, y: int(str(x) + str(y)))

# # 여기서 str 아니고 'x' 'y' 이렇게 따옴표로 덮게되면
# # 변수 x가 아니라 진짜 문자 x라고 인식하게 됨 그래서 x가 유지될 수 있는 str() 함수로 해야함.
"""""" """""" """""" """""" """""" """""" """""" """""" """"""


# import time

# def timeit(func):
#     def wrapper(*args, **kwargs):
#         start_time = time.time()  # 함수 실행 전 시간 기록
#         result = func(*args, **kwargs)  # 함수 실행
#         end_time = time.time()  # 함수 실행 후 시간 기록
#         print(f"실행시간 : {end_time - start_time:4f}초")
#         return result

#     return wrapper


# # 예제 사용
# @timeit
# def example_function(n):
#     s = 0
#     for i in range(n):
#         s += i
#     return s


# # 함수 실행 및 시간 측정
# example_function(1000000)

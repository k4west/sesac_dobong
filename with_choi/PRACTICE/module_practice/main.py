# import my_module

# print(my_module.add(5, 3))
# print(my_module.subtract(5, 3))

# mul = my_module.Multiplier()
# print(mul.do(5, 4))


# from my_module import *

# print(add(5, 3))
# print(subtract(5, 3))

# mul = Multiplier()
# print(mul.do(5, 4))


from my_module import subtract

print(subtract(1, 4))

a = 10
b = 20
user_variables = {
    key: value
    for key, value in globals().items()
    if not key.startswith("__") and not callable(value)
}
print(user_variables)

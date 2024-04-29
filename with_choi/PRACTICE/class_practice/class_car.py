class Car:
    def __init__(self, color, brand):
        self.color = color
        self.brand = brand

    def drive(self):
        return f"{self.brand} 붕붕~"

    def stop(self):
        return f"{self.brand} 끼이익"


# 객체 생성
my_car = Car("회색", "모닝")
print(my_car.drive())
print(my_car.stop())

class Pikachu:
    def __init__(self, name="그냥 피카츄"):
        self.name = name
        self.health = 100
        self.level = 1
        self.attack_power = 10

    def __repr__(self):
        return "Pika Pika!"

    def attack(self, target=None):
        if target is None:
            print(f"{self.name}공격할 상대가 필요해요 ㅜㅜ")
            return

        damage = self.attack_power * self.level
        print(f"{self.name}이 {target.name}을 {damage}의 데미지로 공격했다!")
        target.be_attacked(damage, self)

    def be_attacked(self, damage, attacker):
        self.health -= damage
        print(f"{self.name}는 {damage}의 데미지만큼 {attacker.name}에게 상처를 입었다!")

        if self.health <= 0:
            print(f"{self.name}는 더 이상 싸울 수 없다!")
            self.health = 0

    def heal(self, amount=10):
        self.health += amount
        if self.health > 100:
            self.health = 100
        print(f"{self.name}가 체력을 {amount} 만큼 회복했다!")


yello_pikachu = Pikachu("노란색 피카츄")
red_pikachu = Pikachu("빨간색 피카츄")

print(yello_pikachu)
print(red_pikachu)

yello_pikachu.attack(red_pikachu)
red_pikachu.attack(yello_pikachu)

for i in range(10):
    yello_pikachu.attack(red_pikachu)

print(red_pikachu.health)

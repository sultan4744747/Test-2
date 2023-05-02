import random
import time


class Player:
    def __init__(self, xp, damage, name):
        self.name = None
        self.xp = xp
        self.damage = damage
        self.level = 1
        self.exp = 0

    def Alf(species, name, species2, ):
        xp = 0
        damage = 0
        if species == species_list[0]:
            xp = 100
            damage = 30
        elif species == species_list[1]:
            xp = 100
            damage = 30
        elif species == species_list[2]:
            xp = 100
            damage = 30
        else:
            print('Вы выбрали не существуещего героя')
        if species2 == species2_list[0]:
            xp -= 20
            damage += 40
        elif species2 == species2_list[1]:
            xp += 20
            damage += 20
        elif species2 == species2_list[2]:
            xp -= 30
            damage += 50
        else:
            print('Вы выбрали не существующую професию')

        return Player(xp, damage, name)

    def fight(self, enemy):
        enemy.xp1 -= self.damage
        max_exp = self.level * 100
        if enemy.xp1 <= 0:
            print('вы победили')
            return False
        else:
            print(f'Оставшееся здоровье:{enemy.xp1}')
            return True

    def lvl(self, max_exp):
        self.exp -= max_exp
        self.level += 1
        self.damage += 5
        self.xp += 5
        print(f'Вы достигли нового уровня!!!\nВаш текущий уровень:{self.level}')


class Enemy:
    def __init__(self, xp, damage, name):
        self.name1 = name
        self.xp1 = xp
        self.damage1 = damage

    def create_Enemy(self):
        name = random.choice(enemy_species_list)
        xp = random.randint(30, 70)
        damage = random.randint(17, 40)
        return Enemy(xp, damage, name)

    def fight(self, hero):
        hero.xp -= self.damage1
        if hero.xp <= 0:
            print('вы погибли')
            return False
        else:

            print(f'Оставшееся здоровье:{hero.xp}')
            return True


def fightchoice():
    c = random.randint(1, 2)
    a = input('Готов ли ты сражаться ? да или нет\n').lower()
    if a == "да":
        result = hero.fight(enemy)
        if result == True:
            enemy.fight(hero)
            fightchoice()
    elif a == "нет":

        if c == 1:
            print("Вы не смогли убежать ")
            fight()
        elif с == 2:
            print('Вы убежали')
            fight()




    else:
        print('У вас нет такого варианта ')
        fightchoise()


enemy_species_list = ['слизь', 'варвар', 'зомби']

name = input('Введите свой NickName:')

species_list = ['эльф', 'гном', "оборотень"]

print(f'{name},Здравствуйте ')

print(f'Выберите героя:{species_list}')

species = input('Ваш выбор:').lower()

species2_list = ['лучник', 'рыцарь', 'волшебник']

print(f'Выберите проффесию:{species2_list}')

species2 = input('Ваш выбор:').lower()

hero = Player.Alf(species, name, species2)

print(
    f'Характеристика вашего героя:Имя:{name}\nЗдоровье:{hero.xp}\nУрон:{hero.damage}\nУровень:{hero.level}\nОпыт:{hero.exp} ')
while True:
    b = random.randint(1, 2)
    if b == 1:
        print('Никто не встретился,идем дальше')
        time.sleep(3)

    else:
        enemy = Enemy.create_Enemy()

        print(f'Вы встретили: {enemy.name1}\nЕго характеристики:\nЗдоровье:{enemy.xp1}\nУрон:{enemy.damage1}')
        time.sleep(3)
        fightchoice()

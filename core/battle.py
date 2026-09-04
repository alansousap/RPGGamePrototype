from assets.main import Main
from assets.enemy import Enemy
import random

class Battle:

    def __init__(self, main:Main, enemy:Enemy):
        self.__dice = 20
        self.__main = main
        self.__enemy = enemy
        self.__bonus = 0

    def main_attack(self, action:str) -> float:
        if action == '1':
            power = self.__main.get_atk_damage()
        if action == '2':
            power = self.__main.get_mag_damage()

        damage = self.__calculate_damage(power)

        if damage > 0.00:
            enemy_life = self.__enemy.get_life()
            enemy_life = enemy_life - damage
            if enemy_life < 0.00:
                enemy_life = 0.00
            self.__enemy.set_life(enemy_life)

            if action == '2':
                magic = self.__main.get_magic()
                magic = magic - 25.00
                if magic < 0.00:
                    magic = 0.00
                self.__main.set_magic(magic)

        return damage

    def enemy_attack(self) -> float:
        power = self.__enemy.get_atk_damage()

        damage = self.__calculate_damage(power)

        if damage > 0.00:
            main_life = self.__main.get_life()
            main_life = main_life - damage
            if main_life < 0.00:
                main_life = 0.00
            self.__main.set_life(main_life)

        return damage

    def __calculate_damage(self, power:int) -> float:
        roll = random.randint(1, self.__dice)

        damage = 0.00
        if roll <= 10:
            damage = power * 0.75
        if roll > 10 and roll < 20:
            damage = power * 0.90
        if roll == 20:
            damage = power * 1.00

        self.__bonus += 1
        if self.__bonus == 6:
            damage += 150.00
            self.__bonus = 0

        return damage

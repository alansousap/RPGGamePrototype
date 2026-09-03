from assets.main import Main
from assets.enemy import Enemy
from core.battle import Battle
import subprocess
import os

class Game:

    def __init__(self, name:str):
        self.__main = Main(name, 500.00, 100, 50.00, 250)
        self.__enemy = Enemy("Morcego", 1000.00, 50)
        self.__battle = Battle(self.__main, self.__enemy)

    def start_game(self) -> None:
        battle_on = True
        turno = 1

        while battle_on:
            self.__clear()

            print(f"\nTurno: {turno}")
            self.__show_stats()
            
            action = self.__choose_action()
            damage = self.__battle.main_attack(action)
            print(f"\n{self.__main.get_name()} tirou {damage} de dano")
            
            print(f"\nO {self.__enemy.get_name()} efetuou um Ataque Físico!")
            damage = self.__battle.enemy_attack()
            print(f"\n{self.__enemy.get_name()} tirou {damage} de dano")

            if self.__main.get_life() == 0:
                print("\nSinto Muito, Você Perdeu!")
                battle_on = False
                break
            
            if self.__enemy.get_life() == 0:
                print("\nMuito Bem, Você Ganhou!")
                battle_on = False
                break

            input("\nAperte [Enter] para o Próximo Turno")
            turno += 1

        input("\nAperte [Enter] para Terminar")
        

    def __show_stats(self) -> None:
        print(f"\n{self.__main.get_name()}(HP): {self.__main.get_life()}")
        print(f"{self.__main.get_name()}(MP): {self.__main.get_magic()}")
        print(f"{self.__enemy.get_name()}(HP): {self.__enemy.get_life()}")

    def __choose_action(self) -> str:
        print("\nAções disponiveis:")
        print("1 - Ataque Físico")
        print("2 - Ataque Mágico")
        action = input(f"{self.__main.get_name()}, Escolha sua ação : ")
        if action != '1' and action != '2':
            print("Ação inválida, utilizando Ataque Físico!")
            action = str('1')
        if action == '2' and self.__main.get_magic() == 0.00:
            print("Sem MP para o Ataque Mágico, utilizando Ataque Físico!")
            action = str('1')
        return action

    def __clear(self) -> None:
        subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)
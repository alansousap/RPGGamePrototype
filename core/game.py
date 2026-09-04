from assets.main import Main
from assets.enemy import Enemy
from core.battle import Battle
import subprocess
import os

class Game:

    def __init__(self, name:str):
        self.__main = Main(name, 1000.00, 250, 50.00, 500)
        self.__enemy_list = [
            Enemy("Morcego", 800.00, 50),
            Enemy("Valomir", 1200.00, 100),
            Enemy("Adria", 2000.00, 150),
        ]

    def start_game(self) -> None:
        game_on = True
        battle_count = 0

        for enemy in self.__enemy_list:
            battle_on = True
            round = 1

            battle_count += 1
            battle = Battle(self.__main, enemy)
            
            while battle_on:
                self.__clear()

                print(f"\nBatalha: {battle_count}")
                print(f"Rodada: {round}")
                self.__show_stats(enemy)
                
                action = self.__choose_action()
                damage = battle.main_attack(action)
                print(f"\n{self.__main.get_name()} tirou {damage} de dano")
                
                print(f"\nO {enemy.get_name()} efetuou um Ataque Físico!")
                damage = battle.enemy_attack()
                print(f"\n{enemy.get_name()} tirou {damage} de dano")

                if self.__main.get_life() == 0:
                    print("\nSinto Muito, Você Perdeu!")
                    battle_on = False
                    game_on = False
                    break
                
                if enemy.get_life() == 0:
                    print("\nMuito Bem, Você Ganhou!")
                    battle_on = False
                    break

                input("\nAperte [Enter] para a Próxima Rodada")
                round += 1

            if not game_on:
                break

            life = self.__main.get_life()
            self.__main.set_life(1000.00)
            self.__main.set_magic(50.00)

            input("\nBatalha terminou, aperte [Enter] para a próxima batalha")

        input("\nAperte [Enter] para Terminar")
        

    def __show_stats(self, enemy:Enemy) -> None:
        print(f"\n{self.__main.get_name()}(HP): {self.__main.get_life()}")
        print(f"{self.__main.get_name()}(MP): {self.__main.get_magic()}")
        print(f"{enemy.get_name()}(HP): {enemy.get_life()}")

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
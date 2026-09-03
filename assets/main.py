from assets.character import Character

class Main(Character):

    def __init__(self, name:str, life:float, atk_damage:int, magic:float, mag_damage: int):
        super().__init__(name, life, atk_damage)
        self.__magic = magic
        self.__mag_damage = mag_damage

    def get_magic(self) -> float:
        return self.__magic

    def set_magic(self, magic:float) -> None:
        self.__magic = magic

    def get_mag_damage(self) -> int:
        return self.__mag_damage

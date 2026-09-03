class Character:

    def __init__(self, name:str, life:float, atk_damage:int):
        self.__name = name
        self.__life = life
        self.__atk_damage = atk_damage
    
    def get_name(self) -> str:
        return self.__name

    def get_life(self) -> float:
        return self.__life
    
    def get_atk_damage(self) -> int:
        return self.__atk_damage

    def set_life(self, life: float) -> None:
        self.__life = life

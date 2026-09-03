from assets.character import Character

class Enemy(Character):

    def __init__(self, name:str, life:float, atk_points:int):
        super().__init__(name, life, atk_points)

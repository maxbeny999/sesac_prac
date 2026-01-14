from abc import ABC,  abstractmethod
from weapons import Sword, Wand

class Job(ABC):

    def __init__(self, attack_style):
        self.attack_style = attack_style

    @ abstractmethod
    def attack(self):
        pass

class Warrior(Job):

    def __init__(self,):
        super().__init__("검을 휘둘러 벤다")
        self.exclusive_weapon = [Sword]

    def attack(self):
        print(f" {self.attack_style} ")

class Mage(Job):

    def __init__(self):
        super().__init__("지팡이를 조준해 마법을 쏜다")
        self.exclusive_weapon = [Wand]

    def attack(self):
        print(f"{self.attack_style}")

class Character:
    def __init__(self, name, job):
        self.name = name
        self.job = job        # Warrior 또는 Mage 객체가 들어옵니다.
        self.weapon = None    # 처음엔 무기가 없습니다.

    # 1. 공격하기 (직업에게 시킴)
    def attack(self):
        print(f"\n[{self.name}의 공격 턴!]")
        # 내 직업(self.job)이 가지고 있는 attack() 메서드를 실행
        self.job.attack()

    # 2. 무기 장착 (경찰 역할: 직업 규칙 확인)
    def equip_weapon(self, new_weapon):
        # type(new_weapon) -> Sword 클래스인지 Wand 클래스인지 확인
        # self.job.exclusive_weapon -> [Sword] 같은 허용 목록 리스트
        
        if type(new_weapon) in self.job.exclusive_weapon:
            self.weapon = new_weapon
            print(f"{self.name}이(가) 무기를 장착했습니다! (스킬: {self.weapon.skill_name})")
        else:
            print(f"{self.name}({type(self.job).__name__})은(는) 이 무기를 착용할 수 없습니다.")

    # 3. 스킬 사용 (무기에게 시킴)
    def use_skill(self):
        if self.weapon is None:
            print(" 무기가 없어서 스킬을 쓸 수 없습니다!")
        else:
            # 내 무기(self.weapon)가 가지고 있는 use_skill() 메서드를 실행
            self.weapon.use_skill()
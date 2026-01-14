from abc import ABC, abstractmethod

# Weapon 클래스 ( 모든 무기들 부모 클래스 (설계도))
class Weapon(ABC): 
    def __init__ (self, skill_name):
        # [ 작동원리 3 ] 자식이 정보를 넘겨주면 받아서 self.skill_name 변수에 저장해둠
        self.skill_name = skill_name

    # [ 작동원리 1] 추상 메서드 정의
    # 모든 Weapon 클래스는 use_skill 기능이 있어야 한다고 규칙을 선언함
    # 내용을 비워두고 넘긴다 (pass 사용) 이 부분 구현은 자식이 한다.
    @abstractmethod
    def use_skill(self):
        pass

# Sword 클래스 ( Weapon 클래스의 자식 / (설계도를 기반으로 만든 실체) )
class Sword(Weapon):

    def __init__(self):
        # [ 작동원리 2 ] Sword가 생성될 때 실행된다.
        # super().__init__을 통해 부모클래스(Weapon)의 생성자를 호출한다
        super().__init__("Giant Hunt")
        # "Giant Hunt" 라는 스킬의 구체적 정보를 부모에 전달한다

    # [ 작동원리 4 ] 오버라이딩 (덮어쓰기)
    # 부모가 @abstractmethod 로 강제한 use_skill을 실제로 동작하게 하는 단계
    def use_skill(self):
        # [ 작동원리 5 ] 실행한다
        # 부모가 [ 작동원리 3 ] 에서 저장한 self.skill_name을 꺼내서 사용한다.
        print(f"무기 스킬 사용 {self.skill_name}")

# 전체흐름
# --- 테스트 코드 (실행 흐름 미리보기) ---
# my_sword = Sword()      # 1. Sword 생성 -> 2. 부모에게 "Giant Hunt" 전달 -> 3. 저장
# my_sword.use_skill()    # 4. use_skill 호출 -> 5. 저장된 "Giant Hunt" 출력

class Wand(Weapon):

    def __init__(self):
        super().__init__("Comet")

    def use_skill(self):
        print(f"무기 스킬 사용 {self.skill_name}")
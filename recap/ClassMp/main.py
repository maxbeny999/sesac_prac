# [설명] 다른 파일(모듈)에 만들어둔 클래스(설계도)들을 가져옵니다.
from char import Character        # char.py 파일에서 Character 클래스 가져옴
from jobs import Warrior, Mage    # jobs.py 파일에서 Warrior, Mage 클래스 가져옴
from weapons import Sword, Wand   # weapons.py 파일에서 Sword, Wand 클래스 가져옴

# ==========================================
# 1. 캐릭터 생성 (합성: Composition)
# ==========================================
# 설명: '아서'라는 이름의 객체를 만듭니다.
# 중요: 두 번째 인자로 Warrior() 객체를 생성해서 넘겨줍니다.
#      -> 이제 arthur.job 에는 Warrior 객체가 저장됩니다. (jobs.py 참조)
arthur = Character("아서", Warrior())  

# 설명: '멀린' 객체 생성, Mage() 객체를 직업으로 넘겨줍니다.
merlin = Character("멀린", Mage())      


# ==========================================
# 2. 무기 준비 (객체 생성)
# ==========================================
# 설명: Sword()를 호출하면 weapons.py의 Sword 클래스 __init__이 실행됩니다.
#      -> 내부적으로 skill_name="Giant Hunt"가 저장된 객체가 나옵니다.
my_sword = Sword()  

# 설명: Wand()를 호출하면 skill_name="Comet"이 저장된 객체가 나옵니다.
my_wand = Wand()    


# ==========================================
# 3. 테스트 시작 (상호작용)
# ==========================================

print("=== ⚔️ 전사 아서 테스트 ===")

# [상황 1] 전사가 지팡이를 들려고 함 (실패 케이스)
# 흐름: 
# 1. char.py의 equip_weapon(my_wand) 실행
# 2. '경찰' 로직 발동: type(my_wand)가 arthur.job.exclusive_weapon 리스트에 있는지 검사
# 3. Warrior의 허용 목록은 [Sword]인데, 들어온 건 Wand -> 실패!
arthur.equip_weapon(my_wand)   


# [상황 2] 전사가 검을 들려고 함 (성공 케이스)
# 흐름:
# 1. type(my_sword)는 Sword 클래스임 -> Warrior 허용 목록 [Sword]에 있음 -> 통과!
# 2. arthur.weapon 변수에 my_sword 객체가 저장됨.
arthur.equip_weapon(my_sword)  


# [상황 3] 공격하기 (위임: Delegation)
# 흐름:
# 1. char.py의 attack() 실행 -> 내부에서 self.job.attack() 호출
# 2. arthur.job은 Warrior 객체이므로, jobs.py의 Warrior.attack() 실행
# 3. 결과: "검을 휘둘러 벤다" 출력
arthur.attack()     


# [상황 4] 스킬 쓰기 (다형성)
# 흐름:
# 1. char.py의 use_skill() 실행 -> 내부에서 self.weapon.use_skill() 호출
# 2. arthur.weapon은 Sword 객체이므로, weapons.py의 Sword.use_skill() 실행
# 3. 결과: "무기 스킬 사용 Giant Hunt" 출력
arthur.use_skill()  



print("\n=== 🔮 마법사 멀린 테스트 ===")

# [상황 5] 마법사가 검을 들려고 함
# 흐름: Mage의 허용 목록은 [Wand]인데, Sword가 들어옴 -> "착용 불가" 출력
merlin.equip_weapon(my_sword)  

# [상황 6] 마법사가 지팡이를 듦
# 흐름: Mage의 허용 목록에 Wand가 있음 -> 성공 -> merlin.weapon에 my_wand 저장
merlin.equip_weapon(my_wand)   

# [상황 7] 마법사 공격
# 흐름: merlin.job은 Mage 객체 -> jobs.py의 Mage.attack() 실행
# 결과: "지팡이를 조준해 마법을 쏜다" 출력
merlin.attack()     

# [상황 8] 마법사 스킬
# 흐름: merlin.weapon은 Wand 객체 -> weapons.py의 Wand.use_skill() 실행
# 결과: "무기 스킬 사용 Comet" 출력
merlin.use_skill()

####
#🎓 핵심 요약 (이 코드로 배운 것)
# 합성 (Composition): Character 안에 Warrior나 Sword 객체를 부품처럼 끼워 넣어서 사용했습니다.
# 다형성 (Polymorphism): arthur.attack()과 merlin.attack()은 똑같은 코드를 호출하지만, 직업이 무엇이냐에 따라 전혀 다른 행동(대사)이 나옵니다.
# 타입 체크 (Type Check): type(new_weapon)을 통해 "이 객체가 어떤 설계도(Class)로 만들어졌는지" 확인하여 장착 가능 여부를 판단했습니다.
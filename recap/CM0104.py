class Device:
    def __init__(self, name):
        self.name = name
        self.is_on = False  # 기본은 꺼진 상태

    def turn_on(self):
        self.is_on = True
        print(f"[{self.name}] 전원이 켜졌습니다.")

    def turn_off(self):
        self.is_on = False
        print(f"[{self.name}] 전원이 꺼졌습니다.")

    def check_status(self):
        # 자식들이 고쳐 쓸(오버라이딩) 예정입니다.
        state = "ON" if self.is_on else "OFF"
        print(f"[{self.name}] 현재 상태: {state}")

# Device를 상속받음
class AirConditioner(Device):
    def __init__(self, name):
        super().__init__(name) # 부모의 __init__ (이름 설정) 실행
        self.temp = 24         # 나만의 속성

    def adjust_temp(self, temp):
        self.temp = temp
        print(f"[{self.name}] 희망 온도를 {temp}도로 설정합니다.")

    # 부모의 check_status를 덮어쓰기 (Overriding)
    def check_status(self):
        state = "ON" if self.is_on else "OFF"
        print(f"[{self.name}] 상태: {state} / 현재 온도: {self.temp}도")

class Light(Device):
    def __init__(self, name):
        super().__init__(name)
        self.brightness = 50

    def adjust_brightness(self, level):
        self.brightness = level
        print(f"[{self.name}] 밝기를 {level}로 조절합니다.")

    def check_status(self):
        state = "ON" if self.is_on else "OFF"
        print(f"[{self.name}] 상태: {state} / 밝기: {self.brightness}")

class TV(Device):
    def __init__(self, name):
        super().__init__(name)
        self.channel = 1

    def change_channel(self, num):
        self.channel = num
        print(f"[{self.name}] 채널을 {num}번으로 변경합니다.")
        
    def check_status(self):
        state = "ON" if self.is_on else "OFF"
        print(f"[{self.name}] 상태: {state} / 현재 채널: {self.channel}번")

class SmartHub:
    def __init__(self):
        self.devices = []  # 기기들을 저장할 빈 리스트

    # 기기 연결 (리스트에 추가)
    def connect_device(self, device):
        self.devices.append(device)
        print(f"✅ {device.name}이(가) 스마트 허브에 연결되었습니다.")

    # 전체 켜기 (반복문 활용)
    def turn_all_on(self):
        print("\n--- 모든 기기를 켭니다 ---")
        for device in self.devices:
            device.turn_on()

    # 전체 끄기
    def turn_all_off(self):
        print("\n--- 모든 기기를 끕니다 ---")
        for device in self.devices:
            device.turn_off()
            
    # 전체 상태 확인
    def show_all_status(self):
        print("\n--- 연결된 기기 상태 목록 ---")
        for device in self.devices:
            device.check_status() # 각자 오버라이딩된 메서드가 실행됨!

# 1. 기기(객체)들 생성
my_ac = AirConditioner("거실 에어컨")
my_light = Light("침실 조명")
my_tv = TV("안방 TV")

# 2. 허브 생성 및 연결
hub = SmartHub()
hub.connect_device(my_ac)
hub.connect_device(my_light)
hub.connect_device(my_tv)

# 3. 개별 기능 사용해보기 (잘 되는지 확인)
my_ac.adjust_temp(18)
my_tv.change_channel(11)

# 4. 허브로 중앙 제어
hub.turn_all_on()     # 전부 켜짐
hub.show_all_status() # 각자의 상태(온도, 채널 등)가 다르게 출력됨 (오버라이딩 효과)
hub.turn_all_off()    # 전부 꺼짐
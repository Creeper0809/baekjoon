import pyautogui

try:
    location = pyautogui.locateOnScreen('school2_1.jpg', confidence=0.7)
    if location:
        center = pyautogui.center(location)
        print(f"이미지 발견: 위치={location}, 중심={center}")
        pyautogui.moveTo(center)
    else:
        print("이미지를 찾을 수 없습니다.")
except pyautogui.ImageNotFoundException:
    print("이미지가 화면에서 감지되지 않았습니다.")
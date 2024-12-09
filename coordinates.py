import pyautogui
import time
try:
    while True:
        x, y = pyautogui.position()
        print(f"Mouse position: X={x}, Y={y}")
        time.sleep(1)
except KeyboardInterrupt:
    print("Exited...")

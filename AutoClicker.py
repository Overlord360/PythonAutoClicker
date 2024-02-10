import time
import pyautogui
from pynput import keyboard

class AutoClicker:
    def __init__(self, clicks, interval):
        self.clicks = clicks
        self.interval = interval
        self.running = True
        self.listener = keyboard.Listener(on_release=self.on_release)
        self.listener.start()

    def on_release(self, key):
        if key == keyboard.Key.esc:
            self.running = False
            return False

    def start_clicking(self):
        for i in range(self.clicks):
            if not self.running:
                break
            print(f'{i} out of {self.clicks}')
            pyautogui.click()
            time.sleep(self.interval)

print('3...')
time.sleep(1)
print('2...')
time.sleep(1)
print('1...')
time.sleep(1)
print('CLICK!')
auto_clicker = AutoClicker(1000000, 0.0001)
auto_clicker.start_clicking()
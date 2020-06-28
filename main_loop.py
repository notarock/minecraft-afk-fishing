from PIL import ImageGrab
import win32gui
import win32ui 
import time
import win32api, win32con


class main_loop(object):
    game_window = None

    def __init__(self, whnd):
        self.is_running = True
        self.game_window = whnd

    def click(self):
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,0,0,0,0)
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,0,0,0,0)

    def pixel_compare(pixel1, pixel2):
        pass

    def get_screen(self):
        rect = win32gui.GetWindowRect(self.game_window)
        img = ImageGrab.grab(bbox=rect)
        return img

    def run(self):
        while(self.is_running):
            img = self.get_screen();
            color = img.getpixel((660, 430))
            print(color)
            if 10 <= color[2] <= 45 and 10 <= color[1] <= 45 or 10 <= color[0] <= 45:
                self.click()
                time.sleep(1)
                self.click()
                time.sleep(3)
            del img
            time.sleep(1)

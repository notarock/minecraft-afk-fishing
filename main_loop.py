import PIL
import pyscreenshot as ImageGrab
import win32gui
import win32ui 

class main_loop(object):
    game_window = None

    def __init__(self, whnd):
        self.game_window = whnd

    def run(self):
        while(True):
            # print(self.game_window.getPixel(20,20))
            i_desktop_window_dc = win32gui.GetWindowDC(self.game_window)
            long_colour = win32gui.GetPixel(i_desktop_window_dc, 30, 30)
            print(long_colour)
            exit(0)
            
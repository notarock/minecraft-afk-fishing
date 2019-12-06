import win32gui
from main_loop import main_loop
from gui import App

""" 
Everything starts here
"""
def main():
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
    GUI()
    ## Get game window and start bot 
    #name = "Minecraft 1.14.4"
    #whnd = win32gui.FindWindow(None, name)
    #if not (whnd == 0):
    #  print('FOUND! initiating main loop')
    #  loop = main_loop(whnd)
    #  loop.run()
    #else:
    #    print("Could not find minecraft window. Is it even opened?")
    #    exit(0)

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import pyqtSlot
from PyQt5.Qt import *

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = "Notarock's Minecraft AFK Fishing"
        self.left = 10
        self.top = 10
        self.width = 200
        self.height = 100
        self.fishing_status = QLabel(self)
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        text = QLabel(self)
        text.setText("You are currently:")
        text.move(10, 10)
        
        self.fishing_status.move(10, 30)
        self.fishing_status.resize(100, 10)
        self.set_fishing()
        
        button_start = QPushButton('Start fishing', self)
        button_start.setToolTip('Click to start fishing')
        button_start.move(10,50)
        button_start.clicked.connect(self.start_fishing)


        button_stop = QPushButton('Stop fishing', self)
        button_stop.setToolTip('Click to stop fishing')
        button_stop.move(110,50)
        button_stop.clicked.connect(self.stop_fishing)
        
        self.location_on_the_screen()
        self.show()

    def location_on_the_screen(self):
        ag = QDesktopWidget().availableGeometry()
        sg = QDesktopWidget().screenGeometry()

        screen = QDesktopWidget().screenGeometry()
        widget = self.geometry()
        x = (screen.width() / 2) - widget.width()
        y = (screen.height() / 2) - widget.height()
        self.move(x, y)

    def set_fishing(self):
        self.fishing_status.setText("FISHING")
        self.fishing_status.setStyleSheet('color: green')

    def set_not_fishing(self):
        self.fishing_status.setText("NOT FISHING")
        self.fishing_status.setStyleSheet('color: red')

    @pyqtSlot()
    def start_fishing(self):
        print('Start fishing pressed')  
        self.set_fishing()
        
    @pyqtSlot()
    def stop_fishing(self):
        print('Stop fishing pressed')
        self.fishing_status.move(10, 30)
        self.set_not_fishing()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
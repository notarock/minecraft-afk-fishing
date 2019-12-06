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


import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import pyqtSlot
from PyQt5.Qt import *
from threading import Thread

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = "Notarock's Minecraft AFK Fishing"
        self.left = 10
        self.top = 10
        self.width = 200
        self.height = 125
        self.fishing_status = QLabel(self)
        self.main_loop = None
        self.background = None
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        text = QLabel(self)
        text.setText("You are currently:")
        text.move(10, 10)

        self.fishing_status.move(10, 30)
        self.fishing_status.resize(100, 10)
        self.set_not_fishing()

        text = QLabel(self)
        text.setText("Minecraft's window title:")
        text.move(10, 50)

        textbox = QLineEdit(self)
        textbox.move(10, 65)
        textbox.setText("Minecraft 1.14.4")
        
        button_start = QPushButton('Start fishing', self)
        button_start.setToolTip('Click to start fishing')
        button_start.move(110,90)
        button_start.clicked.connect(self.start_fishing)

        button_stop = QPushButton('Stop fishing', self)
        button_stop.setToolTip('Click to stop fishing')
        button_stop.move(10,90)
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
        print('Started fishing')  
        # Get game window and start bot 
        name = "Minecraft 1.14.4"
        whnd = win32gui.FindWindow(None, name)
        if not (whnd == 0):
            self.set_fishing()
            print('FOUND! initiating main loop')
            self.main_loop = main_loop(whnd)
            self.background = Thread(target = self.main_loop.run)
            self.background.start()
        else:
            print("Could not find minecraft window. Is it even opened?")
            exit(0)
        
    @pyqtSlot()
    def stop_fishing(self):
        print('Stopped fishing')
        self.fishing_status.move(10, 30)
        self.set_not_fishing()
        self.main_loop.is_running = False
        self.main_loop = None
        self.background = None

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
import win32gui
from main_loop import main_loop
from gyu import window

""" 
Everything starts here
"""
def main():
    window()

#    # Get game window and start bot 
#    whnd = win32gui.FindWindow(None, "Minecraft 1.14.4")
#    if not (whnd == 0):
#      print('FOUND! initiating main loop')
#      loop = main_loop(whnd)
#      loop.run()
#    else:
#        print("Could not find minecraft window. Is it even opened?")

"""
Only fun main() if current file is ran as entrypoint
"""
if __name__ == "__main__":
    main()
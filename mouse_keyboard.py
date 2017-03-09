import pyautogui
import time
import os


class mouse_control():
    '''
    Creating my own class for controlling the mouse
    '''

    def __init__(self):
        pyautogui.FAILSAFE = False
        self.size = pyautogui.size()
        self.x, self.y = pyautogui.position()

    def __str__(self):
        return self.current_position()

    def position_update(self):
        self.x, self.y = pyautogui.position()

    def continuous_current_position(self):
        clear = lambda: os.system('cls')
        try:
            while True:
                time.sleep(1)
                clear()
                x, y = pyautogui.position()
                print("Press Ctrl+C to Stop the Program")
                print("X: {}  Y: {}".format(x, y))
        except KeyboardInterrupt:
            clear()
            print("Program Stopped")

    @staticmethod
    def to_move_position(x,y):
        pyautogui.moveTo(x,y,duration=0.5)

    @staticmethod
    def rel_move_position(x,y):
        pyautogui.moveRel(x,y,duration=0.5)

    def current_position(self):
        self.position_update()
        return ("X: {}  Y: {}".format(self.x, self.y))


    def button_click(self,LorR = 'left', num_clicks = 1):
        self.position_update()
        pyautogui.click(x=self.x,y=self.y,button=LorR,clicks=num_clicks)


if __name__ == '__main__':
    Mouse1 = mouse_control()
    Mouse1.to_move_position(180,325)
    Mouse1.button_click()
    pyautogui.typewrite("John Reilly")
    Mouse1.to_move_position(180,390)
    Mouse1.button_click()
    pyautogui.typewrite("Never Achieving anything meaningful")
    Mouse1.to_move_position(180,450)
    Mouse1.button_click()
    Mouse1.to_move_position(180,550)
    Mouse1.button_click()
    Mouse1.to_move_position(375, 560)
    Mouse1.button_click()
    Mouse1.to_move_position(180,645)
    Mouse1.button_click()
    pyautogui.typewrite("This only took like 3 minutes to program")
    Mouse1.to_move_position(180,812)
    Mouse1.button_click()
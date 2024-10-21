import pyautogui as pg # pip install pyautogui, pillow
from time import sleep
import keyboard # pip install keyboard
import win32api, win32con

class Main:
    def __init__(
        self
    ):
        self.rgb = (255,  87,  34) # cores em formato rgb do alvo
        self.window_size = (275, 160, 800, 480) # dimensões da janela do jogo
        self.search_target
    
    def click(self, x: int, y: int):
        win32api.SetCursorPos((x,y)) # definindo a posição do cursor
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0) # clique do cursor
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0) # desclique do cursor
    
    @property
    def search_target(self):
        sleep(3) # espera para iniciar o jogo
        while keyboard.is_pressed('q') == False:
            pic = pg.screenshot(region=self.window_size) # capturando a janela

            width, height = pic.size # obtendo as dimenções da janela

            for x in range(0, width, 5):
                for y in range(0, height, 5):
                    r, g, b = pic.getpixel((x,y)) # extraindo a referencia das cores RGB

                    if b in range(self.rgb[2] - 2, self.rgb[2] + 2):
                        self.click(x + self.window_size[0], y + self.window_size[1])
                        sleep(0.05)
                        break

if __name__ == '__main__':
    Main()
import pyxel
import random

class App:
    def __init__(self):
        self.width = 160
        self.height = 160
        self.state = "start"
        pyxel.init(self.width, self.height)
        self.board = self.create_solvable_puzzle()
        self.tile_size = 160//3
        pyxel.mouse(True)
        pyxel.run(self.update, self.draw)
        
    def update(self):
        if not self.state == "play" and pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            self.state = "play"
            
    def draw(self):
        pyxel.cls(0)
        if self.state == "start":
            self.draw_start()
        if self.state == "start":
            self.draw_start()
        if self.state == "play":
            # self.draw_play()
            self.draw_bodo()
            
    def draw_start(self):
        pyxel.text(50, 60, "Click to start", pyxel.frame_count % 16)
    
    def draw_bodo(self):
        for y, row in enumerate(self.board):
            for x, tile in enumerate(row):
                if tile != 0:
                    pyxel.rect(x * self.tile_size, y * self.tile_size, self.tile_size, self.tile_size, 6)
                    pyxel.text(x * self.tile_size + self.tile_size//2, y * self.tile_size + self.tile_size//2, str(tile), 0)
                else:
                    pyxel.rect(x * self.tile_size, y * self.tile_size, self.tile_size, self.tile_size, 13)
                    
    def is_solvable(self, numbers):
        return True
    
    def create_solvable_puzzle(self):
        numbers = list(range(1, 9)) + [0]  # 1から8と空きスペースの0
        while True:
            random.shuffle(numbers)
            if self.is_solvable(numbers):
                break
        return [numbers[i:i+3] for i in range(0, 9, 3)]

App()

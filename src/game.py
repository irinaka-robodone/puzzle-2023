import pyxel
import random
import time
import json

class App:
    def __init__(self):
        self.width = 160
        self.empty_tile = (2, 2)
        self.clear_time = None
        self.height = 160
        self.state = "start"
        self.board_size = 3
        self.win = False
        self.ranking = self.load_keikazikan_from_file("out/rireki.txt")
        self.filename = "out/rireki.txt"
        pyxel.init(self.width, self.height, fps=60, title="数字パズル")
        self.start_time = pyxel.frame_count
        
        self.board = self.create_solvable_puzzle()
        x,y = 0,0
        for i in self.board:
            for j in i:
                if j==0:
                    
                    
                        8*410
                        
                        
                        self.empty_tile=(y,x)
                y +=1
            x +=1
            y=0
        print(self.board)
        self.tile_size = 50
        pyxel.mouse(True)
        self.start_time = pyxel.frame_count
        pyxel.run(self.update, self.draw)
        
    def update(self):
        if not self.state == "play" and pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            self.state = "play"
        if self.state == "play":
            self.elapsed_time = (pyxel.frame_count - self.start_time) // 60
            if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
                # マウスのクリック位置を取得
                mouse_x, mouse_y = pyxel.mouse_x, pyxel.mouse_y
                
                # クリックされたタイルの位置を計算
                tile_x, tile_y = int(mouse_x // self.tile_size), int(mouse_y // self.tile_size)
                print("empty->",self.empty_tile[0],self.empty_tile[1],"click",tile_x, tile_y)
                if self.is_adjacent(self.empty_tile, (tile_x, tile_y)):
                    print("ok")
                    # タイルを移動
                    self.move_tile(tile_x, tile_y)
                    if self.check_win():
                        self.win = True
                        self.state ="win"
                        self.ranking.append(self.keikazikann)
                        self.sebu()
        if self.state == "win":
            if pyxel.btnp(pyxel.KEY_SPACE):
                self.board_size += 1
                self.tile_size = int(self.tile_size * 3 / self.board_size)
                self.board = self.create_solvable_puzzle()
                self.state = "play"
    def sebu(self):
        with open(self.filename, "+a") as file:
            for time in self.ranking:
                file.write(f"{time}\n")
        
    def check_win(self):
        expected = list(range(1, 9)) + [0]
        flattened_board = [tile for row in self.board for tile in row]
        return flattened_board == expected
    # 画面をクリア
    
    def draw(self):
        pyxel.cls(0)
        if self.state == "start":
            self.draw_start()
        if self.state == "play":
            # self.draw_play()
            self.draw_bodo()
            self.keikazikann = int(time.time()-self.hazime)
            pyxel.text(0, 0, str(self.keikazikann), 3)
        if self.state == "win":
            self.draw_win()
            
            
            
    def draw_start(self):
        pyxel.text(50, 70, "suuzipazuruge-mu", pyxel.frame_count % 7)
        pyxel.text(50, 60, "Click to start", pyxel.frame_count % 16)
    
                    
    def is_adjacent(self, tile1, tile2):
        # タイルが隣接しているかをチェックする
        return (abs(tile1[0] - tile2[0]) == 1 and tile1[1] == tile2[1]) or \
            (abs(tile1[1] - tile2[1]) == 1 and tile1[0] == tile2[0])

    def move_tile(self, tile_x, tile_y):
        # タイルと空白スペースの位置を入れ替える
        self.board[self.empty_tile[1]][self.empty_tile[0]], self.board[tile_y][tile_x] = \
        self.board[tile_y][tile_x], self.board[self.empty_tile[1]][self.empty_tile[0]]
        
        self.empty_tile = (tile_x, tile_y)
    def is_solvable(self, numbers):
        return True
    
    def create_solvable_puzzle(self):
        numbers = list(range(1, self.board_size*self.board_size)) + [0]  # 1から8と空きスペースの0
        while True:
            random.shuffle(numbers)
            if self.is_solvable(numbers):
                break
        # tiles = list(range(1, 9)) + [0, 0, 0]
        # board = [tiles[i:i+4] for i in range(0, len(tiles), 4)]
        board = [numbers[i:i+self.board_size] for i in range(0, self.board_size*self.board_size, self.board_size)]
        
        for y, row in enumerate(board):
            for x, cell in enumerate(row):
                if cell == 0:
                    self.empty_tile = (int(x), int(y))
        
        self.hazime = time.time()
        return board

    def draw_win(self):
        pyxel.cls(13)
        pyxel.text(50, 60, "You Win!", pyxel.frame_count % 16)
        pyxel.text(60, 70, str(self.keikazikann), pyxel.frame_count % 16)
        pyxel.text(50, 70, "Ranking:", 7)
        for i, time in enumerate(self.ranking):
            pyxel.text(50, 80 + 10 * i, f"{i + 1}: {time:.2f}s", 7)
    def draw_bodo(self):
        for y, row in enumerate(self.board):
            for x, tile in enumerate(row):
                if tile != 0:
                    pyxel.rect(x * self.tile_size, y * self.tile_size, self.tile_size, self.tile_size, 11)
                    pyxel.text(x * self.tile_size + 25, y * self.tile_size + 25, str(tile), 7)
    def load_keikazikan_from_file(self, filename="ranking.txt"):
        try:
            with open(filename, "r") as file:
                ranking = [int(line.striip()) for line in file]
        except FileNotFoundError:
            ranking = []
            print("ranking not found!")
        return ranking
    
            
App()

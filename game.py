import pyxel
import random

class App:
    def __init__(self):
        self.width = 160
        self.empty_tile = (2, 2)
        self.height = 160
        self.state = "start"
        self.board_size = 3
        self.win = False
        pyxel.init(self.width, self.height, fps=60)
        self.board = self.create_solvable_puzzle()
        x,y = 0,0
        for i in self.board:
            for j in i:
                if j==0:
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
                tile_x, tile_y = mouse_x // self.tile_size, mouse_y // self.tile_size
                print("empty->",self.empty_tile[0],self.empty_tile[1],"click",tile_x, tile_y)
                if self.is_adjacent(self.empty_tile, (tile_x, tile_y)):
                    print("ok")
                    # タイルを移動
                    self.move_tile(tile_x, tile_y)
                    if self.check_win():
                        self.win = True
                        self.state ="win"
        if self.state == "win":
            self.board_size = 4
            if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
                self.board = self.create_solvable_puzzle()
                self.state = "play"
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
        if self.state == "win":
            self.draw_win()
            
            
    def draw_start(self):
        pyxel.text(50, 60, "Click to start", pyxel.frame_count % 16)
    
    def draw_bodo(self):
        for y, row in enumerate(self.board):
            for x, tile in enumerate(row):
                if tile != 0:
                    pyxel.rect(x * self.tile_size, y * self.tile_size, self.tile_size, self.tile_size, 11)
                    pyxel.text(x * self.tile_size + 25, y * self.tile_size + 25, str(tile), 7)
                    
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
        numbers = list(range(1, 9)) + [0]  # 1から8と空きスペースの0
        while True:
            random.shuffle(numbers)
            if self.is_solvable(numbers):
                break
        return [numbers[i:i+3] for i in range(0, 9, 3)]
    def draw_win(self):
        pyxel.text(50, 60, "You Win!", pyxel.frame_count % 16)
    def draw_bodo(self):
        for y, row in enumerate(self.board):
            for x, tile in enumerate(row):
                if tile != 0:
                    pyxel.rect(x * self.tile_size, y * self.tile_size, self.tile_size, self.tile_size, 11)
                    pyxel.text(x * self.tile_size + 25, y * self.tile_size + 25, str(tile), 7)
App()

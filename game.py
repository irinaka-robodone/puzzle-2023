import pyxel

class App:
    def __init__(self):
        self.width = 160
        self.height = 160
        self.state = "start"
        pyxel.init(self.width, self.height)
        pyxel.run(self.update, self.draw)
        
    def update(self):
        if self.state == "start":
            self.draw.start()
        if self.
        if self.state == "start":
            self.draw_start()
        if self.state == "play":
            self.draw_play()
    
    def draw_start(self):
        pyxel.text(50, 60, "Click to start", pyxel.frame_count % 16)
        
    
App()

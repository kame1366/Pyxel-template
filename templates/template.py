import pyxel

class App():

    def __init__(self) -> None:
        pyxel.init(100,100)
        pyxel.load()
        pyxel.run(self.update,self.draw)
    
    def update(self):
        pass
    def draw(self):
        pass
App()



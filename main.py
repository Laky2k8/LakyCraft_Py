import pyglet

pyglet.options["shadow_window"] = False
pyglet.options["debug_gl"] = False

import pyglet.gl as gl

class Window(pyglet.window.Window):
    def __init__(self, **args):
        super(Window,self).__init__(**args)

    def on_draw(self):
        gl.glClearColor(0.0,0.0,0.0,1.0)
        self.clear()

    def on_resize(self,width,height):
        print(f"Resize {width} * {height}")  # print out window size

class Game:
    def __init__(self):
        self.config = gl.Config(double_buffer=True, major_version=3)  # use modern opengl
        self.window = Window(config=self.config, width=800, height=600, caption="LakyCraft Python v1.0", resizable=True, vsync=False)  # vsync with pyglet causes problems on some computers, so disable it

    def run(self):
        pyglet.app.run()  # run our application


if __name__ == "__main__": # only run the game if source file is the one run
	game = Game() # create game object
	game.run()
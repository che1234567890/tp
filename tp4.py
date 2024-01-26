import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

COLORS = []

class balle:
    def __init__(self, x, y, change_x, change_y, rayon,color):
        self.x = x
        self.y = y
        self.change_x = change_x
        self.change_y = change_y
        self.rayon = rayon
        self.color = color

    def update(self, width, height):
        self.x += self.change_x
        self.y += self.change_y
        if self.x < 0 or self.x > width:
            self.change_x *= -1
        if self.y < 0 or self.y > height:
            self.change_y *= -1

    def draw(self):
        arcade.start_render()
        arcade.draw_circle_filled(self.x, self.y, self.rayon, self.color)

class rectangle:
    def __init__(self, x, y, change_x, change_y, width, height, color):
        self.x = x
        self.y = y
        self.change_x = change_x
        self.change_y = change_y
        self.width = width
        self.height = height
        self.color = color
    def update(self, width, height):
        self.x += self.change_x
        self.y += self.change_y
        if self.x < 0 or self.x > width:
            self.change_x *= -1
        if self.y < 0 or self.y > height:
            self.change_y *= -1

    def draw(self):
        arcade.start_render()
        arcade.draw_rectangle_filled(self.x, self.y, self.width, self.height, self.color)

class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Exercice #1")
        self.forme = []
    def setup(self):
        pass

    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            self.forme.append(balle(x, y, 2, 2, 20, arcade.color.RED))

        elif button == arcade.MOUSE_BUTTON_RIGHT:
            self.forme.append(rectangle(x, y, 3, 3, 40, 30, arcade.color.BLUE))


    def on_draw(self):
        arcade.start_render()

        for forme in self.forme:
            forme.draw()





    def on_update(self, delta_time):
        for forme in self.forme:
            forme.update(self.width, self.height)


def main():
    my_game = MyGame()
    my_game.setup()

    arcade.run()


main()


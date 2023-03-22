import arcade
import random
SW = 640
SH = 480
SPEED1 = 4
SPEED2 = 5

class Ball():
    def __init__(self,pos_x,pos_y,dx,dy,rad,hue,sound):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.dx = dx
        self.dy = dy
        self.rad = rad
        self.hue = hue
        self.sound = sound

    def draw_ball(self):
        arcade.draw_circle_filled(self.pos_x,self.pos_y,self.rad,self.hue)

    def update_ball(self):
        self.pos_x+=self.dx
        self.pos_y+=self.dy
        # bounce ball of edge of screen
        # if self.pos_x < self.rad or self.pos_x > SW-self.rad:
        #     self.dx*=-1
        # if self.pos_y < self.rad or self.pos_y > SH-self.rad:
        #     self.dy*=-1
        # stop ball at edge of screen
        if self.pos_x < self.rad:
            self.pos_x = self.rad
            arcade.play_sound(self.sound)
        if self.pos_x > SW - self.rad:
            self.pos_x = SW - self.rad
            arcade.play_sound(self.sound)
        if self.pos_y < self.rad:
            self.pos_y = self.rad
            arcade.play_sound(self.sound)
        if self.pos_y > SH - self.rad:
            self.pos_y = SH - self.rad
            arcade.play_sound(self.sound)

class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.AERO_BLUE)
        self.ball = Ball(50, 50, 0, 0, 15, arcade.color.RUBY, arcade.load_sound("laser.wav"))
        self.set_mouse_visible(False)
        self.ball2 = Ball(590, 430, 0, 0, 15, arcade.color.BALL_BLUE, arcade.load_sound("explosion.wav"))

        # self.ball_list=[]
        # for i in range (110):
        #     rad = random.randint(10, 30)
        #     x = random.randint(rad,SW-rad)
        #     y = random.randint(rad,SH-rad)
        #     dx = random.randint(-2,2)
        #     dy = random.randint(-2, 2)
        #     hue = (random.randint(200, 230),random.randint(0, 200),random.randint(50, 255))
        #     if dx == 0:
        #         dx = random.randint(1, 3)
        #     if dy == 0:
        #         dy = random.randint(1, 3)
        #     self.ball = Ball(x,y,dx,dy,rad,hue)
        #     self.ball_list.append(self.ball)
    def on_draw(self):
        arcade.start_render()
        self.ball.draw_ball()
        self.ball2.draw_ball()

    def on_update(self, dt):
        self.ball.update_ball()
        self.ball2.update_ball()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.ball.dx = -SPEED1
        elif key == arcade.key.RIGHT:
            self.ball.dx = SPEED1
        elif key == arcade.key.UP:
            self.ball.dy = SPEED1
        elif key == arcade.key.DOWN:
            self.ball.dy = -SPEED1

        if key == key == arcade.key.A:
            self.ball2.dx = -SPEED2
        elif key == key == arcade.key.D:
            self.ball2.dx = SPEED2
        elif key == key == arcade.key.W:
            self.ball2.dy = SPEED2
        elif key == key == arcade.key.S:
            self.ball2.dy = -SPEED2

    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.ball.dx = 0
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.ball.dy = 0

        if key == key == arcade.key.A or key == arcade.key.D:
            self.ball2.dx = 0
        if key == key == arcade.key.W or key == arcade.key.S:
            self.ball2.dy = 0



def main():
    window = MyGame(SW,SH,"User Control")
    arcade.run()

if __name__ == "__main__":
    main()
'''
USER CONTROL PROJECT
-----------------
Your choice!!! Have fun and be creative.
Create a background and perhaps animate some objects.
Pick a user control method and navigate an object around your screen.
Make your object more interesting than a ball.
Create your object with a new class.
Perhaps move your object through a maze or move the object to avoid other moving objects.
Incorporate some sound.
Type the directions to this project below:

DIRECTIONS:
----------
Please type directions for this game here.

'''
import arcade
import random

SW = 500
SH = 500
SPEED1 = 4
SPEED2 = 4
SPEED3 = 5
PULL = 3
PULL2 = 7
class line():
    def __init__(self, pos_x, pos_y, pos_x2, pos_y2, dx, dy, dx2, dy2, rad, hue):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.dx = dx
        self.dy = dy
        self.pos_x2 = pos_x2
        self.pos_y2 = pos_y2
        self.dx2 = dx2
        self.dy2 = dy2
        self.rad = rad
        self.hue = hue

    def draw_line(self):
        arcade.draw_line(self.pos_x,self.pos_y, self.pos_x2,self.pos_y2,self.hue,self.rad)

    def update_line(self):
        self.pos_x += self.dx
        self.pos_y += self.dy
        self.pos_x2 += self.dx2
        self.pos_y2 += self.dy2
        # bounce ball of edge of screen
        if self.pos_x < 0:
            self.dx *= -1
        if self.pos_x > SW:
            self.dx *= -1
        if self.pos_y < 0:
            self.dy *= -1
        if self.pos_y > SH:
            self.dy *= -1

        if self.pos_x2 < 0:
            self.dx2 *= -1
        if self.pos_x2 > SW:
            self.dx2 *= -1
        if self.pos_y2 < 0:
            self.dy2 *= -1
        if self.pos_y2 > SH:
            self.dy2 *= -1

class Ball():
    def __init__(self, pos_x, pos_y, dx, dy, rad, hue, sound):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.dx = dx
        self.dy = dy
        self.rad = rad
        self.hue = hue
        self.sound = sound
        self.tilt = 45
        self.sides = 4

    def draw_ball(self):
        arcade.draw_circle_filled(self.pos_x, self.pos_y, self.rad, self.hue, self.tilt, self.sides)

    def update_ball(self):
        self.pos_x += self.dx
        self.pos_y += self.dy
        # bounce ball of edge of screen
        # if self.pos_x < self.rad or self.pos_x > SW-self.rad:
        #     self.dx*=-1
        # if self.pos_y < self.rad or self.pos_y > SH-self.rad:
        #     self.dy*=-1
        #stop ball at edge of screen
        if self.pos_x < self.rad - 4:
            self.pos_x = self.rad - 4
            # arcade.play_sound(self.sound)
        if self.pos_x > SW - self.rad + 4:
            self.pos_x = SW - self.rad + 4
            # arcade.play_sound(self.sound)
        if self.pos_y < self.rad - 4:
            self.pos_y = self.rad - 4
            # arcade.play_sound(self.sound)
        if self.pos_y > SH - self.rad + 4:
            self.pos_y = SH - self.rad + 4
            # arcade.play_sound(self.sound)


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.AERO_BLUE)

        self.ball = Ball(450, 470, 0, 0, 15, arcade.color.BALL_BLUE, arcade.load_sound("laser.wav"))
        # self.set_mouse_visible(False)
        self.ball2 = Ball(450, 400, 0, 0, 15, arcade.color.RUBY, arcade.load_sound("explosion.wav"))
        self.ball3 = Ball(470, 10, 0, 0, 15, arcade.color.GREEN, arcade.load_sound("explosion.wav"))
        self.line = line(1,1,5,5,0,0,0,0,2,arcade.color.GOLD)
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
        arcade.draw_lrtb_rectangle_filled(0, 520, 450, 420, arcade.color.BLACK)
        arcade.draw_lrtb_rectangle_filled(190, 230, 500, 0, arcade.color.AERO_BLUE)
        arcade.draw_lrtb_rectangle_filled(230, 260, 450, 300, arcade.color.BLACK)
        arcade.draw_lrtb_rectangle_filled(260, 360, 330, 300, arcade.color.BLACK)
        arcade.draw_lrtb_rectangle_filled(330, 360, 380, 300, arcade.color.BLACK)
        arcade.draw_lrtb_rectangle_filled(360, 460, 380, 350, arcade.color.BLACK)
        arcade.draw_lrtb_rectangle_filled(430, 460, 380, 120, arcade.color.BLACK)
        arcade.draw_lrtb_rectangle_filled(430, 500, 80, 50, arcade.color.BLACK)
        arcade.draw_lrtb_rectangle_filled(0, 380, 80, 40, arcade.color.BLACK)
        arcade.draw_lrtb_rectangle_filled(330, 360, 260, 170, arcade.color.BLACK)
        arcade.draw_lrtb_rectangle_filled(0, 460, 150, 120, arcade.color.BLACK)
        arcade.draw_lrtb_rectangle_filled(330, 360, 120, 80, arcade.color.BLACK)
        arcade.draw_lrtb_rectangle_filled(330, 360, 190, 155, arcade.color.AERO_BLUE)
        arcade.draw_lrtb_rectangle_filled(260, 290, 160, 90, arcade.color.AERO_BLUE)
        arcade.draw_lrtb_rectangle_filled(50, 90, 100, 40, arcade.color.AERO_BLUE)
        arcade.draw_lrtb_rectangle_filled(230, 270, 70, 30, arcade.color.AERO_BLUE)

        arcade.draw_circle_filled(75,350,15,arcade.color.RED,0,5)
        arcade.draw_circle_filled(75, 220, 15, arcade.color.BLUE, 36, 5)
        self.line.draw_line()
        self.ball.draw_ball()
        self.ball2.draw_ball()
        self.ball3.draw_ball()


    def on_update(self, dt):
        self.ball.update_ball()
        self.ball2.update_ball()
        self.ball3.update_ball()
        self.line.update_line()
        if self.ball.pos_x == self.ball2.pos_x and self.ball.pos_y == self.ball2.pos_y:
            print("BLUE WINS")

        self.ball3.dy = -1
        # self.ball3.dy = self.ball2.dy *-1
        # self.ball3.dx = self.ball2.dx*-1
        if random.randint(0,10) == 0:
            self.ball3.dy = random.randint(-1,1)*SPEED3
            self.ball3.dx = random.randint(-1,1)*SPEED3
        # tie them together
        self.line.pos_x = self.ball.pos_x
        self.line.pos_y = self.ball.pos_y
        self.line.pos_x2 = self.ball2.pos_x
        self.line.pos_y2 = self.ball2.pos_y
        # keep them together
        if self.line.pos_x-self.line.pos_x2 > 75 :
            self.ball.pos_x = self.line.pos_x - PULL
        if self.line.pos_x - self.line.pos_x2 < -75:
            self.ball.pos_x = self.line.pos_x + PULL

        if self.line.pos_y-self.line.pos_y2 > 75 :
            self.ball.pos_y = self.line.pos_y -PULL
        if self.line.pos_y - self.line.pos_y2 < -75:
            self.ball.pos_y = self.line.pos_y + PULL

        if self.line.pos_x2 - self.line.pos_x > 75 :
            self.ball2.pos_x = self.line.pos_x2 -PULL
        if self.line.pos_x2 - self.line.pos_x < -75:
            self.ball2.pos_x = self.line.pos_x2 + PULL

        if self.line.pos_y2 - self.line.pos_y > 75 :
            self.ball2.pos_y = self.line.pos_y2 -PULL
        if self.line.pos_y2 - self.line.pos_y < -75:
            self.ball2.pos_y = self.line.pos_y2 + PULL
        # -----------------------
        if self.line.pos_x-self.line.pos_x2 > 150 :
            self.ball.pos_x = self.line.pos_x - PULL2
        if self.line.pos_x - self.line.pos_x2 < -150:
            self.ball.pos_x = self.line.pos_x + PULL2

        if self.line.pos_y-self.line.pos_y2 > 150 :
            self.ball.pos_y = self.line.pos_y -PULL2
        if self.line.pos_y - self.line.pos_y2 < -150:
            self.ball.pos_y = self.line.pos_y + PULL2

        if self.line.pos_x2 - self.line.pos_x > 150 :
            self.ball2.pos_x = self.line.pos_x2 -PULL2
        if self.line.pos_x2 - self.line.pos_x < -150:
            self.ball2.pos_x = self.line.pos_x2 + PULL2

        if self.line.pos_y2 - self.line.pos_y > 150 :
            self.ball2.pos_y = self.line.pos_y2 -PULL2
        if self.line.pos_y2 - self.line.pos_y < -150:
            self.ball2.pos_y = self.line.pos_y2 + PULL2



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
            self.ball2.dx = -SPEED1
        elif key == key == arcade.key.D:
            self.ball2.dx = SPEED1
        elif key == key == arcade.key.W:
            self.ball2.dy = SPEED1
        elif key == key == arcade.key.S:
            self.ball2.dy = -SPEED1

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
    window = MyGame(SW, SH, "User Control")
    arcade.run()


if __name__ == "__main__":
    main()
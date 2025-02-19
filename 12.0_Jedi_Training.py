'''
Sign your name:________________
 
Update the code in this chapter to do the following:
Open a 500px by 500px window.
Change the Ball class to a Box class.
Instantiate two 30px by 30px boxes. One red and one blue.
Make the blue box have a speed of 240 pixels/second
Make the red box have a speed of 180 pixels/second
Control the blue box with the arrow keys.
Control the red box with the WASD keys.
Do not let the boxes go off of the screen.
Incorporate different sounds when either box hits the edge of the screen.
Have two people play this TAG game at the same time.
The red box is always "it" and needs to try to catch the blue box.
When you're done demonstrate to your instructor!

'''
import arcade
import random
SW = 500
SH = 500
SPEED1 = 4
SPEED2 = 3

class Ball():
    def __init__(self,pos_x,pos_y,dx,dy,rad,hue,sound):
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
        arcade.draw_circle_filled(self.pos_x,self.pos_y,self.rad,self.hue,self.tilt,self.sides)

    def update_ball(self):
        self.pos_x+=self.dx
        self.pos_y+=self.dy
        # bounce ball of edge of screen
        # if self.pos_x < self.rad or self.pos_x > SW-self.rad:
        #     self.dx*=-1
        # if self.pos_y < self.rad or self.pos_y > SH-self.rad:
        #     self.dy*=-1
        # stop ball at edge of screen
        if self.pos_x < self.rad-4:
            self.pos_x = self.rad-4
            arcade.play_sound(self.sound)
        if self.pos_x > SW - self.rad+4:
            self.pos_x = SW - self.rad+4
            arcade.play_sound(self.sound)
        if self.pos_y < self.rad-4:
            self.pos_y = self.rad-4
            arcade.play_sound(self.sound)
        if self.pos_y > SH - self.rad+4:
            self.pos_y = SH - self.rad+4
            arcade.play_sound(self.sound)

class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.AERO_BLUE)
        self.ball = Ball(50, 50, 0, 0, 15, arcade.color.BALL_BLUE, arcade.load_sound("laser.wav"))
        # self.set_mouse_visible(False)
        self.ball2 = Ball(450, 450, 0, 0, 15, arcade.color.RUBY, arcade.load_sound("explosion.wav"))

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
        if self.ball.pos_x == self.ball2.pos_x and self.ball.pos_y == self.ball2.pos_y:
            print("BLUE WINS")
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
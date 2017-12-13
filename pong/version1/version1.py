# Pong Version 1
# In this game two users play ping pong by moving paddles
# vertically near the two screen edges.
# The ball is a small circle that bounces off the edges.
# If the ball hits the left edge, the right player scores a point
# and if the ball hits the right edge, the left player scores a
# point. The game ends when one player scores 11 points.
# The left player uses the q key to move the paddle up and the a
# key to move the paddle down. The right player uses the p key to
# move the paddle up and the l key to move the paddle down.

# V1 uses "Template - Events Algorithm" and implements a left paddle
# centered vertically, 100 pixels aways from the left edge of the window,
# a right paddle centered vertically and 100 pixels away from the right
# edge of the window and a moving ball that "wraps around" the edge of the
# the window
# - no scoreboard
# - no collision with the paddle
# - no handling of player actions
# - game runs until the player closes the window
import pygame, time
from pygame.locals import *
from uagame import Window


# User-defined functions

def main():
    window = Window('Pong', 500, 400)
    game = Game(window)
    game.play()
    window.close()


# User-defined classes

class Game:
    # An object in this class represents a complete game.

    def __init__(self, window):
        # Initialize a Game.
        # - self is the Game to initialize
        # - window is the uagame Window object
        self.window = window
        self.pause_time = 0.04  # smaller is faster game
        self.close_clicked = False
        self.continue_game = True
        self.fg_color = pygame.Color('white')
        surface = self.window.get_surface()
        surface_size = surface.get_size()
        # initialize left and right paddles
        center = [surface_size[0] // 2, surface_size[1] // 2]
        p_width = 10
        p_height = 40
        p_x_offset = 100
        p_y_offset = (surface_size[1] - p_height) // 2
        self.p_left = pygame.Rect(p_x_offset, p_y_offset, p_width, p_height)
        self.p_right = pygame.Rect(surface_size[0] - p_x_offset - p_width, p_y_offset, p_width, p_height)

        # initialize ball
        self.ball = Ball(self.fg_color, center, 5, [4, 1], surface)

    def play(self):
        # Play the game until the player presses the close box.
        # - self is the Game that should be continued or not

        while not self.close_clicked:  # until player clicks close box
            self.handle_event()
            self.draw()
            if self.continue_game:
                self.update()
                self.decide_continue()
            time.sleep(self.pause_time)  # set game velocity by pausing

    def handle_event(self):
        # Handle one user event by changing the game state
        # appropriately.
        # - self is the Game whose events will be handled

        event = pygame.event.poll()
        if event.type == QUIT:
            self.close_clicked = True

    def draw(self):
        # Draw all game objects.
        # - self is the Game to draw

        self.window.clear()
        self.ball.draw()
        surface = self.window.get_surface()
        pygame.draw.rect(surface, self.fg_color, self.p_left)
        pygame.draw.rect(surface, self.fg_color, self.p_right)
        self.window.update()

    def update(self):
        # Update the game objects.
        # - self is the Game to update

        self.ball.move()

    def decide_continue(self):
        # Check and remember if the game should continue
        # - self is the Game to check

        pass


class Ball:
    # An object in this class represents a colored circle
    # that can move on its own.

    def __init__(self, color, center, radius, velocity, surface):
        # Initialize a Ball.
        # - self is the Ball to initialize
        # - color is the pygame.Color of the Ball
        # - center is a list containing the x and y int
        # coords of the center of the Ball
        # - radius is the int pixel radius of the Ball
        # - velocity is a list containing the x and y int
        # components of the velocity of the Ball
        # - surface is the window's pygame.Surface object

        self.color = color
        self.center = center
        self.radius = radius
        self.velocity = velocity
        self.surface = surface

    def draw(self):
        # Draw the Ball on the surface.
        # - self is the Ball

        pygame.draw.circle(self.surface, self.color, self.center, self.radius)

    def move(self):
        # Change the location and the speed of the Ball so it
        # remains on the surface by bouncing from its edges.
        # - self is the Ball

        size = self.surface.get_size()
        for coord in range(0, 2):
            self.center[coord] = (self.center[coord] + self.velocity[coord]) % size[coord]


if __name__ == "__main__":
    window = Window('Pong', 500, 400)
    game = Game(window)
    game.play()
    window.close()

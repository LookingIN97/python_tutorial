import pygame, time
from pygame.locals import *
from uagame import Window


# User-defined functions

def main():
    window = Window('Pong', 500, 400)
    window.set_auto_update(False)
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
        self.pause_time = 0.02  # smaller is faster game
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

        # initialize the maximum score and the game score
        self.max_score = 11
        self.score = [0, 0]

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
        self.draw_score()
        surface = self.window.get_surface()
        pygame.draw.rect(surface, self.fg_color, self.p_left)
        pygame.draw.rect(surface, self.fg_color, self.p_right)
        self.window.update()

    def draw_score(self):
        # Draw the score.
        # - self is the Game

        self.window.set_font_size(72)

        # draw left score
        left_score = str(self.score[0])
        self.window.draw_string(left_score, 0, 0)

        # draw right score
        right_score = str(self.score[1])
        window_width = self.window.get_width()
        score_width = self.window.get_string_width(right_score)
        x_coord = window_width - score_width
        y_coord = 0
        self.window.draw_string(right_score, x_coord, 0)

    def update(self):
        # Update the game objects.
        # - self is the Game to update
        # move the ball
        # check edge and update score

        edge = self.ball.move(self.p_left, self.p_right)

        if edge == 'left':  # if left edge update the right score
            self.score[1] = self.score[1] + 1
        elif edge == 'right':  # if right edge update the left score
            self.score[0] = self.score[0] + 1

    def decide_continue(self):
        # Check and remember if the game should continue
        # - self is the Game to check
        if self.score[0] == self.max_score or self.score[1] == self.max_score:
            self.continue_game = False


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

    def move(self, left_paddle, right_paddle):
        # Change the location by the speed of the Ball
        # Bounces from the left paddle if ball is moving right to left
        # Bounces from the right paddle if ball is moving left to right
        # remains on the surface by bouncing from edges of the window.
        # Returns 'left' or 'right' if ball hits left edge or right edge
        # - self is the Ball
        # - left_paddle is pygame.Rect object that represents the left paddle
        # - right_paddle is pygame.Rect object that represents the right paddle.

        for coord in range(0, 2):
            self.center[coord] = self.center[coord] + self.velocity[coord]
            # Bounce the ball from the left paddle or right paddle
            self.paddle_collision(left_paddle, right_paddle)
            # Check which edge the ball has collided with
            edge = self.window_edge_collision(coord)
            if edge != '':  # check if ball collides with left or right edge
                return edge

    def window_edge_collision(self, coord):
        # Checks the edge of the window
        # Returns left or right depending on which edge the ball collided with
        # a black string otherwise
        # - self is the Ball
        # - coord is the x or y coord

        size = self.surface.get_size()
        edge = ''
        # check left or top
        if self.center[coord] < self.radius:
            self.velocity[coord] = - self.velocity[coord]
            if coord == 0:
                edge = 'left'
                # check right or bottom
        if self.center[coord] + self.radius > size[coord]:
            self.velocity[coord] = - self.velocity[coord]
            if coord == 0:
                edge = 'right'
        return edge

    def paddle_collision(self, left_paddle, right_paddle):
        # Reverse the x component of the Ball's velocity.
        # - self is the Ball to bounce
        # - left_paddle is the paddle the Ball bounces off
        # if travelling towards the left of the window
        # - right_paddle is the paddle the Ball bounces off
        # if travelling towards the right of the window

        if left_paddle.collidepoint(self.center) and self.velocity[0] < 0:
            self.velocity[0] = - self.velocity[0]
        if right_paddle.collidepoint(self.center) and self.velocity[0] > 0:
            self.velocity[0] = - self.velocity[0]


main()

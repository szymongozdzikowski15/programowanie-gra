import arcade
import os

class Obstacle(arcade.Sprite):
    """A moving obstacle sprite that represents a hazard on screen. Inherits from arcade.sprite"""

    shared_texture = None

    @classmethod
    def load_texture(cls):
        """Load the shared texture for all obstacle instances if not already loaded"""

        if cls.shared_texture is None:
            path = os.path.join("assets", "images", "szczur.png")
            cls.shared_texture = arcade.load_texture(path)

    def __init__(self, x, y, speed=200, width=0, height=0):
        """Initialize an Obstacle instance with position, speed, and optional scaling

        Args:
            x (float): Horizontal starting position
            y (float): Vertical starting position
            speed (float, optional): Horizontal movement speed in pixels per second. Defaults to 200
            width (int, optional): Target width for scaling (unused). Defaults to 0
            height (int, optional): Target height for scaling. Defaults to 0
        """

        if Obstacle.shared_texture is None:
            Obstacle.load_texture()

        super().__init__()

        self.texture = Obstacle.shared_texture
        scale = height / self.texture.height if height > 0 else 1.0
        self.scale = scale

        self.center_x = x
        self.center_y = y
        self.speed = speed

    def update(self, delta_time: float = 1 / 60):
        """Update the position of the obstacle based on time and speed

        Args:
            delta_time (float, optional): Time since last update. Defaults to 1/60
        """

        self.center_x -= self.speed * delta_time

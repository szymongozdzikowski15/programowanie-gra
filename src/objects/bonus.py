import arcade
import os

class Bonus(arcade.Sprite):
    """A collectible bonus sprite that moves horizontally across the screen"""

    shared_texture = None

    @classmethod
    def load_texture(cls):
        """Load the shared texture for all bonus instances if not already loaded"""

        if cls.shared_texture is None:
            path = os.path.join("assets", "images", "notes.png")
            cls.shared_texture = arcade.load_texture(path)

    def __init__(self, x, y, speed=1.0, lane_height=100):
        """Initialize a Bonus instance with position, speed, and scaling based on lane height

        Args:
            x (float): Horizontal starting position
            y (float): Vertical starting position
            speed (float, optional): Horizontal movement speed. Defaults to 1.0
            lane_height (int, optional): Height of the lane used to scale the sprite. Defaults to 100
        """

        if Bonus.shared_texture is None:
            Bonus.load_texture()

        super().__init__()

        self.texture = Bonus.shared_texture
        scale = lane_height / self.texture.height
        self.scale = scale

        self.center_x = x
        self.center_y = y
        self.speed = speed

    def update(self, delta_time: float = 1 / 60):
        """Update the position of the bonus based on time and speed

        Args:
            delta_time (float, optional): Time since last update. Defaults to 1/60
        """

        self.center_x -= self.speed * delta_time

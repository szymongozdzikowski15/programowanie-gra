import arcade
import os

class Obstacle:
    """
    Represents an obstacle object that moves from right to left and can collide with the player.
    """

    texture = None

    @classmethod
    def load_texture(cls):
        """
        Loads the obstacle texture once for all instances.
        """
        if cls.texture is None:
            texture_path = os.path.join("assets", "images", "szczur.png")
            cls.texture = arcade.load_texture(texture_path)

    def __init__(self, x, y, size=40, color=arcade.color.RED, speed=250):
        """
        Initialize the obstacle.

        Args:
            x (float): Initial horizontal position.
            y (float): Vertical position.
            size (int, optional): Width and height of the obstacle. Defaults to 40.
            color (tuple, optional): Color used (currently unused, texture overrides it). Defaults to arcade.color.RED.
            speed (float, optional): Speed in pixels per second moving left. Defaults to 250.
        """
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.speed = speed  # pixels per second, moving left
        self.texture = Obstacle.texture

    def update(self, delta_time):
        """
        Update the obstacle's position by moving it left.

        Args:
            delta_time (float): Time elapsed since last update.
        """
        self.x -= self.speed * delta_time

    def draw(self):
        """
        Draw the obstacle texture at the current position.
        """
        rect = arcade.rect.XYWH(
            self.x,
            self.y,
            self.size,
            self.size
        )
        arcade.draw_texture_rect(self.texture, rect)

    def collides_with(self, player):
        """
        Check if the obstacle collides with the player using AABB collision.

        Args:
            player (Player): The player object to check collision with.

        Returns:
            bool: True if colliding, False otherwise.
        """
        half_size = self.size / 2
        player_half = player.size / 2

        if (abs(self.x - player.x) < half_size + player_half and
            abs(self.y - player.y) < half_size + player_half):
            return True
        return False

import arcade
import os

class Bonus:
    """
    Represents a collectible bonus item that moves from right to left.
    """

    texture = None

    @classmethod
    def load_texture(cls):
        """
        Loads the bonus texture once for all instances.
        """
        if cls.texture is None:
            texture_path = os.path.join("assets", "images", "notes.png")
            cls.texture = arcade.load_texture(texture_path)

    def __init__(self, x, y, size=40, speed=250):
        """
        Initialize the bonus item.

        Args:
            x (float): Initial horizontal position.
            y (float): Vertical position.
            size (int, optional): Width and height of the bonus. Defaults to 40.
            speed (float, optional): Speed in pixels per second moving left. Defaults to 250.
        """
        self.x = x
        self.y = y
        self.size = size
        self.speed = speed
        self.texture = Bonus.texture

    def update(self, delta_time):
        """
        Update the bonus's position by moving it left.

        Args:
            delta_time (float): Time elapsed since last update.
        """
        self.x -= self.speed * delta_time

    def draw(self):
        """
        Draw the bonus texture at the current position.
        """
        rect = arcade.rect.XYWH(
            self.x,
            self.y,
            self.size,
            self.size,
        )
        arcade.draw_texture_rect(self.texture, rect)

    def collides_with(self, player):
        """
        Check if the bonus collides with the player using AABB collision.

        Args:
            player (Player): The player object to check collision with.

        Returns:
            bool: True if colliding, False otherwise.
        """
        half_size = self.size / 2
        player_half = player.size / 2
        return (abs(self.x - player.x) < half_size + player_half and
                abs(self.y - player.y) < half_size + player_half)

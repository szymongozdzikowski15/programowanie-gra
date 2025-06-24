import arcade
import os

class Player:
    """
    Represents the player character, which can move between lanes.
    """

    def __init__(self, lanes):
        """
        Initialize the player with the given lane positions.

        Args:
            lanes (tuple/list): A list or tuple of three y-coordinates representing bottom, middle, and top lanes.
        """
        self.tor_dol, self.tor_srodek, self.tor_gora = lanes
        self.current_lane = self.tor_srodek  # Start in the middle lane
        self.x = 100  # Fixed horizontal position

        avatar_path = os.path.join("assets", "images", "girl_avatar.png")
        self.texture = arcade.load_texture(avatar_path)

        self.scale = 0.2  # Scale factor for the sprite

        # Calculate width and height based on texture and scale
        self.width = self.texture.width * self.scale
        self.height = self.texture.height * self.scale

        # Use height as a general size for collision/hitbox purposes
        self.size = self.height

        # Vertical position corresponds to the current lane
        self.y = self.current_lane

    def move_up(self):
        """
        Move the player up one lane, if possible.
        """
        if self.current_lane == self.tor_dol:
            self.current_lane = self.tor_srodek
        elif self.current_lane == self.tor_srodek:
            self.current_lane = self.tor_gora

    def move_down(self):
        """
        Move the player down one lane, if possible.
        """
        if self.current_lane == self.tor_gora:
            self.current_lane = self.tor_srodek
        elif self.current_lane == self.tor_srodek:
            self.current_lane = self.tor_dol

    def update(self, delta_time):
        """
        Update the player's vertical position to match the current lane.

        Args:
            delta_time (float): Time elapsed since the last update (unused here).
        """
        self.y = self.current_lane

    def draw(self):
        """
        Draw the player's sprite at the current position.
        """
        rect = arcade.rect.XYWH(
            self.x,
            self.y,
            self.width,
            self.height,
        )
        arcade.draw_texture_rect(self.texture, rect)

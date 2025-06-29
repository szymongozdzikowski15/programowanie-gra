import arcade
import os

class Player(arcade.Sprite):
    """A controllable player character that moves vertically between lanes"""

    def __init__(self, lanes, lane_height):
        """Initialize the player with lane data and calculate position and scaling

        Args:
            lanes (list of float): Y-coordinates for each lane
            lane_height (float): Height of each lane used to scale the player sprite
        """

        super().__init__()

        self.lanes = lanes
        self.lane_height = lane_height
        self.current_lane = 1

        self.fixed_x = 100

        # Wczytaj teksturę ręcznie
        avatar_path = os.path.join("assets", "images", "girl_avatar.png")
        self.texture = arcade.load_texture(avatar_path)

        # Oblicz skalę na podstawie wysokości toru
        self.scale = lane_height / self.texture.height

        # Pozycjonowanie postaci
        self.center_x = self.fixed_x
        self.center_y = self.lanes[self.current_lane]

    def move_up(self):
        """Move the player up by one lane if not already in the top lane"""

        if self.current_lane < len(self.lanes) - 1:
            self.current_lane += 1
            self.center_y = self.lanes[self.current_lane]

    def move_down(self):
        """Move the player down by one lane if not already in the bottom lane"""

        if self.current_lane > 0:
            self.current_lane -= 1
            self.center_y = self.lanes[self.current_lane]

    def reset(self):
        """Reset the player position to the default lane and fixed X coordinate"""

        self.current_lane = 1
        self.center_y = self.lanes[self.current_lane]
        self.center_x = self.fixed_x

    

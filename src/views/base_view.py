import arcade
import os
from settings import SCREEN_WIDTH, SCREEN_HEIGHT 

class BaseView(arcade.View):
    """
    Base view class that provides a common background for all game views.
    """

    def __init__(self):
        """
        Initialize the view and load the background texture.
        """
        super().__init__()
        background_path = os.path.join("assets", "images", "city.png")
        self.background_texture = arcade.load_texture(background_path)

    def draw_background(self):
        """
        Draw the background texture covering the entire screen.
        """
        rect = arcade.Rect(
            left=0,
            right=SCREEN_WIDTH,
            bottom=0,
            top=SCREEN_HEIGHT,
            width=SCREEN_WIDTH,
            height=SCREEN_HEIGHT,
            x=SCREEN_WIDTH / 2,
            y=SCREEN_HEIGHT / 2
        )
        arcade.draw_texture_rect(self.background_texture, rect)

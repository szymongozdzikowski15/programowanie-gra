import arcade
import os
from views.base_view import BaseView
from settings import SCREEN_HEIGHT, SCREEN_WIDTH

class AboutView(arcade.View):
    """
    View displaying information about the author and the game.
    """

    def __init__(self):
        """
        Initialize the AboutView and load the background image.
        """
        super().__init__()
        background_path = os.path.join("assets", "images", "pwr.jpg")
        self.background_texture = arcade.load_texture(background_path)

    def on_draw(self):
        """
        Render the About screen, including background, overlay, title, and informational text.
        """
        self.clear()

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

        # Semi-transparent overlay rectangle
        arcade.draw_lrbt_rectangle_filled(
            left=50,
            right=self.window.width - 50,
            top=self.window.height - 50,
            bottom=50,
            color=(20, 20, 30, 90)
        )

        x = self.window.width // 2
        y = self.window.height - 150

        # Title
        arcade.draw_text("O autorze", x, y, arcade.color.ORANGE, 48, anchor_x="center")

        # Informational text lines
        info_lines = [
            "",
            "Gra napisana w Pythonie z użyciem biblioteki Arcade",
            "Autor: Szymon Goździkowski, Data: 2025",
            "Student matematyki stosowanej na PWr",
            "Projekt realizowany w ramach zadanka na laby z Programowania",
            "Moją — bardzo luźną — inspiracją była gra Urban Fatburner",
            "Miłego grania!",
            "",
            "",
            "",
            "Naciśnij ESC, aby wrócić do menu głównego"
        ]

        start_y = y - 80
        line_height = 30

        for i, line in enumerate(info_lines):
            arcade.draw_text(
                line,
                x,
                start_y - i * line_height,
                arcade.color.PINK,
                font_size=20,
                anchor_x="center"
            )

    def on_key_press(self, key, modifiers):
        """
        Handle key presses. Returns to the main menu if ESC is pressed.
        """
        if key == arcade.key.ESCAPE:
            from views.main_menu import MainMenuView
            self.window.show_view(MainMenuView())

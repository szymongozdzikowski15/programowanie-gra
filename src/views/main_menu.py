import arcade
import os
from settings import SCREEN_HEIGHT, SCREEN_WIDTH


class MainMenuView(arcade.View):
    """
    View displaying the main menu of the game

    Allows navigation to other views such as starting the game,
    reading the rules, adjusting difficulty, checking high scores,
    reading about the author, or exiting the game
    """
    def __init__(self):
        """Initialize main menu view with buttons and background."""
        super().__init__()
        self.buttons = [
            ("Start gry", SCREEN_HEIGHT - 200),
            ("Zasady gry", SCREEN_HEIGHT - 240),
            ("Poziom trudności", SCREEN_HEIGHT - 280),
            ("Najlepsze wyniki", SCREEN_HEIGHT - 320),
            ("O autorze", SCREEN_HEIGHT - 360),
            ("Zakończ", SCREEN_HEIGHT - 400),
        ]
        self.button_height = 35
        self.hovered_button_index = None
        background_path = os.path.join("assets", "images", "city.png")
        self.background_texture = arcade.load_texture(background_path)

    def on_show(self):
        """Play menu music when the main menu is shown."""

    def on_hide(self):
        """Called when the view is hidden; music stop removed."""
        pass

    def on_draw(self):
        """Draw background, title, and menu buttons with hover effect."""
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

        # Draw game title
        title = arcade.Text(
            "Wrocław City Girl",
            self.window.width // 2,
            SCREEN_HEIGHT - 100,
            arcade.color.ORANGE,
            font_size=40,
            anchor_x="center",
            anchor_y="bottom"
        )
        title.draw()

        # Draw menu buttons
        for index, (text, y) in enumerate(self.buttons):
            x = self.window.width // 2
            color = arcade.color.DARK_PINK if self.hovered_button_index == index else arcade.color.PINK

            button_text = arcade.Text(
                text,
                x,
                y,
                color,
                font_size=24,
                anchor_x="center",
                anchor_y="bottom"
            )
            button_text.draw()

    def on_mouse_motion(self, x, y, dx, dy):
        """Track mouse movement to update which button is hovered."""
        self.hovered_button_index = None
        for index, (text, y_pos) in enumerate(self.buttons):
            x_center = self.window.width // 2
            font_size = 24

            # Create a text object to get its dimensions
            text_obj = arcade.Text(text, x_center, y_pos, font_size=font_size, anchor_x="center", anchor_y="bottom")
            text_width = text_obj.content_width
            text_height = text_obj.content_height

            left = x_center - text_width / 2
            right = x_center + text_width / 2
            bottom = y_pos
            top = y_pos + text_height

            if left <= x <= right and bottom <= y <= top:
                self.hovered_button_index = index
                break

    def on_mouse_press(self, x, y, button, modifiers):
        """Handle mouse clicks on buttons to trigger corresponding actions."""
        if self.hovered_button_index is None:
            return

        option = self.buttons[self.hovered_button_index][0]

        if option == "Start gry":
            from views.game import GameView
            game_view = GameView()
            game_view.setup()
            self.window.show_view(game_view)
        elif option == "Zasady gry":
            from views.rules import RulesView
            self.window.show_view(RulesView())
        elif option == "Poziom trudności":
            from views.configuration import ConfigurationView
            self.window.show_view(ConfigurationView())
        elif option == "Najlepsze wyniki":
            from views.scores import ScoresView
            scores_view = ScoresView()
            self.window.show_view(scores_view)
        elif option == "O autorze":
            from views.about import AboutView
            self.window.show_view(AboutView())
        elif option == "Zakończ":
            arcade.close_window()

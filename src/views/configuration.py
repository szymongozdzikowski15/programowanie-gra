import arcade
import settings
from views.base_view import BaseView
from settings import SCREEN_HEIGHT, SCREEN_WIDTH

class ConfigurationView(BaseView):
    """
    View for configuring the game difficulty level.

    Allows the player to select between "Łatwy" (Easy) and "Trudny" (Hard) difficulty modes,
    either by clicking on buttons or pressing keys 1 or 2.
    Displays relevant descriptions and instructions.
    """

    def __init__(self):
        """
        Initialize the ConfigurationView.

        Sets up positions and dimensions for two difficulty buttons ("Łatwy" and "Trudny").
        Buttons are horizontally centered and placed near the top part of the screen.
        """
        super().__init__()

        button_width = 120
        button_height = 50
        button_bottom = SCREEN_HEIGHT - 230
        gap = 40

        left_easy = SCREEN_WIDTH // 2 - button_width - gap // 2
        right_easy = left_easy + button_width
        top_easy = button_bottom + button_height

        left_hard = SCREEN_WIDTH // 2 + gap // 2
        right_hard = left_hard + button_width
        top_hard = button_bottom + button_height

        # Store button rectangles as tuples (left, right, bottom, top)
        self.easy_button = (left_easy, right_easy, button_bottom, top_easy)
        self.hard_button = (left_hard, right_hard, button_bottom, top_hard)

    def on_show(self):
        """
        Called when this view is shown.

        Sets the background color to white.
        """
        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        """
        Render the configuration screen.

        Draws:
        - Semi-transparent dark rectangle as background panel.
        - Title and subtitle texts.
        - Two difficulty buttons with different colors indicating selection.
        - Descriptions explaining differences between difficulties.
        - Instructions on how to select difficulty.
        - Reminder about pressing ESC to return to the main menu.
        """
        self.clear()
        self.draw_background()

        # Draw semi-transparent dark panel
        arcade.draw_lrbt_rectangle_filled(
            left=40,
            right=self.window.width - 40,
            bottom=40,
            top=self.window.height - 60,
            color=(20, 20, 30, 180)
        )

        # Title
        arcade.draw_text(
            "Konfiguracja",
            self.window.width // 2,
            self.window.height - 100,
            arcade.color.ORANGE,
            40,
            anchor_x="center"
        )

        # Subtitle
        arcade.draw_text(
            "Wybierz poziom trudności:",
            self.window.width // 2,
            self.window.height - 160,
            arcade.color.PINK,
            25,
            anchor_x="center"
        )

        # Button colors depend on selected difficulty
        easy_color = arcade.color.FOREST_GREEN if settings.difficulty == "Łatwy" else arcade.color.DARK_GREEN
        hard_color = arcade.color.FIREBRICK if settings.difficulty == "Trudny" else arcade.color.BLACK_BEAN

        # Draw difficulty buttons
        arcade.draw_lrbt_rectangle_filled(*self.easy_button, easy_color)
        arcade.draw_lrbt_rectangle_filled(*self.hard_button, hard_color)

        arcade.draw_lrbt_rectangle_outline(*self.easy_button, arcade.color.BLACK, 2)
        arcade.draw_lrbt_rectangle_outline(*self.hard_button, arcade.color.BLACK, 2)

        # Draw button labels centered
        easy_center_x = (self.easy_button[0] + self.easy_button[1]) / 2
        easy_center_y = (self.easy_button[2] + self.easy_button[3]) / 2

        hard_center_x = (self.hard_button[0] + self.hard_button[1]) / 2
        hard_center_y = (self.hard_button[2] + self.hard_button[3]) / 2

        arcade.draw_text("Łatwy", easy_center_x, easy_center_y - 12, arcade.color.PINK, 24, anchor_x="center")
        arcade.draw_text("Trudny", hard_center_x, hard_center_y - 12, arcade.color.PINK, 24, anchor_x="center")

        # Description text lines explaining the "Trudny" difficulty
        description_lines = [
            "Poziom trudny sprawia, że przedmioty poruszają się",
            "szybciej, jest je więc trudniej ominąć oraz generuje",
            "się więcej przeszkód niż na poziomie łatwym."
        ]

        start_y_desc = self.window.height - 300
        for i, line in enumerate(description_lines):
            arcade.draw_text(line, self.window.width // 2, start_y_desc - i * 25, arcade.color.PINK, 18, anchor_x="center")

        # Instruction lines for changing difficulty
        info_lines = [
            "Kliknij myszką na poziom lub naciśnij 1 lub 2,",
            "aby zmienić poziom trudności."
        ]

        start_y_info = 130
        for i, line in enumerate(info_lines):
            arcade.draw_text(line, self.window.width // 2, start_y_info - i * 20, arcade.color.PINK, 16, anchor_x="center")

        # Instruction to return to menu
        arcade.draw_text("Naciśnij ESC, aby wrócić do menu.", self.window.width // 2, 50, arcade.color.PINK, 16, anchor_x="center")

    def on_mouse_press(self, x, y, button, modifiers):
        """
        Handle mouse clicks.

        If the click is inside the "Łatwy" button rectangle, set difficulty to "Łatwy".
        If inside the "Trudny" button rectangle, set difficulty to "Trudny".

        Args:
            x (int): Mouse X coordinate.
            y (int): Mouse Y coordinate.
            button (int): Mouse button pressed.
            modifiers (int): Modifier keys pressed.
        """
        if self._point_in_rect(x, y, *self.easy_button):
            settings.difficulty = "Łatwy"
            self.window.clear()
            self.on_draw()
        elif self._point_in_rect(x, y, *self.hard_button):
            settings.difficulty = "Trudny"
            self.window.clear()
            self.on_draw()

    def on_key_press(self, key, modifiers):
        """
        Handle key presses.

        Pressing 1 sets difficulty to "Łatwy".
        Pressing 2 sets difficulty to "Trudny".
        Pressing ESC returns to the main menu.

        Args:
            key (int): The key pressed.
            modifiers (int): Modifier keys pressed.
        """
        if key == arcade.key.KEY_1:
            settings.difficulty = "Łatwy"
            self.window.clear()
            self.on_draw()
        elif key == arcade.key.KEY_2:
            settings.difficulty = "Trudny"
            self.window.clear()
            self.on_draw()
        elif key == arcade.key.ESCAPE:
            from views.main_menu import MainMenuView
            self.window.show_view(MainMenuView())

    def _point_in_rect(self, px, py, left, right, bottom, top):
        """
        Utility method to check if a point (px, py) lies inside a rectangle defined by (left, right, bottom, top).

        Args:
            px (float): X coordinate of the point.
            py (float): Y coordinate of the point.
            left (float): Left boundary of the rectangle.
            right (float): Right boundary of the rectangle.
            bottom (float): Bottom boundary of the rectangle.
            top (float): Top boundary of the rectangle.

        Returns:
            bool: True if point is inside the rectangle, False otherwise.
        """
        return left <= px <= right and bottom <= py <= top

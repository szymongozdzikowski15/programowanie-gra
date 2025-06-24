import arcade
from views.base_view import BaseView

class RulesView(BaseView):
    def on_show(self):
        """Set background color when the view is shown."""
        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        """Render the rules screen with instructions and background."""
        self.clear()
        self.draw_background()
        arcade.draw_lrbt_rectangle_filled(
            left=50,
            right=self.window.width - 50,
            top=self.window.height - 50,
            bottom=50,
            color=(20, 20, 30, 180)
        )

        arcade.draw_text("Game Rules", self.window.width // 2, self.window.height - 100,
                         arcade.color.ORANGE, 40, anchor_x="center")

        rules = [
            "Control the character moving between three lanes",
            "of Wrocław City urban space.",
            "Collect student notes to earn points",
            "and avoid ubiquitous rats.",
            "You need to hurry and pass the exam.",
            "Movement speed gradually increases.",
            "You have limited lives, so be careful!",
            "Good luck :)"
        ]

        start_y = self.window.height - 160
        for i, line in enumerate(rules):
            arcade.draw_text(line, self.window.width // 2, start_y - i * 30,
                             arcade.color.PINK, 20, anchor_x="center")

        arcade.draw_text("Press ESC to return to menu",
                         self.window.width // 2, 50,
                         arcade.color.LIGHT_PINK, 15, anchor_x="center")

    def on_key_press(self, key, modifiers):
        """Handle key press events.

        Args:
            key (int): The key code pressed.
            modifiers (int): Modifier keys pressed (Shift, Ctrl, etc.).
        """
        if key == arcade.key.ESCAPE:
            from views.main_menu import MainMenuView  # Local import to avoid circular dependency
            self.window.show_view(MainMenuView())

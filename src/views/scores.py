import arcade
from views.base_view import BaseView
import score_manager

class ScoresView(BaseView):
    """
    View displaying the list of high scores stored in the game

    Loads scores from file and shows them on the screen, with an option to return to the main menu using ESC
    """
    def __init__(self):
        """Initialize ScoresView and prepare an empty scores list."""
        super().__init__()
        self.scores = []
        self._scores_loaded = False

    def on_draw(self):
        """Render the scores screen with background and scores list."""
        self.clear()
        self.draw_background()

        if not self._scores_loaded:
            self.scores = score_manager.load_scores()
            self._scores_loaded = True

        arcade.draw_lrbt_rectangle_filled(
            left=50,
            right=self.window.width - 50,
            top=self.window.height - 50,
            bottom=50,
            color=(20, 20, 30, 180)
        )
        arcade.draw_text("Najlepsze Wyniki", self.window.width // 2, self.window.height - 100,
                         arcade.color.ORANGE, 40, anchor_x="center")

        if not self.scores:
            arcade.draw_text("Brak wyników", self.window.width // 2, self.window.height // 2,
                             arcade.color.GRAY, 20, anchor_x="center")
        else:
            start_y = self.window.height - 160
            for i, entry in enumerate(self.scores):
                y = start_y - i * 30
                text = f"{i+1}. {entry['score']} pkt – {entry['difficulty']} – {entry['date']}"
                arcade.draw_text(text, self.window.width // 2, y,
                                arcade.color.PINK, 20, anchor_x="center")

        arcade.draw_text("Naciśnij ESC, aby wrócić do menu", self.window.width // 2, 50,
                            arcade.color.LIGHT_PINK, 15, anchor_x="center")
        
    def on_key_press(self, key, modifiers):
        """Handle key press events to navigate back to the main menu.

        Args:
            key (int): The key code pressed.
            modifiers (int): Modifier keys pressed (Shift, Ctrl, etc.).
        """
        if key == arcade.key.ESCAPE:
            from views.main_menu import MainMenuView
            self.window.show_view(MainMenuView())

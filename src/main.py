import arcade
from views.main_menu import MainMenuView

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Wrocław City Girl"

def main():
    """
    Create the game window, set the main menu view, and start the Arcade event loop.
    """
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    menu_view = MainMenuView()
    window.show_view(menu_view)
    arcade.run()

if __name__ == "__main__":
    main()

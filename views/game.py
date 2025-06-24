import arcade
import random
import os
import math
import settings
from objects.player import Player
from objects.obstacle import Obstacle
from objects.bonus import Bonus
import score_manager
from settings import SCREEN_HEIGHT, SCREEN_WIDTH

SOUND_FOLDER = os.path.join("assets", "sounds")


class GameView(arcade.View):
    def __init__(self):
        """
        Initialize the game view, load textures, create player and lanes,
        set up initial game state and sounds.
        """
        super().__init__()
        # Load background and player
        # Setup lanes and lane colors
        # Initialize obstacles, bonuses, timers, score, lives, and UI elements
        # Load sound effects
        # Initialize game over state and menu button parameters

    def setup(self):
        """
        Configure game parameters depending on difficulty level,
        such as object speed, spawn intervals, and speed increments.
        """
        Obstacle.load_texture()
        Bonus.load_texture()
        if settings.difficulty == "Łatwy":
            # Easy difficulty settings
            pass
        else:
            # Hard difficulty settings
            pass
        self.time_since_speed_increase = 0

    def on_show(self):
        """
        Called when the view is shown, runs setup.
        """
        self.setup()

    def is_too_close(self, x, y, objects, min_distance=50):
        """
        Check if the position (x, y) is too close to any object in the list.

        Args:
            x (float): X coordinate.
            y (float): Y coordinate.
            objects (list): List of objects with x and y attributes.
            min_distance (float): Minimum allowed distance.

        Returns:
            bool: True if too close to any object, False otherwise.
        """
        for obj in objects:
            dist = math.hypot(x - obj.x, y - obj.y)
            if dist < min_distance:
                return True
        return False

    def on_update(self, delta_time):
        """
        Update game state each frame.

        Handles:
        - Game over delay and sound.
        - Speed increase over time.
        - Player movement update.
        - Spawning obstacles and bonuses.
        - Moving obstacles and bonuses.
        - Collision detection and score/lives update.
        """
        if self.game_over and not self.loss_sound_played:
            # Play loss sound after short delay
            pass

        if self.game_over:
            return

        # Increase speed gradually, decrease increment over time, play speed sound
        # Update player position
        # Spawn obstacles and bonuses at intervals, avoiding overlap
        # Move obstacles and bonuses leftwards
        # Remove offscreen obstacles and bonuses
        # Handle collisions: lose life on obstacle hit, gain points on bonus
        # Play sounds on events, update game over and score

    def on_draw(self):
        """
        Render the game screen.

        Draws:
        - Background city texture.
        - Colored lanes with lines.
        - Player, obstacles, bonuses.
        - Score and remaining lives as hearts.
        - Game over screen and menu button if game ended.
        """
        self.clear()
        # Draw background and lanes with colors and lines
        # Draw player, obstacles, bonuses
        # Draw score text
        # Draw lives as heart textures
        # If game over, draw translucent overlay, text, and menu button

    def on_key_press(self, key, modifiers):
        """
        Handle key presses for player movement.

        Args:
            key: Key pressed.
            modifiers: Modifier keys pressed.
        """
        if key == arcade.key.UP:
            self.player.move_up()
        elif key == arcade.key.DOWN:
            self.player.move_down()

    def on_mouse_press(self, x, y, button, modifiers):
        """
        Handle mouse clicks.

        If game over, check if menu button was clicked and return to main menu.

        Args:
            x (int): Mouse x position.
            y (int): Mouse y position.
            button: Mouse button pressed.
            modifiers: Modifier keys pressed.
        """
        if self.game_over:
            # Check if menu button clicked and show main menu view
            pass
        else:
            pass

import arcade
import random
import os
import math
import settings
import score_manager
from objects.player import Player
from objects.obstacle import Obstacle
from objects.bonus import Bonus
from views.main_menu import MainMenuView
from settings import SCREEN_HEIGHT, SCREEN_WIDTH

SOUND_FOLDER = os.path.join("assets", "sounds")

class GameView(arcade.View):
    """Main gameplay view where the player avoids obstacles and collects bonuses."""

    def __init__(self):
        """Initialize the game view, including background, player, lanes, obstacles, bonuses, sounds and UI elements"""

        super().__init__()
        self.game_over = False
        self.loss_sound_played = False

        self.background = arcade.load_texture("assets/images/city1.png")
        self.lane_count = 3
        self.lane_height = int((1 / 2) * SCREEN_HEIGHT // self.lane_count)
        self.lanes = [self.lane_height // 2 + i * self.lane_height for i in range(self.lane_count)]
        self.player = Player(self.lanes, self.lane_height)
        self.player_list = arcade.SpriteList()
        self.player_list.append(self.player)

        self.obstacle_list = arcade.SpriteList()
        self.bonus_list = arcade.SpriteList()

        self.obstacle_timer = 0
        self.bonus_timer = 0
        self.obstacle_interval = 2.0
        self.bonus_interval = 5.0

        self.speed = 3
        self.max_speed = 8
        self.speed_increment = 0.2

        self.score = 0
        self.lives = 3
        self.next_score_sound_threshold = 100

        self.heart_texture = arcade.load_texture("assets/images/heart.png")

        self.loss_sound = arcade.load_sound(os.path.join(SOUND_FOLDER, "loss.wav"))
        self.notes_sound = arcade.load_sound(os.path.join(SOUND_FOLDER, "coin1.wav"))
        self.rat_sound = arcade.load_sound(os.path.join(SOUND_FOLDER, "burger.wav"))
        self.speed_up_sound = arcade.load_sound(os.path.join(SOUND_FOLDER, "speed.wav"))
        self.triumph_sound = arcade.load_sound(os.path.join(SOUND_FOLDER, "triumph.wav"))

        self.menu_button_x = SCREEN_WIDTH // 2
        self.menu_button_y = SCREEN_HEIGHT // 2 - 100
        self.menu_button_width = 200
        self.menu_button_height = 50

    def setup(self):
        """Configure or reset game state depending on difficulty level and initialize gameplay variables"""

        Obstacle.load_texture()
        Bonus.load_texture()
        if settings.difficulty == "Łatwy":
            self.speed = 400
            self.max_speed = 700
            self.speed_increment = 50
            self.obstacle_interval = 1.8
            self.bonus_interval = 3.5
        else:
            self.speed = 600
            self.max_speed = 1000
            self.speed_increment = 75
            self.obstacle_interval = 1.2
            self.bonus_interval = 4.0

        #losowy rozrzut czasowy
        self.next_obstacle_time = self.obstacle_interval + random.uniform(-0.3, 0.3)
        self.next_bonus_time = self.bonus_interval + random.uniform(-0.5, 0.5)
        self.base_obstacle_interval = self.obstacle_interval

        self.time_since_speed_increase = 0
        self.score = 0
        self.lives = 3

        self.player.reset()
        self.player_list = arcade.SpriteList()
        self.player_list.append(self.player)

    def on_show(self):
        """Called when this view is shown; sets up the game"""

        self.setup()

    def is_too_close(self, x, y, objects, min_distance=50):
        """Check if a new object at (x, y) is too close to any existing object

        Args:
            x (float): X coordinate of the new object
            y (float): Y coordinate of the new object
            objects (Iterable[arcade.Sprite]): List of existing objects to compare with
            min_distance (int, optional): Minimum allowed distance. Defaults to 50.

        Returns:
            bool: True if an object is too close, False otherwise
        """

        for obj in objects:
            dist = math.hypot(x - obj.center_x, y - obj.center_y)
            if dist < min_distance:
                return True
        return False

    def on_update(self, delta_time):
        """Update game logic including player, obstacles, bonuses, speed progression, collisions and scoring

        Args:
            delta_time (float): Time passed since the last update
        """

        if self.game_over and not self.loss_sound_played:
            arcade.play_sound(self.loss_sound)
            self.loss_sound_played = True
            score_manager.add_score(self.score, settings.difficulty)
            return

        if self.game_over:
            return

        self.time_since_speed_increase += delta_time
        if self.time_since_speed_increase >= 15:
            self.speed = min(self.speed + self.speed_increment, self.max_speed)
            arcade.play_sound(self.speed_up_sound)
            self.time_since_speed_increase = 0

        self.player.update(delta_time)
        current_speed = self.speed

        # Dynamiczne zmniejszanie odstępu między przeszkodami wraz z wynikiem
        min_obstacle_interval = 0.6  # minimalny odstęp
        self.obstacle_interval = max(self.base_obstacle_interval - (self.score // 100) * 0.2, min_obstacle_interval)

        self.next_obstacle_time -= delta_time
        if self.next_obstacle_time <= 0:
            self.next_obstacle_time = self.obstacle_interval + random.uniform(-0.3, 0.3)

            lane = random.randint(0, self.lane_count - 1)
            y = self.lanes[lane]
            new_x = SCREEN_WIDTH + 40
            if not self.is_too_close(new_x, y, list(self.obstacle_list) + list(self.bonus_list), min_distance=80):
                obstacle = Obstacle(new_x, y, speed=current_speed, height=self.lane_height * 0.5)
                self.obstacle_list.append(obstacle)

                # 33% szans na podwójną przeszkodę w innym pasie
                if random.random() < 0.33:
                    other_lane = (lane + random.choice([1, 2])) % self.lane_count
                    y2 = self.lanes[other_lane]
                    if not self.is_too_close(new_x + 60, y2, self.obstacle_list, min_distance=80):
                        obstacle2 = Obstacle(new_x + 60, y2, speed=current_speed, height=self.lane_height * 0.5)
                        self.obstacle_list.append(obstacle2)

        self.next_bonus_time -= delta_time
        if self.next_bonus_time <= 0:
            self.next_bonus_time = self.bonus_interval + random.uniform(-0.5, 0.5)

            lane = random.randint(0, self.lane_count - 1)
            y = self.lanes[lane]
            new_x = SCREEN_WIDTH + 40
            if not self.is_too_close(new_x, y, list(self.obstacle_list) + list(self.bonus_list), min_distance=120):
                bonus = Bonus(new_x, y, speed=current_speed, lane_height=self.lane_height * 0.5)
                self.bonus_list.append(bonus)

        # Aktualizacja przeszkód i bonusów
        for obstacle in self.obstacle_list:
            obstacle.update(delta_time)

        for bonus in self.bonus_list:
            bonus.update(delta_time)

        # Usuwanie przeszkód poza ekranem
        for obstacle in self.obstacle_list[:]:
            if obstacle.right < 0:
                self.obstacle_list.remove(obstacle)

        for bonus in self.bonus_list[:]:
            if bonus.center_x < -bonus.width:
                self.bonus_list.remove(bonus)

        # Kolizje z przeszkodami
        for obstacle in self.obstacle_list:
            if arcade.check_for_collision(self.player, obstacle):
                arcade.play_sound(self.rat_sound)
                self.lives -= 1
                self.obstacle_list.remove(obstacle)
                if self.lives <= 0:
                    self.game_over = True

        # Kolizje z bonusami
        for bonus in self.bonus_list:
            if arcade.check_for_collision(self.player, bonus):
                arcade.play_sound(self.notes_sound)
                self.score += 10
                self.bonus_list.remove(bonus)
                if self.score >= self.next_score_sound_threshold:
                    arcade.play_sound(self.triumph_sound)
                    self.next_score_sound_threshold += 100    

    def on_draw(self):
        """Render the game screen including background, lanes, player, obstacles, bonuses, score, lives, and game over screen"""

        self.clear()

        background_rect = arcade.Rect(
            x=SCREEN_WIDTH // 2,
            y=SCREEN_HEIGHT // 2,
            width=SCREEN_WIDTH,
            height=SCREEN_HEIGHT,
            left=0,
            right=SCREEN_WIDTH,
            bottom=0,
            top=SCREEN_HEIGHT
        )
        arcade.draw_texture_rect(self.background, background_rect)

        total_height = SCREEN_HEIGHT // 2
        lane_height = total_height // 3
        bottom_start = 0

        lane_colors = [
            (100, 255, 100, 150),  # jasny zielony (pastelowy)
            (150, 230, 255, 150),  # bardzo jasny niebieski
            (255, 100, 120, 150)   # różowy pozostaje bez zmian
        ]

        border_colors = [
            (80, 230, 80),
            (150, 230, 255),
            (255, 160, 170)
        ]

        for i in range(3):
            bottom = bottom_start + i * lane_height
            top = bottom + lane_height
            left = 0
            right = SCREEN_WIDTH

            arcade.draw_lrbt_rectangle_outline(left, right, bottom, top, border_colors[i], border_width=2)

            line_spacing = 4
            line_thickness = 1
            for y_line in range(bottom, top, line_spacing):
                arcade.draw_line(left, y_line, right, y_line, lane_colors[i], line_thickness)

        self.player_list.draw()
        self.obstacle_list.draw()
        self.bonus_list.draw()

        arcade.draw_text(f"Wynik: {self.score}", 20, SCREEN_HEIGHT - 40, arcade.color.WHITE, 20)

        for i in range(self.lives):
            center_x = SCREEN_WIDTH - 30 - i * 40
            center_y = SCREEN_HEIGHT - 30
            width = 30
            height = 30
            left = center_x - width / 2
            right = center_x + width / 2
            bottom = center_y - height / 2
            top = center_y + height / 2

            heart_rect = arcade.Rect(
                x=center_x,
                y=center_y,
                width=width,
                height=height,
                left=left,
                right=right,
                bottom=bottom,
                top=top
            )
            arcade.draw_texture_rect(self.heart_texture, heart_rect)

        if self.game_over:
            arcade.draw_lrbt_rectangle_filled(0, SCREEN_WIDTH, 0, SCREEN_HEIGHT, (0, 0, 0, 180))
            arcade.draw_text("Koniec Gry", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 40,
                             arcade.color.WHITE, 40, anchor_x="center")

            arcade.draw_lrbt_rectangle_filled(
            self.menu_button_x - self.menu_button_width // 2,
            self.menu_button_x + self.menu_button_width // 2,
            self.menu_button_y - self.menu_button_height // 2, 
            self.menu_button_y + self.menu_button_height // 2, 
            arcade.color.LIGHT_BLUE
            )
            arcade.draw_text("Menu", self.menu_button_x, self.menu_button_y,
                             arcade.color.BLACK, 20, anchor_x="center", anchor_y="center")

    def on_key_press(self, key, modifiers):
        """Handle player input for moving up or down between lanes

        Args:
            key (int): The key that was pressed
            modifiers (int): Bitmask for modifier keys (unused)
        """

        if key == arcade.key.UP:
            self.player.move_up()
        elif key == arcade.key.DOWN:
            self.player.move_down()

    def on_mouse_press(self, x, y, button, modifiers):
        """Handle mouse click on the menu button when the game is over

        Args:
            x (float): Mouse X coordinate
            y (float): Mouse Y coordinate
            button (int): Mouse button pressed
            modifiers (int): Bitmask for modifier keys (unused)
        """

        if self.game_over:
            if (self.menu_button_x - self.menu_button_width // 2 < x < self.menu_button_x + self.menu_button_width // 2 and
                self.menu_button_y - self.menu_button_height // 2 < y < self.menu_button_y + self.menu_button_height // 2):
                self.window.show_view(MainMenuView())

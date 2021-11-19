class Settings():
    def __init__(self):
        #Настройка экрана
        self.screen_width = 1500
        self.screen_height = 950
        self.display_color = (6,74,76)

        #Настройка пуль
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 0, 0, 0
        self.bullet_alowed = 3
        self.fleet_drop_speed = 10
        self.ship_limit = 3
        self.speedup_scale = 1.1
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        #Инициализирует настройки, изменяющиеся в ходе игры
        self.ship_speed_factor = 2.3
        self.bullet_speed_factor = 2.5
        self.alien_speed_factor = 1.7
        self.fleet_direction = 1
        self.alien_points = 50

    def increase_speed(self):
        #Увеличивает сложность
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
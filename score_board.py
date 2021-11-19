import pygame.font
from pygame.sprite import Group
from ship import Ship
class ScoreBoard():
    #Класс для вывода игровой информации
    def __init__(self, ai_settings, screen, stats, msg):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats
        self.msg = msg

        self.text_color = (30,30,30)
        self.font = pygame.font.SysFont(None, 48)
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_level(self):
        #Выводит текущий уровень
        self.level_image2 = self.font.render(self.msg, True, self.text_color, self.ai_settings.display_color)
        self.level_image = self.font.render(str(self.stats.level), True, self.text_color, self.ai_settings.display_color)
        self.level_rect2 = self.level_image2.get_rect()
        self.level_rect2.right = self.score_rect.right - 30
        self.level_rect2.top = self.score_rect.bottom + 10
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ships(self):
        #Сообщает количество оставшихся кораблей
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_settings, self.screen)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = -10
            self.ships.add(ship)



    def prep_score(self):
        #Преобразует счёт в графическое изображение
        rounded_score = int(round(self.stats.score, -1))
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.ai_settings.display_color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20


    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.screen.blit(self.level_image2, self.level_rect2)
        self.screen.blit(self.high_score_image2, self.high_score_rect2)
        self.ships.draw(self.screen)

    def prep_high_score(self):
        high_score = int(round(self.stats.high_score, -1))
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.ai_settings.display_color)
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top * 1.9

        self.high_score_image2 = self.font.render('Record', True, self.text_color, self.ai_settings.display_color)
        self.high_score_rect2 = self.high_score_image2.get_rect()
        self.high_score_rect2.centerx = self.screen_rect.centerx
        self.high_score_rect2.top = self.screen_rect.top + 5
        with open('record.txt', 'w') as fl_o:
            fl_o.write(str(high_score))


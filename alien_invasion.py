import pygame
from settings import Settings
from ship import Ship
import  game_functions as gf
from pygame.sprite import Group
from Alien import Alien
from game_stats import GameStats
from button import Button
from score_board import ScoreBoard
#Запуск игры
def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    ship = Ship(ai_settings, screen)
    alien = Alien(ai_settings, screen)
    stats = GameStats(ai_settings)
    bullets = Group()
    aliens = Group()
    play_button = Button(ai_settings, screen, "Play")
    gf.create_fleet(ai_settings, screen, ship, aliens)
    sb = ScoreBoard(ai_settings, screen, stats, "LVL: ")
    pygame.display.set_caption("Alien Invasion")
    #Цикл событий выполняемых пользователем
    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            bullets.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, sb, screen, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)
        pygame.display.flip()
run_game()

#AUTOR ~~~~ lautariano
#VK ~~~~ https://vk.com/id347462764
#GMAIL ~~~~ lautariano777@gmail.com
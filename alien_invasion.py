import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    ship = Ship(screen, ai_settings)
    bullets = Group()
    aliens = Group()
    stats = GameStats(ai_settings)
    play_button = Button(ai_settings, screen, "Play")
    sb = Scoreboard(ai_settings, screen, stats)

    gf.create_fleet(ai_settings, screen, aliens, ship)

    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(bullets)
            gf.check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, sb, ship, aliens, bullets)

        gf.update_screen(ai_settings, screen, stats, ship, aliens, bullets, play_button, sb)


run_game()

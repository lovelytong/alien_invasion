import sys
import pygame

from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf
from game_stats import Gamestats
from button import Button
from scoreboard import ScoreBoard

def run_game():
  #初始化游戏并创建一个屏幕对象
  pygame.init()
  ai_settings = Settings()
  screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
  pygame.display.set_caption("Alien Invasion")

  #创建一艘飞船，一个子弹编组和一个外星人编组,play按钮
  ship = Ship(ai_settings, screen)
  bullets = Group()
  aliens = Group()
  play_button = Button(ai_settings, screen, "play")

  #创建外星人群
  gf.create_fleet(ai_settings, screen, ship, aliens)

  #创建一个用于存储游戏统计信息的实例,并创建记分牌
  stats = Gamestats(ai_settings)
  sb = ScoreBoard(ai_settings, screen, stats)

  #开始游戏的主循环
  while  True:
    if stats.game_active:
      ship.update()
      gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
      gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)
    gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)

    gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)

run_game()
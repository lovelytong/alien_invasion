import sys
import pygame
from bullet import Bullet

def fire_bullet(ai_settings, screen, ship, bullets):
  if len(bullets) < ai_settings.bullets_allowed:
      #创建一颗子弹，并将其加入到编组bullets中
      new_bullet = Bullet(ai_settings, screen, ship)
      bullets.add(new_bullet)

def check_keydown_events(event, ai_settings, screen, ship, bullets):
  if event.key == pygame.K_RIGHT:
    ship.moving_right = True
  elif event.key == pygame.K_LEFT:
    ship.moving_left = True
  elif event.key == pygame.K_SPACE:
    fire_bullet(ai_settings, screen, ship, bullets)

def check_keyup_events(event, ship):
  if event.key == pygame.K_RIGHT:
    ship.moving_right = False
  elif event.key == pygame.K_LEFT:
    ship.moving_left = False


def check_events(ai_settings, screen, ship, bullets):
  """响应按键和鼠标事件"""
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      sys.exit()

    elif event.type == pygame.KEYDOWN:
      check_keydown_events(event, ai_settings, screen, ship, bullets)

    elif event.type == pygame.KEYUP:
      check_keyup_events(event, ship)


def update_screen(ai_settings, screen, ship, bullets):
  #每次循环时都重绘屏幕
  screen.fill(ai_settings.bg_color)
  #在飞船和外星人后面重绘所有子弹
  for bullet in bullets.sprites():
    bullet.draw_bullet()
  ship.blitme()

  #让最近绘制的屏幕可见
  pygame.display.flip()

def update_bullets(bullets):
  #更新子弹位置，删除已消失的子弹
  bullets.update()

  for bullet in bullets:
    if bullet.rect.y <= 0:
      bullets.remove(bullet)




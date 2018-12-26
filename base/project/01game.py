# -*- coding: utf-8 -*-
#   File Name：     01game
#   Description :
#   Author :       zongyanzhang
#   date：          2018/12/26

from pygame.locals import *
import pygame
import sys

if __name__ == '__main__':
    # 设置图标
    pygame.display.set_icon(pygame.image.load('icon.ico'))
    window = pygame.display.set_mode((400, 600))
    window_rect = window.get_rect()
    print(window_rect.x, window_rect.y, window_rect.topleft, window_rect.right, window_rect.center)
    # 设置title
    pygame.display.set_caption('测试游戏')
    # 创建图片对象
    image = pygame.image.load('./images/me1.png')
    image_rect = image.get_rect()

    # 设置图片显示位置
    image_rect.midbottom = (window_rect.midbottom[0], window_rect.midbottom[1]-20)

    # 设置帧率
    clock = pygame.time.Clock()
    while True:
        # 获取所有的事件
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit(0)
        # 获取按键
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            image_rect.x -= 2
        if keys[pygame.K_RIGHT]:
            image_rect.x += 2
        if keys[pygame.K_UP]:
            image_rect.y -= 2
        if keys[pygame.K_DOWN]:
            image_rect.y += 2

        window.fill((255,255,255))
        # 将一个image画到另一个image中
        window.blit(image, image_rect)

        clock.tick(30)
        # 刷新
        pygame.display.flip()
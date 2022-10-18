import random
import pygame

#屏幕大小的常量
SCREEN_RECT = pygame.Rect(0,0,1200,700)
#刷新的帧率
FRAME_PER_SEC = 60
#创建敌机的定时器常量
CREATE_ENEMY_EVENT = pygame.USEREVENT
#英雄发射子弹事件
HERO_FIRE_EVENT = pygame.USEREVENT + 1




class GameSprite(pygame.sprite.Sprite):
    """飞机大战游戏精灵"""
    def __init__(self, image_name, speed=1):
        super().__init__()
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        self.rect.x -= self.speed

class Tank(GameSprite):
    """英雄精灵"""

    def __init__(self):

        #调用父类方法，设置image speed
        super().__init__("TE_Karrar.png", 0)

        #设置英雄初始位置
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120

        #创建子弹的精灵组
        self.bullets = pygame.sprite.Group()


    def update(self):

        #英雄在水平方向移动
        self.rect.x += self.speed

        #控制英雄不能离开屏幕
        if self.rect.x < 0:
            self.rect.x = 0

        elif self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right


    def fire(self):
        print("发射子弹")

        bullet = Bullet()

            #设置精灵的位置
        bullet.rect.bottom = 250
        bullet.rect.centerx = self.rect.centerx - 250

            #将精灵添加到精灵组
        self.bullets.add(bullet)


class Bullet(GameSprite):
    def __init__(self):
    
        #调用父类方法设施子弹图片 初始速度
        super().__init__("Heavy_Shell.png", -2)

    def update(self):

        #调用父类方法，让子弹沿垂直方向飞行
        super().update()

        #判断子弹是否飞出屏幕
        if self.rect.bottom < 0:
            self.kill()

    def __del__(self):
        print("子弹被销毁")
        
import random
import pygame

#屏幕大小的常量
SCREEN_RECT = pygame.Rect(0,0,1200,600)
#刷新的帧率
FRAME_PER_SEC = 60
#创建敌机的定时器常量
CREATE_ENEMY_EVENT = pygame.USEREVENT
#英雄发射子弹事件
TANK_FIRE_EVENT = pygame.USEREVENT + 1

class GameSprite(pygame.sprite.Sprite):
    """飞机大战游戏精灵"""
    def __init__(self, image_name, speed=1):

        #调用父类的初始化方法
        super().__init__()

        #定义对象属性
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.rect.centerx = self.rect.centrex + 10
        self.speed = speed

    def update(self):

        #在屏幕垂直方向上移动
        self.rect.y += self.speed
        

class Tank(GameSprite):
    """Tank Spirite"""
    def __init__(self):
        super().__init__("TE_Karrar.png", 0)
        
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120

        self.bullets = pygame.sprite.Group()
        
class Enemy(GameSprite):
    """敌机精灵"""

    def __init__(self):
        #调用父类方法，创建敌机精灵，同时指定敌机图片
        super().__init__("leopard.png")
        #指定敌机的初始随机速度
        self.speed = random.randint(1,3)

        #指定敌机的初始随机位置
        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0,max_x)

    def update(self):

        #调用父类方法，保持垂直方向上的飞行
        super().update()
        #判断是否飞出屏幕，如果是，需要从精灵组删除敌机
        if self.rect.y >= SCREEN_RECT.height:
            #print("飞出屏幕，需要从精灵组删除")
            #kill 方法可以将精灵从所有精灵组中移出，精灵就会被自动销毁
            self.kill()

    def __del__(self):
       # print("敌机挂了 %s" %self.rect)
        pass       
        
class Bullet(GameSprite):
    """Bullet Spirite"""

    def __init__(self):

        #调用父类方法设施子弹图片 初始速度
        super().__init__("images.jfif", 1)

    def update(self):

        #调用父类方法，让子弹沿垂直方向飞行
        super().update()

        #判断子弹是否飞出屏幕
        if self.rect.topright > 1200:
            self.kill()

    def __del__(self):
        print("子弹被销毁")

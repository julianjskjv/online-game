from pygame import*
from random import randint
from math import hypot*
init()
window=display.set_mode((800,800))
display.set_caption("Level 1")
window.fill((135, 105, 255))

clock=time.Clock()
my_player=[0,0,20]
all_players=[]
class  Food():
    def __init__(self,x,y,r,c):
        self.x=x
        self.y=y
        self.size=r
        self.color=c
    def check_collision(self,player_x,player_y,player_r):
            dx=self.x - player_x
            dy=self.y - player_y


eats=[Food(randint(0,800),randint(0,600),10,(randint(0,255),randint(0,255),randint(0,255))) for _ in range(20)]

while True:
    for e in event.get():
        if e.type==QUIT:
            quit()
    draw.circle(window,(181, 223, 255),(500,500),my_player[2])
    keya=key.get_pressed()
    if keya[K_w]: my_player[1]-= 15
    if keya[K_s]: my_player[1]+= 15
    if keya[K_a]: my_player[0]-= 15
    if keya[K_d]: my_player[0]+= 15

    display.update()
    clock.tick(60)

import pgzrun
import random
WIDTH=1000
HEIGHT=700
Flower=Actor("flower")
Flower.x=200
Flower.y=130
Bee=Actor("left")
Bee.x=500
Bee.y=235

angle=0
score=0
game=True
def timer():
    global game
    game=False
def draw():
    screen.fill("Grey")
    Flower.draw()
    Bee.angle=angle
    Bee.draw()
    screen.draw.text(str(score),(450,50))
    if game==False:
        screen.fill("Red")
        screen.draw.text("Game over, you scored "+str(score),(500,350))
def update():
    global angle,score
    if keyboard.w:
        if Bee.y>30:
            Bee.image="up"
            Bee.y-=5
    if keyboard.s:
         if Bee.y<650:
            Bee.image="down"
            Bee.y+=5
    if keyboard.a:
         if Bee.x>30:
            Bee.image="left"
            Bee.x-=5
    if keyboard.d:
        if Bee.x<950:
            Bee.image="right"
            Bee.x+=5
    if Bee.colliderect(Flower):
        Flower.x=random.randint(50,950)
        Flower.y=random.randint(50,650)
        score+=1
clock.schedule(timer,60.0)
pgzrun.go()


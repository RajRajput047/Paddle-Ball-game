
import pygame as pg
import sys,time,random
pg.init()
SCREEN_WIDTH=700
SCREEN_HIGHT=700
win=pg.display.set_mode((700,700))
paddle=pg.Rect(310,660,80,20)
BALL_X=paddle.x+40
BALL_Y=paddle.y-13
MAX_BALL_SPEED=7
MIN_BALL_SPEED=4
BALL_X_SPEED=0
BALL_Y_SPEED=0
font=pg.font.Font("Bold.ttf",15)
SCORE=0
scoretext=font.render("Score:0",True,(000,255,000))
scoretextRect=scoretext.get_rect()
scoretextRect.x=10
scoretextRect.y=10
font2=pg.font.Font("Bold.ttf",48)
gameovertext=font2.render("GAME OVER",True,(255,000,000))
gameovertextRect=gameovertext.get_rect()
gameovertextRect.center=(SCREEN_WIDTH//2,SCREEN_HIGHT//2)
font3=pg.font.Font("Bold.ttf",60)
welcometext=font3.render("WEL COME",True,(255,255,000))
welcometextRect=welcometext.get_rect()
welcometextRect.center=(SCREEN_WIDTH//2,SCREEN_HIGHT//2)
font4=pg.font.Font("Bold.ttf",32)
notetext=font4.render("PRESH SPACE TO START",True,(255,000,255),(255,255,255))
notetextRect=notetext.get_rect()
notetextRect.center=(SCREEN_WIDTH//2,SCREEN_HIGHT//2+50)
font5=pg.font.Font("Bold.ttf",32)
exittext=font5.render("PRESH ESCAPE TO EXIT",True,(255,000,255),(255,255,255))
exittextRect=exittext.get_rect()
exittextRect.center=(SCREEN_WIDTH//2,SCREEN_HIGHT//2+50)
font6=pg.font.Font("Bold.ttf",15)
exittext2=font6.render("PRESH ESCAPE TO EXIT",True,(000,255,000))
exittext2Rect=exittext.get_rect()
exittext2Rect.x=550
exittext2Rect.y=10
pg.mixer.music.load("background.mp3")
pg.mixer.Sound("end.mp3")
old=time.time()
TARGET_FPS=100
clock=pg.time.Clock()
GAME_RUNNING=True
GAME_STARTED=False



def updateScore():
    global SCORE,scoretext
    SCORE+=1
    scoretext=font.render(f"Score:{SCORE}",True,(000,255,000))



def GAMEOVER():
    global GAME_RUNNING
    GAME_RUNNING=False
    

def checkcollision():
    global SCREEN_WIDTH,paddle,BALL_X,BALL_Y,BALL_X_SPEED,BALL_Y_SPEED,GAME_STARTED
    if paddle.x<=0:
        paddle.x=0
    if paddle.x>=SCREEN_WIDTH-80:
        paddle.x=SCREEN_WIDTH-80
    
    if BALL_X-13<=0 or BALL_X+13>=SCREEN_WIDTH:
        BALL_X_SPEED=-BALL_X_SPEED
    if BALL_Y-13<=0:
        BALL_Y_SPEED=-BALL_Y_SPEED
    if BALL_Y+13>=paddle.y+5. and GAME_STARTED==True and BALL_X>=paddle.x and BALL_X<=paddle.x+80:
        BALL_Y_SPEED=-BALL_Y_SPEED 
        updateScore()
    elif BALL_Y>paddle.y:
        GAMEOVER()
        
            

while True:
    new=time.time()
    dt=new-old
    old=new
    
    for event in pg.event.get():
        
        if event.type==pg.QUIT:
            pg.quit()
            sys.exit()
        if event.type==pg.KEYDOWN:
            if event.key==pg.K_SPACE:
                GAME_STARTED=True
                pg.mixer.music.play()  
                sign=random.randint(0,1)    
                BALL_Y_SPEED=-random.randint(MIN_BALL_SPEED,MAX_BALL_SPEED)   
                BALL_X_SPEED=random.randint(MIN_BALL_SPEED,MAX_BALL_SPEED)   
                if sign==0:
                    BALL_X_SPEED=-BALL_X_SPEED
            if event.key==pg.K_ESCAPE:
                pg.quit() 
                sys.exit()
    checkcollision()           
    if GAME_RUNNING==True:
        
        if GAME_STARTED==False and SCORE==0:
            win.blit(welcometext,welcometextRect)
        key=pg.key.get_pressed()
        if key[pg.K_RIGHT]   :
            paddle.x+=5*dt*TARGET_FPS  
            if GAME_STARTED==False:
                BALL_X=paddle.x+40 
        if key[pg.K_LEFT]   :
            paddle.x-=5*dt*TARGET_FPS
            if GAME_STARTED==False:
                BALL_X=paddle.x+40 
            
        win.fill("black")  
        win.blit(scoretext,scoretextRect)
        win.blit(exittext2,exittext2Rect)
              
        pg.draw.rect(win,"grey",paddle) 
        if GAME_STARTED==False:
            pg.draw.circle(win,"white",(BALL_X,BALL_Y),13) 
        if GAME_STARTED==False:
            win.blit(welcometext,welcometextRect)
            win.blit(notetext,notetextRect) 
              
        else:
            BALL_X+=BALL_X_SPEED*dt*TARGET_FPS   
            BALL_Y+=BALL_Y_SPEED*dt*TARGET_FPS  
            pg.draw.circle(win,"white",(BALL_X,BALL_Y),13)
             
    else:
        win.blit(gameovertext,gameovertextRect)
        win.blit(exittext,exittextRect)
        pg.mixer.music.pause() 
        pg.mixer.Sound("end.mp3").play()
    
    pg.display.update()  
     
    clock.tick(150)
    
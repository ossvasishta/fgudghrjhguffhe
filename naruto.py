import pygame

pygame.init()
white = (255,255,255)
red = (255,0,0)

naruto_left = pygame.image.load('NL1.png')
naruto_right = pygame.image.load('NR1.png')
naruto_rassengan = pygame.image.load('nar.png')
form = pygame.image.load('Nstanding.png')
screen_width = 1200
screen_height = 600
pygame.mixer.init()

win = pygame.display.set_mode((screen_width,screen_height))
p_x = 36
p_y = 516
state = "normal"
press = False
direction = "right"
state = False
lock = False
jump = False
vel_y = 15
sound_play = False
lock2 = False

shadow_clone_state = 'normal'

run = True

while run:
    for event in pygame.event.get():
        key = pygame.key.get_pressed()

    if event.type == pygame.QUIT:
        run = False


    win.fill(white)
    naruto_player = pygame.draw.rect(win,white,[p_x,p_y,63,80])
    if direction == "left":
        win.blit(naruto_left,(p_x-20,p_y))

    if direction == "right":
        win.blit(naruto_right,(p_x-20,p_y))


    if not state:
        if key[pygame.K_SPACE]:
            kagebun_shino_jutsu_sound = pygame.mixer.music.load('kagebunshin.mp3')
            pygame.mixer.music.play()
            state = True
            shadow_clone_x = p_x+80
            shadow_clone_y = p_y
            shadow_clone_2_x = p_x+150
            shadow_clone_2_y = p_y


        
        

    if state:
        pygame.draw.rect(win,white,[shadow_clone_x,shadow_clone_y,63,80])
        pygame.draw.rect(win,white,[shadow_clone_2_x,shadow_clone_2_y,63,83])
        win.blit(naruto_right,(shadow_clone_x-20,shadow_clone_y))
        win.blit(naruto_right,(shadow_clone_2_x-20,shadow_clone_2_y))
        if not lock:
            if key[pygame.K_r]:
               lock = True
               if not lock2:
                rassengan_sound = pygame.mixer.music.load('rasengan.mp3')
                pygame.mixer.music.play()

        if lock:
            pygame.draw.rect(win,white,[shadow_clone_x,shadow_clone_y,63,80])
            win.blit(naruto_rassengan,(shadow_clone_x,shadow_clone_y))
            sound_play = True
            shadow_clone_x +=3.3
    
        if not lock2:
            if key[pygame.K_2]:
                if not lock:
                    rassengan_sound = pygame.mixer.music.load('rasengan.mp3')
                    pygame.mixer.music.play()
                lock2 = True

        if lock2:
            pygame.draw.rect(win,white,[shadow_clone_2_x,shadow_clone_2_y,63,80])
            win.blit(naruto_rassengan,(shadow_clone_2_x,shadow_clone_2_y))
            shadow_clone_2_x +=2.3

            


        if shadow_clone_x>=1140:
            state = False
            lock = False
            lock2 = False

        if shadow_clone_2_x>=1140:
            state = False
            lock2 = False
            lock = False
        


        
        
            
            


    
    if key[pygame.K_RIGHT]:
        p_x += 6
        direction = "right"

    

    
    if key[pygame.K_LEFT]:
        p_x -=6 
        direction = "left"

    if not jump:
        if key[pygame.K_UP]:
            jump = True
        
    if jump:
        p_y = p_y-vel_y
        vel_y = vel_y-1
        if vel_y<-15:
            jump = False
            vel_y = 15

    if key[pygame.K_o]:
        print(p_x,
        p_y)

    pygame.time.delay(16)
    pygame.display.update()
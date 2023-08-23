import pygame

pygame.init()

screen_width=800
screen_height=400
screen=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('invat pygame')
clock=pygame.time.Clock()
test_font=pygame.font.Font(None,50) #font type ttf file, font size
game_over_font=pygame.font.Font(None,50)
game_Active=True

ground_surface=pygame.image.load('ground.png').convert()
sky_surface=pygame.image.load('Sky.png').convert()

score_surface=test_font.render('experienta starbucks',False,(64,64,64)).convert() #text, anti-aliasing AA,color
score_rectangle=score_surface.get_rect(center=(400,50))

game_over_surface=game_over_font.render('Game over! Press Space to try again.',False,(64,64,64)).convert() #text, anti-aliasing AA,color
game_over_rectangle=game_over_surface.get_rect(center=(400,50))

sbx_surface=pygame.image.load('sbx_cup.png').convert_alpha()
sbx_rectangle=sbx_surface.get_rect(bottomright=(810,310))

player_surface=pygame.image.load('player1-removebg-preview (1).png').convert_alpha()
player_rectangle=player_surface.get_rect(midbottom=(80,335))
player_gravity=0

run=True
while run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
        if game_Active:
           if event.type==pygame.KEYDOWN:
               if event.key==pygame.K_SPACE: #and player_rectangle.bottom>=330:
                   player_gravity= -20
               elif event.key==pygame.K_d:
                   player_rectangle.move_ip(10,0)
               elif event.key==pygame.K_a:
                   player_rectangle.move_ip(-10,0)
        else:
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    game_Active=True
                    sbx_rectangle.left=800



    if game_Active:
       screen.blit(ground_surface,(0,300)) #surface+position XY
       screen.blit(sky_surface,(0,0))
       pygame.draw.rect(screen,'#c0e8ec',score_rectangle) #surface,color,actual rect -draw a rect all colored
       pygame.draw.rect(screen, '#c0e8ec', score_rectangle, 6,5)  # surface,color,actual rect,width,radius -draw a rect without the center colored
       #pygame.draw.ellipse(screen,'Brown',pygame.Rect(50,200,100,100)) #rect-left,top,width,height
       screen.blit(score_surface,score_rectangle)

       #pygame.draw.line(screen,'Red',(0,0),pygame.mouse.get_pos())


       sbx_rectangle.x -= 3
       if sbx_rectangle.x < -10:
           sbx_rectangle.left = 800
       screen.blit(sbx_surface,sbx_rectangle)


       #WORK with PLAYER
       player_gravity += 1
       player_rectangle.y+=player_gravity
       if player_rectangle.bottom>=330:
           player_rectangle.bottom=330
       screen.blit(player_surface,player_rectangle)

       #collision
       if sbx_rectangle.colliderect(player_rectangle):
           game_Active=False


    else:
        screen.fill('Red')
        screen.blit(game_over_surface,game_over_rectangle)




    pygame.display.update()
    clock.tick(60) #this loop doesn't run faster than 60 times per sec

pygame.quit()
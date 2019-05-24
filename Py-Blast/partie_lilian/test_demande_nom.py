import pygame
 
BLUE = (40, 120, 230)
GREEN = (40, 230, 120)
 
pygame.init()
screen = pygame.display.set_mode((640, 480))
center_x, center_y = 320, 240
 

font = pygame.font.SysFont('Comic Sans MS,Arial', 24)
prompt = font.render('Entrez un nombre : ', True, BLUE)

 
user_input_value = ""
user_input = font.render(user_input_value, True, GREEN)

 
continuer = 1
 
while continuer:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = 0
            
        if event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_RETURN, pygame.K_KP_ENTER):
                continuer = 0
               
            if event.key == pygame.K_BACKSPACE:
                user_input_value = user_input_value[:-1]
            else:
                user_input_value += event.unicode
            user_input = font.render(user_input_value, True, GREEN)
            
 
    
 
    screen.fill((0,0,0))
    screen.blit(prompt, (200,150))
    screen.blit(user_input, (425,150))
    pygame.display.flip()
 
print(user_input_value)
 
pygame.quit()
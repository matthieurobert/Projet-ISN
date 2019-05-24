        if  key[pygame.K_s] and key[pygame.K_a]   :
            clock.tick(time)
            for d in range (0,len(rekt_boîte)):           
                if position_perso.colliderect(rekt_boîte[d]):
                    position_perso = position_perso.move(speed_diagonal,-speed_diagonal)
                
            position_perso = position_perso.move(-speed_diagonal,speed_diagonal)         
            fenetre.blit(perso, position_perso)
            pygame.display.flip()

        if  key[pygame.K_s] and key[pygame.K_d] :
            clock.tick(time)
            for d in range (0,len(rekt_boîte)):            
                if position_perso.colliderect(rekt_boîte[d]):
                    position_perso = position_perso.move(-speed_diagonal,-speed_diagonal)
                
            position_perso = position_perso.move(speed_diagonal,speed_diagonal)         
            fenetre.blit(perso, position_perso)
            pygame.display.flip()

        if  key[pygame.K_w] and key[pygame.K_d] :
            clock.tick(time)
            for d in range (0,len(rekt_boîte)):            
                if position_perso.colliderect(rekt_boîte[d]):
                    position_perso = position_perso.move(-speed_diagonal,speed_diagonal)
               
            position_perso = position_perso.move(speed_diagonal,-speed_diagonal)         
            fenetre.blit(perso, position_perso)
            pygame.display.flip()

        if  key[pygame.K_w] and key[pygame.K_a] :
            clock.tick(time)
            for d in range (0,len(rekt_boîte)):            
                if position_perso.colliderect(rekt_boîte[d]):
                    position_perso = position_perso.move(speed_diagonal,speed_diagonal)
               
            position_perso = position_perso.move(-speed_diagonal,-speed_diagonal)
                    
            fenetre.blit(perso, position_perso)
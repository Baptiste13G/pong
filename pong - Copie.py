"""Ce qu'il reste à faire
-la balle qui bouge
-les collisions
-système de points
-interface (nombre de points etc.)"""
"test"

import pygame
import random 



print("Pygame fonctionne !")


class Bordure1(pygame.sprite.Sprite):
    def __init__(self, hauteur):
        super().__init__()
        self.image = pygame.Surface((25,hauteur))
        self.image.fill((0,0,0))
        self.rect = self.image.get_rect()

class Bordure2(pygame.sprite.Sprite):
    def __init__(self, largeur):
        super().__init__()
        self.image = pygame.Surface((largeur,25))
        self.image.fill((0,0,0))
        self.rect = self.image.get_rect()



class Rect(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((25,250))
        self.image.fill((0,0,0))
        self.rect = self.image.get_rect()

class Balle(pygame.sprite.Sprite):
        def __init__(self,):
            super().__init__()
            self.image = pygame.Surface((50,50), pygame.SRCALPHA)
            pygame.draw.circle(self.image, ((0,0,0)), (25, 25), 25)
            self.rect = self.image.get_rect()


def pong():

    pygame.init()
    window=pygame.display.set_mode((0, 0),pygame.FULLSCREEN)
    pygame.display.set_caption("Pong")
    largeur, hauteur = window.get_size()
    centre_x= largeur//2
    centre_y= hauteur//2

    b1=Bordure1(hauteur)
    b2=Bordure1(hauteur)
    b3=Bordure2(largeur)
    b4=Bordure2(largeur)
    ball=Balle()
    j1=Rect()
    j2=Rect()
    j1.rect.center = (100,centre_y)
    j2.rect.center = (largeur-100,centre_y)
    ball.rect.center = (centre_x,centre_y)
    b1.rect.topleft = (0,0) #bordure de gauche
    b2.rect.topright = (largeur,0) #bordure de droite
    b3.rect.topleft = (0,0) #bordure de haut
    b4.rect.bottomleft = (0,hauteur) #bordure de bas

    j1_g=pygame.sprite.Group()
    j2_g=pygame.sprite.Group()
    b_g=pygame.sprite.Group()
    bord_g1=pygame.sprite.Group()
    bord_g2=pygame.sprite.Group()

    j1_g.add(j1)
    j2_g.add(j2)
    b_g.add(ball)
    bord_g1.add(b1)
    bord_g1.add(b2)
    bord_g2.add(b3)
    bord_g2.add(b4)


    test=True
    while test:
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                test=False
            else :
                pygame.display.update()
                window.fill((255,255,255))
                bord_g1.update()
                bord_g2.update()
                j1_g.update()
                j2_g.update()
                b_g.update()
                j1_g.draw(window)
                j2_g.draw(window)
                b_g.draw(window)
                bord_g1.draw(window)
                bord_g2.draw(window)
                if i.type == pygame.KEYDOWN :
                    if i.key == pygame.K_ESCAPE:
                        pygame.quit()
                    if i.key == pygame.K_DOWN :
                        j2.rect.y += 20
                    if i.key == pygame.K_UP :
                        j2.rect.y -= 20
                    if i.key == pygame.K_s :
                        j1.rect.y += 20
                    if i.key == pygame.K_z :
                        j1.rect.y -= 20
                    
                



    pygame.quit()

pong()
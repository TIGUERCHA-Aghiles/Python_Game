import pygame
from comet import Comet

# creer une classe pour gerer cet evenment
class CometFalleEvent:

    # lors de chargement  -> creer un compteur
    def __init__(self, game):
        self.percent = 0
        self.percent_speed = 10
        self.game = game
        self.fall_mode = False

        # definir un groupe de sprite pour stocker nos comets
        self.all_comets = pygame.sprite.Group()

    def add_percent(self):
        self.percent += self.percent_speed / 100

    def is_full_loaded(self):
        return self.percent >= 100
    
    def reset_percent(self):
        self.percent = 0

    def meteor_fall(self):
        # boucle pour les valeurs 1 et 10
        for i in range(1, 10):
            # apparaitre 1 premiere boule de feu
            self.all_comets.add(Comet(self))

    def attempt_fall(self):
        # la jauge d'evenment est totalement charge
        if self.is_full_loaded() and len(self.game.all_monsters) == 0:
            print("Pluie de comets !!")
            self.meteor_fall()
            self.fall_mode = True # activer l'evenment

    def update_bar(self, surface):

        # ajouter du pourcentage a la bar
        self.add_percent()

        # # appel de la methode pour essayer de declancher la pluie de comets
        # self.attempt_fall()

        # barre noir (en arriere plan)
        pygame.draw.rect(surface, (0, 0, 0), [
            0, # l'axe des x
            surface.get_height() - 20, # l'axe des y
            surface.get_width(), # longueur de la fenetre
            10 # eppaisseur de la barre
        ])
        #barre rouge (jauge d'event)
        pygame.draw.rect(surface, (187, 11, 11), [
            0, # l'axe des x
            surface.get_height() - 20, # l'axe des y
            (surface.get_width() / 100) * self.percent, # longueur de la fenetre
            10 # eppaisseur de la barre
        ])
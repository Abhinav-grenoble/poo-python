#
from animal import Animal

class Serpent(Animal):

    def __init__(self, poids, taille):
        super().__init__(poids,taille)

    def se_deplacer(self):
        return f" I am Serpent, I can crawl. Weight:{self.poids}, Height:{self.taille}"
    
    def __repr__(self):
        return f" I am Serpent, I can crawl. Weight:{self.poids}, Height:{self.taille}" 
 

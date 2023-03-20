
from animal import Animal

class Birds(Animal):

    def __init__(self, poids, taille,max_height):
        super().__init__( poids,taille)
        self.max_height=max_height

    def se_deplacer(self):
        pass
     #   return f"I am a Bird I fly to Maximus height=== {self.max_height} m "

    def __repr__(self):
        return f"I am a Bird, Weight=={self.poids}  Height=={self.taille} fly to Maximus height=== {self.max_height} m "

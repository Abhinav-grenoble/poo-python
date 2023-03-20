    
class Animal: 
       
    def __init__(self, poids, taille):
        
        self.poids  = poids    # instance variable
        self.taille = taille   # instance variable         

    def se_deplacer(self):
        return f"Animal  Weight:{self.poids}, Height:{self.taille}"
    
    def __repr__(self):
        return f"Animal  Weight:{self.poids}, Height:{self.taille}"

    def get_a(self):
        return self.__poids
        
        
    def set_a(self, a):
        if a > 0:
            self.__poids = a
        else:
            print("\n WEIGHT\n   is\nNEGATIVE\n")
            raise ValueError 
                  

    poids = property(get_a,set_a) # property function calls getter if you just call it  euallity sign will call the setter

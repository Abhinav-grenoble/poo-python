

class Zoo:

    def __init__(self,list_animal):
        self.list_animal=list(list_animal)

    def add_animal(self, name_animal): 
        self.list_animal.append(name_animal)
    
    def __add__(self, other_list):
        return Zoo( self.list_animal + list(other_list))
        
    def __repr__(self):
        return f"Animal list:{self.list_animal}"
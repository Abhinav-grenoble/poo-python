from animal import Animal
from serpent import Serpent
from birds import Birds
from zoo import Zoo

animal1 = Animal(-3,1.5)
snake1  = Serpent(2,1.7)
bird1   = Birds(1, 1.0, 65)

#list_animal=['animal2','snake2','bird2']
list_animal_1=[animal1,snake1,bird1]
zoo1=Zoo(list_animal_1)
#print(zoo1)
animal2=Animal(200000,40000)
snake2  = Serpent(5000,100000)
bird2   = Birds(2000, 10000, 6500000)
list_animal_2=[animal2,snake2, bird2]

#animal1.poids = 4
#print(animal1.poids)
#print(animal1)
#print(animal1.se_deplacer())
#print(snake1)
#print(snake1.se_deplacer())
#print(bird1)
#print(bird1.se_deplacer())
#print(zoo.se_deplacer())

print(zoo1.add_animal(animal2))
print(list_animal_1+list_animal_2)
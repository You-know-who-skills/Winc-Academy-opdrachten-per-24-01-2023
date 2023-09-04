# Do not modify these lines
__winc_id__ = '04da020dedb24d42adf41382a231b1ed'
__human_name__ = 'classes'

# Add your code after this line

print('\n')

class Player():
    
    def __init__(self, name: str, speed: float, endurance: float, accuracy: float) -> str:

        self.name = name
        self.speed = speed
        self.endurance = endurance
        self.accuracy = accuracy

    def introduce(self):
        
        print(F"Hello everyone, my name is {self.name}.\n")


    def strength(self):
        
        best = 0.9
        
        for attr in ["speed", "endurance", "accuracy"]:

            value = getattr(self, attr)
            
            if value > best:
                
                print(value)
                # best = (attr, value)
                
                # print(F"{best}, {value}")
                # print(F"{self.name} has {best}.")
            
            else:
                raise ValueError(F"Please make sure that {attr} is between 0 and 1.\n")
        
        return value
    

class Commentator():

    def __init__(self, name: str) -> str:

        self.name = name


if __name__ == "__main__":

    rijkaard = Player("Rijkaard", 0.1, 0.2, 0.3)
    gullit = Player("Gullit", 0.4, 0.5, 0.6)
    seedorf = Player("Seedorf", 0.7, 0.8, 0.9)

    rijkaard.introduce() # Deze code doet het.

    print(rijkaard.strength())
    print(gullit.strength())
    print(seedorf.strength())

    ray = Commentator("Ray Hudson\n") # Deze code doet het.
    
    print(ray.name) # Deze code doet het.
    
    






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
        print(F"Hello everyone, my name is {self.name}.")

    def strength(self):
        
        best = (None, 1)
        for attr in ["speed", "endurance", "accuracy"]:

            value = getattr(self, attr)
            
            if value <= best[-1]:
                best = (attr, value)
            
            else:
                raise ValueError(F"Please make sure that {attr} is between 0 and 1.\n")
        
        return best

if __name__ == "__main__":

    rijkaard = Player("Rijkaard", 0.1, 0.2, 0.3)
    gullit = Player("Gullit", 0.4, 0.5, 0.6)
    seedorf = Player("Seedorf", 0.7, 0.8, 0.9)

    print(rijkaard.strength())
    print(gullit.strength())
    print(seedorf.strength())
    
    






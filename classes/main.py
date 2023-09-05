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
        
        return F"Hello everyone, my name is {self.name}.\n"


    def strength(self):
        
        best_results = (None, 0) # Hier gebruik je een tuple omdat je nog niet weet welke resultaten het beste zijn.
        
        # for attribute in ["speed", "endurance", "accuracy"]:
        for attribute in ["speed", "endurance", "accuracy"]:

            outcome_attribute = getattr(self, attribute)

            if outcome_attribute > best_results[1]:
                
                best_results = attribute, outcome_attribute
                # print(attribute, outcome_attribute)
                        
                # if outcome_attribute == outcome_attribute:
                #     "speed" > "endurance" > "accuracy"
                
                # if outcome_attribute == best_results[1]:
                #     "speed" > "endurance" > "accuracy"
                    # print("Coolio")
                
            # else: print("Not coolio")

            if outcome_attribute > 1 or outcome_attribute < 0:
                raise ValueError(F"Please make sure that {attribute} is between 0 and 1.\n")
            
        return best_results
        # return attribute, outcome_attribute
        

class Commentator():

    def __init__(self, name: str) -> str:

        self.name = name


    def sum_player(self, player):

        attributes =  ["speed", "endurance", "accuracy"]

        sum = getattr(self, attributes)

        return F"{player}, {sum}"


if __name__ == "__main__":

    rijkaard = Player("Frank Rijkaard", 0.5, 0.5, 0.5)
    gullit = Player("Ruud Gullit", 0.2, 0.9, 0.3)
    seedorf = Player("Clarence Seedorf", 0.3, 0.6, 0.8)

    # rijkaard.introduce() # Deze code doet het.
    print(rijkaard.introduce()) # Deze code doet het.

    
    print(rijkaard.strength())
    print(gullit.strength())
    print(seedorf.strength())

    print('\n')

    winter = Commentator("Aron Winter")
    
    print(winter.name)
    
    print('\n')
    

    roy = Commentator("Bryan Roy", 0.9)

    print(roy.sum_player())


    
    






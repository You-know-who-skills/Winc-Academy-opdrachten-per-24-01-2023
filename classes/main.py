# Do not modify these lines
__winc_id__ = '04da020dedb24d42adf41382a231b1ed'
__human_name__ = 'classes'

# Add your code after this line

class Player():
    def __init__(self, name: str, speed: float, endurance: float, accuracy: float) -> str:

        self.name = name
        self.speed = speed
        self.endurance = endurance
        self.accuracy = accuracy

    def introduce(self):
        print(F"Hello everyone, my name is {self.name}.")

    def strength(self):
        for attr in ["speed", "endurance", "accuracy"]:
            






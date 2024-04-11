# Do not modify these lines
__winc_id__ = "9920545368b24a06babf1b57cee44171"
__human_name__ = "refactoring"

# Add your code after this line


class Specialist():

    def __init__(self, name):
        self.name = name


class Electrician(Specialist):
    pass

class Painter(Specialist):
    pass

class Plumber(Specialist):
    pass


class Homeowner():

    def __init__(self, name, address, needs):
        
        self.name = name
        self.address = address
        self.needs = needs
        self.contracts = []

    def add_contract(self, specialist):
        self.contracts.append(specialist)

specialist = {
    Electrician: Electrician("Alice Aliceville"),
    Painter: Painter("Bob Bobsville"),
    Plumber: Plumber("Craig Craigsville"),
}


homeowners = [
    Homeowner("Alfred Alfredson", "Alfredslane 123", [Painter, Plumber]),
    Homeowner("Bert Bertson", "Bertslane 231", [Plumber]),
    Homeowner("Candice Candicedottir", "Candicelane 312",
            [Electrician, Painter]),

]


for homeowner in homeowners:
    
    for need in homeowner.needs:
        homeowner.add_contract(specialist[need])
    
    print('\n')
    print(f"{homeowner.name}'s contracts:\n", [specialist.name for specialist in homeowner.contracts],)
    print('\n')

'''
Hieronder staat de oude code zoals deze te zien is voordat je het aan gaat passen
'''

# alice_name = "Alice Aliceville"
# alice_profession = "electrician"
# bob_name = "Bob Bobsville"
# bob_profession = "painter"
# craig_name = "Craig Craigsville"
# craig_profession = "plumber"

# alfred_name = "Alfred Alfredson"
# alfred_address = "Alfredslane 123"
# alfred_needs = ["painter", "plumber"]
# bert_name = "Bert Bertson"
# bert_address = "Bertslane 231"
# bert_needs = ["plumber"]
# candice_name = "Candice Candicedottir"
# candice_address = "Candicelane 312"
# candice_needs = ["electrician", "painter"]

# alfred_contracts = []
# for need in alfred_needs:
#     if need == alice_profession:
#         alfred_contracts.append(alice_name)
#     elif need == bob_profession:
#         alfred_contracts.append(bob_name)
#     elif need == craig_profession:
#         alfred_contracts.append(craig_name)

# bert_contracts = []
# for need in bert_needs:
#     if need == alice_profession:
#         bert_contracts.append(alice_name)
#     elif need == bob_profession:
#         bert_contracts.append(bob_name)
#     elif need == craig_profession:
#         bert_contracts.append(craig_name)

# candice_contracts = []
# for need in candice_needs:
#     if need == alice_profession:
#         candice_contracts.append(alice_name)
#     elif need == bob_profession:
#         candice_contracts.append(bob_name)
#     elif need == craig_profession:
#         candice_contracts.append(craig_name)

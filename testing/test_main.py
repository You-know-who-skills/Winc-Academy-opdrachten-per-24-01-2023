
from main import get_none


def test_get_none():

    # try:
    #     if get_none() == None:
    #         return True

    # except TypeError:             # Deze foutmelding komt niet tevoorschijn wanneer ik iets anders dan 'None' invul bij de 'return' statement in het 'main.py' bestand. LET OP!!! DIT FF NAVRAGEN BIJ EEN WINC MENTOR.
    #     return "Ceck again"
    
    try:
        if get_none() == None:
            return True

    except TypeError:
        return "Ceck again"


def test_flatten_dict():
    
    try:
        if flatten_dict == ({'a': 42, 'b': 3.14}):
        # [42, 3.14]
    
        flatten_dict({'a': [42, 350], 'b': 3.14})
        # [[42, 350], 3.14]


if __name__ == "__main__":

    print(test_get_none())

import main

'''
In test_main.py, write a function test_get_none that tests if a function from main.py called get_none returns None.
'''


def test_get_none():
    
    assert main.get_none() == None


'''
In test_main.py, write a function test_flatten_dict that tests if a function flatten_dict, when given a dictionary (dict) as its argument, returns the values of that dictionary in a list (list).

For example: 

flatten_dict({'a': 42, 'b': 3.14})
# [42, 3.14]
flatten_dict({'a': [42, 350], 'b': 3.14})
# [[42, 350], 3.14]

Tip: Try to think about the tests you're writing as a tiered system (= gelaagd systeem).

First, you might test if the value returned by flatten_dict is a list at all. Then you could test the function with a very small (single element) dictionary, then more complex dictionaries. 

This way if a test fails, you know not only that it fails, but also exactly where it fails. The more detailed the test levels, the better you can track the failure if the test fails.

'''

def test_flatten_dict():
    
    assert main.flatten_dict({'a': 42, 'b': 3.14}) == [42, 3.14]
            # [42, 3.14]
    
    # assert flatten_dict({'a': [42, 350], 'b': 3.14})
            # [[42, 350], 3.14]


if __name__ == "__main__":

    print(test_get_none())
    print(test_flatten_dict())
    # print(test_add_numbers())
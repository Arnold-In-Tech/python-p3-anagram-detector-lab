# your code goes here!

# pseudocode
"""
- obtain each element from match list
- check if elent when sorted equal word when sorted
"""


class Anagram:

    def __init__(self, word):
        self.word = word

    def match(self, anagram_list):
        matches = [ele for ele in anagram_list if sorted(list(ele)) == sorted(list(self.word))]
        return matches


# test code                 
listen = Anagram("listen")
listen.match(['enlists', 'google', 'inlets', 'banana'])        

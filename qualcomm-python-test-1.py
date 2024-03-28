# Given a words.txt file containing a newline-delimited list of dictionary
# words, please implement the Anagrams class so that the get_anagrams() method
# returns all anagrams from words.txt for a given word.
#
# Bonus requirements:
#   - Optimise the code for fast retrieval
#   - Write more tests
#   - Thread safe implementation

import unittest

class Anagrams:

    def __init__(self):
        self.words = self.store_words_processed()

    def store_words_processed(self):
        """
        Store the words from the words.txt file in a dictionary with sorted word as key
        :return: dictionary with sorted word as key and list of anagrams as value
        
        """
        ana_data = {}
        with open('words.txt') as f:

            words_data = f.readlines()
            for word in words_data:
                word = word.strip()
                sort_word = ''.join(sorted(word.lower()))
                if sort_word in ana_data:
                    ana_data[sort_word].append(word)
                else:
                    ana_data[sort_word] = [word]       

        return ana_data

    def get_anagrams(self, word):
        """
        Get anagrams of the given word from the words.txt file
        :param word: word to find anagrams for
        :return: list of anagrams
        """
        
        sort_word = ''.join(sorted(word.lower().strip()))
        matched_anagrams= self.words.get(sort_word)
        if matched_anagrams:
            return matched_anagrams
        else:
            return []

class TestAnagrams(unittest.TestCase):

    ## Test positive cases for anagrams
    def test_anagrams(self):        
        anagrams = Anagrams()
        self.assertEqual(anagrams.get_anagrams('plates'), ['palest', 'pastel', 'petals', 'plates', 'staple'])
        self.assertEqual(anagrams.get_anagrams('platesss'), [])
        self.assertEqual(anagrams.get_anagrams('eat'), ['ate', 'eat', 'tea'])
        self.assertEqual(anagrams.get_anagrams('platess'), ['staples'])
    ## Test negative cases for anagrams
    def test_anagrams_negative(self):
        anagrams = Anagrams()
        self.assertEqual(anagrams.get_anagrams('platesss'), [])
        self.assertNotEqual(anagrams.get_anagrams('eat'), ['ate', 'eat', 'tea', 'ate'])
        self.assertNotEqual(anagrams.get_anagrams('hello'), ['hello', 'hello'])

if __name__ == '__main__':
    unittest.main()

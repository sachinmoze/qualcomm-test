import threading
import unittest

class Anagrams:
    def __init__(self):
        self.words = self.store_words_processed()
        self.lock = threading.Lock()

    def store_words_processed(self):
        ana_data = {}
        with open('words.txt') as file:
            for word in file:
                word = word.strip()
                sorted_word = ''.join(sorted(word.lower()))
                if sorted_word in ana_data:
                    ana_data[sorted_word].append(word)
                else:
                    ana_data[sorted_word] = [word]
        return ana_data

    def get_anagrams(self, word):
        """
        Get anagrams of the given word from the words.txt file
        :param word: word to find anagrams for
        :return: list of anagrams
        """
        
        sort_word = ''.join(sorted(word.lower().strip()))
        with self.lock:
            matched_anagrams = self.words.get(sort_word)
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
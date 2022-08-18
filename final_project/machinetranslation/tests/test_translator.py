import sys
import unittest

sys.path.append('../machinetranslation')

from translator import english_to_french, french_to_english

class TestE2F(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(english_to_french(''), 'Wrong input: empty or null') # test when null is given as input the output is 'Wrong input: empty or null'.
        self.assertEqual(english_to_french('Hello'), 'Bonjour')  # test when 'Hello' is given as input the output is 'Bonjour'.
        self.assertNotEqual(english_to_french('Hello'), None)

class TestF2E(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(french_to_english(''), 'Wrong input: empty or null') # test when null is given as input the output is 'Wrong input: empty or null'.
        self.assertEqual(french_to_english('Bonjour'), 'Hello')  # test when 'Hello' is given as input the output is 'Bonjour'.
        self.assertNotEqual(french_to_english('Bonjour'), None)
        
unittest.main()
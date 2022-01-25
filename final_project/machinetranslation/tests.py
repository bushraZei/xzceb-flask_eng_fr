import unittest
from translator import english_to_french, french_to_english

class TestMyFunction(unittest.TestCase):

    def test_null_input_e2f(self):
        self.assertIsNone(english_to_french(None))
    
    def test_null_input_f2e(self):
        self.assertIsNone(french_to_english(None))

    def test_correct_translation_f2e(self):
        self.assertEqual("Hello", french_to_english("Bonjour"))

    def test_correct_translation_e2f(self):
        self.assertEqual("Bonjour", english_to_french("Hello"))

if __name__ == '__main__':
    unittest.main()
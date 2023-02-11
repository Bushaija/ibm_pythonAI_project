import unittest
from translator import englishToFrench, frenchToEnglish

class TestTranslator(unittest.TestCase):
    #test for null input for frenchToEnglish
    def test_frenchToEnglish_null_input(self):
        with self.assertRaises(TypeError):
            frenchToEnglish(None)
    
    #test for null input for englishToFrench
    def test_englishToFrench_null_input(self):
        with self.assertRaises(TypeError):
            englishToFrench(None)
    
    #test translation of "hello" to "bonjour"
    def test_englishToFrench(self):
        self.assertEqual(englishToFrench("Hello"), "Bonjour")

    #test translation of "bonjour" to "hello"
    def test_frenchToEnglish(self):
        self.assertEqual(frenchToEnglish("Bonjour"),"Hello")


if __name__ == '__main__':
    unittest.main()

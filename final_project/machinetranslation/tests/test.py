import unittest

from translator import englishToFrench, frenchToEnglish

class TestEtoF(unittest.TestCase):
    def test1(self):
        self.assertEqual(englishToFrench(None), None)
        self.assertEqual(englishToFrench("Hello"), "Bonjour")
    
class TestFtoE(unittest.TestCase):
    def test1(self):
        self.assertEqual(frenchToEnglish(None), None)
        self.assertEqual(frenchToEnglish("Bonjour"), "Hello")

unittest.main()

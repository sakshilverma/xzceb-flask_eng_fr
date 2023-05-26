import unittest
import translator

class TestTranslateEnToFr(unittest.TestCase):
    """
    Class to test the function english_to_french
    """
    def test1(self):
        """
        Function to test the function english_to_french
        """
        self.assertIsNone(translator.english_to_french(None))
        print("englishToFrench: assertIsNone : Passed")
        self.assertEqual(translator.english_to_french("Hello"), "Bonjour")
        print("englishToFrench: assertEqual : Passed")
        self.assertNotEqual(translator.english_to_french("Bonjour"), "Hello")
        print("englishToFrench: assertNotEqual : Passed")

class TestTranslateFrToEn(unittest.TestCase):
    """
    Class to test the function french_to_english
    """
    def test1(self):
        """
        Function to test the function french_to_english
        """
        self.assertIsNone(translator.french_to_english(None))
        print("frenchToEnglish: assertIsNone : Passed")
        self.assertEqual(translator.french_to_english("Bonjour"), "Hello")
        print("frenchToEnglish: assertEqual : Passed")
        self.assertNotEqual(translator.french_to_english("Hello"), "Bonjour")
        print("frenchToEnglish: assertNotEqual : Passed")

unittest.main()
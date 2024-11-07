import unittest

from emotion_detection import emotion_detector


class TestEmotion_detector(unittest.TestCase): 

    # Define the first test method for the 'square' function.
    # Test methods should start with the word 'test' so that the test runner recognizes them as test cases.
    def test1(self): 
        
        self.assertEqual(emotion_detector('I am glad this happened'), 'joy') 
        self.assertEqual(emotion_detector('I am really mad about this'), 'anger')        
        self.assertEqual(emotion_detector('I feel disgusted just hearing about this'), 'disgust')
        self.assertEqual(emotion_detector('I am so sad about this'), 'sadness')
        self.assertEqual(emotion_detector('I am really afraid that this will happen'), 'fear')

unittest.main()

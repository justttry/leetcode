#encoding:UTF-8

import os
import unittest
import numpy as np
from findLadders import Solution
    
class TestSolution(unittest.TestCase):
    
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    def test_solution(self):
        beginWord = "hit"
        endWord = "cog"
        wordList = ["hot","dot","dog","lot","log","cog"]
        c = Solution.findLadders(beginWord, endWord, wordList)
        print(c)
    
    def test_solution_0(self):
        beginWord = "hot"
        endWord = "hog"
        wordList = ["hot", "hog"]
        c = Solution.findLadders(beginWord, endWord, wordList)
        print(c)
    
    def test_solution_1(self):
        beginWord = "hot"
        endWord = "dog"
        wordList = ["hot", "dog"]
        c = Solution.findLadders(beginWord, endWord, wordList)
        print(c)
    
    def test_solution_2(self):
        beginWord = "hit"
        endWord = "cog"
        wordList = ["hot","dot","dog","lot","log"]
        c = Solution.findLadders(beginWord, endWord, wordList)
        print(c)
    
    def test_solution_3(self):
        beginWord = "red"
        endWord = "tax"
        wordList = ["ted","tex","red","tax","tad","den","rex","pee"]
        c = Solution.findLadders(beginWord, endWord, wordList)
        print(c)
    
    def test_solution_4(self):
        beginWord = "qa"
        endWord = "sq"
        wordList = ["si","go","se","cm","so","ph","mt","db","mb",
                    "sb","kr","ln","tm","le","av","sm","ar","ci",
                    "ca","br","ti","ba","to","ra","fa","yo","ow",
                    "sn","ya","cr","po","fe","ho","ma","re","or",
                    "rn","au","ur","rh","sr","tc","lt","lo","as",
                    "fr","nb","yb","if","pb","ge","th","pm","rb",
                    "sh","co","ga","li","ha","hz","no","bi","di",
                    "hi","qa","pi","os","uh","wm","an","me","mo",
                    "na","la","st","er","sc","ne","mn","mi","am",
                    "ex","pt","io","be","fm","ta","tb","ni","mr",
                    "pa","he","lr","sq","ye"]
        c = Solution.findLadders(beginWord, endWord, wordList)
        print(c)
    
    def test_solution_5(self):
        beginWord = "hot"
        endWord = "log"
        wordList = ["hot", "hog", "log"]
        c = Solution.findLadders(beginWord, endWord, wordList)
        print(c)
    
    def test_solution_6(self):
        beginWord = "hit"
        endWord = "cot"
        wordList = ["hot","dot","dog","lot","log","cot"]
        c = Solution.findLadders(beginWord, endWord, wordList)
        print(c)
    
    def test_solution_7(self):
        beginWord = "hit"
        endWord = "cog"
        wordList = ["hot","dot","dog","lot","hog","cog"]
        c = Solution.findLadders(beginWord, endWord, wordList)
        print(c)
    
    def test_solution_8(self):
        beginWord = "abcd"
        endWord = "abee"
        wordList = ['abed', 'abee', 'afcd', 'afgd', 'afge', 'abge']
        c = Solution.findLadders(beginWord, endWord, wordList)
        print(c)
    
def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestSolution('test_solution_4'))
    suite.addTest(TestSolution('test_solution_7'))
    suite.addTest(TestSolution('test_solution_6'))
    suite.addTest(TestSolution('test_solution'))
    suite.addTest(TestSolution('test_solution_5'))
    suite.addTest(TestSolution('test_solution_0'))
    suite.addTest(TestSolution('test_solution_1'))
    suite.addTest(TestSolution('test_solution_2'))
    suite.addTest(TestSolution('test_solution_3'))
    suite.addTest(TestSolution('test_solution_8'))
    return suite

if __name__ == '__main__':
    unittest.main(defaultTest='suite')
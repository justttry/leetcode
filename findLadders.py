#encoding:UTF-8

import os
import numpy as np
import collections
import string

class Solution(object):
    @staticmethod
    def findLadders(beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        def add_path(word, der, path, forward):
            if forward: path[word].append(der)
            else: path[der].append(word)  
        def bfs(begin, end, path, forward, words):
            if not begin: return False
            if len(begin) > len(end): return bfs(end, begin, path, not forward, words)
            for word in (begin | end): words.discard(word)
            found, next_begin = False, set()
            for word in begin:
                for i in range(len(word)):
                    for c in string.ascii_lowercase:
                        der = word[:i] + c + word[i+1:]
                        if der in end:
                            found = True
                            add_path(word, der, path, forward)
                        if not found and der in words:
                            next_begin.add(der)
                            add_path(word, der, path, forward)
            return found or bfs(next_begin, end, path, forward, words)
        def construct(source, target, path):
            if source == target: return [[source]]
            return [[source] + rest for der in path[source] for rest in construct(der, target, path)]
        begin, end, path, words = {beginWord}, {endWord}, collections.defaultdict(list), set(wordList)
        if not (endWord in words and bfs(begin, end, path, True, words)): return []
        return construct(beginWord, endWord, path)
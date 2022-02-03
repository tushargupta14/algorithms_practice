#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 02-02-2022 22:45
# @Author  : Tushar Gupta

from collections import defaultdict


class TrieNode:

    def __init__(self):
        self.keys = {}
        self.isEnd = 0


class WordDictionary(object):

    def __init__(self):
        self.root = TrieNode()

    def getNode(self):
        return TrieNode()

    def get_index(self, char):
        return ord(char) - ord('a')

    def insert(self, word):

        node = self.root
        for char in word:
            if char not in node.keys:
                node.keys[char] = self.getNode()
            node = node.keys[char]
        node.isEnd = 1

    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """

        self.insert(word)

    def dfs(self, node, i, n):

        # print(self.word_to_search,i, node.isEnd)
        if i == n:
            if node.isEnd:
                return True
            else:
                return False

        if self.word_to_search[i] == '.':
            listOfNodes = node.keys.values()
            for val in listOfNodes:
                if self.dfs(val, i + 1, n):
                    return True
            return False

        if self.word_to_search[i] in node.keys:
            return self.dfs(node.keys[self.word_to_search[i]], i + 1, n)

        else:
            return False

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """

        self.word_to_search = word
        if word[0] not in self.root.keys and word[0] != '.':
            return False
        else:
            return self.dfs(self.root, 0, len(word))

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
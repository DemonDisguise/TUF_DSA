# Word Ladder - I
""" Given are the two distinct words startWord and targetWord, and a list denoting wordList of unique words of equal lengths. Find the length of the shortest transformation sequence from startWord to targetWord..

In this problem statement, we need to keep the following conditions in mind:

A word can only consist of lowercase characters.
Only one letter can be changed in each transformation.
Each transformed word must exist in the wordList including the targetWord.
startWord may or may not be part of the wordList
Note:  If there's no possible way to transform the sequence from startWord to targetWord return 0. """


import sys
from collections import deque


def solve(word_list: list[str], start_word: str, target_word: str) -> int:
    word_set = set(word_list)
    if target_word not in word_set: return 0
    q = deque([start_word])
    if start_word in word_set:
        word_set.remove(start_word)
    
    level = 1
    
    while q:
        for _ in range(len(q)):
            word = q.popleft()
            
            if word == target_word:
                return level
            
            chars = list(word)
            
            for i in range(len(chars)):
                original = chars[i]
                
                for ch in "abcdefghijklmnopqrstuvwxyz":
                    if ch == original:
                        continue
                    
                    chars[i] = ch
                    new_word = "".join(chars)
                    
                    if new_word in word_set:
                        word_set.remove(new_word)
                        q.append(new_word)
                    
                    chars[i] = original
        
        level += 1
        
    return 0


if __name__ == "__main__":
    input = sys.stdin.readline
    word_list = list(input().strip().split())
    start_word, end_word = input().split()
    print(solve(word_list, start_word, end_word))

# hot dot dog lot log cog
# hit cog    
# Word Ladder - II
""" Given two distinct words startWord and targetWord, and a list denoting wordList of unique words of equal lengths. Find all shortest transformation sequence(s) from startWord to targetWord. You can return them in any order possible.

In this problem statement, we need to keep the following conditions in mind:
A word can only consist of lowercase characters.
Only one letter can be changed in each transformation.
Each transformed word must exist in the wordList including the targetWord.
startWord may or may not be part of the wordList.
Return an empty list if there is no such transformation sequence. """


import sys
from collections import deque

# The time complexity differs from test case to test case so gives TLE in leetcode (this code is for interviews), can be optimized using cp
""" def solve(word_list: list[str], start_word: str, target_word: str) -> list[list[str]]:
    word_set = set(word_list)
    if target_word not in word_set:
        return []
    
    q = deque([[start_word]])
    found = []
    visited_this_level = {start_word}
    
    while q and not found:
        level_visited = set()
        
        for _ in range(len(q)):
            curr = q.popleft()
            last_word = curr[-1]
            
            if last_word == target_word:
                found.append(curr)
                continue
            
            chars = list(last_word)
            for i in range(len(chars)):
                original = chars[i]
                for ch in "abcdefghijklmnopqrstuvwxyz":
                    if ch == original:
                        continue
                    
                    chars[i] = ch
                    new_word = "".join(chars)
                    
                    if new_word in word_set and new_word not in visited_this_level:
                        q.append(curr + [new_word])
                        level_visited.add(new_word)
                    
                    chars[i] = original
        
        visited_this_level.update(level_visited)
        word_set -= level_visited
    
    return found """                  
                    
# Instead of going from start and searching all paths, we go from the end searching the shortest path to start reducing the paths to check.
def solve(word_list: list[str], start_word: str, target_word: str) -> list[list[str]]:
    word_set = set(word_list)
    map = {}
    q = deque()
    q.append(start_word)
    map[start_word] = 1
    if start_word in word_set:
        word_set.remove(start_word)
    found = []
    
    def dfs(end_word: str, path: list[str]) -> None:
        if end_word == start_word:
            found.append(path[::-1])
            return
        
        chars = list(end_word)
        steps = map[end_word]
        
        
        for i in range(len(chars)):
            original = chars[i]
            
            for ch in "abcdefghijklmnopqrstuvwxyz":
                if ch == original: 
                    continue
                
                chars[i] = ch
                new_word = "".join(chars)
                
                if new_word in map and map[new_word] + 1 == steps:
                    path.append(new_word)
                    dfs(new_word, path)
                    path.pop()
                
                chars[i] = original
    
    while q:
        word = q.popleft()
        steps = map[word]
        chars = list(word)
        
        if word == target_word: break

        for i in range(len(chars)):
            original = chars[i]
            
            for ch in "abcdefghijklmnopqrstuvwxyz":
                if ch == original:
                    continue
                
                chars[i] = ch
                new_word = "".join(chars)
                
                if new_word in word_set:
                    q.append(new_word)
                    word_set.remove(new_word)
                    map[new_word] = steps + 1
                
                chars[i] = original
    
    if target_word in map:
        dfs(target_word, [target_word])
    
    return found

if __name__ == "__main__":
    lines = sys.stdin.readlines()
    start_word, target_word = lines[0].strip().split()
    word_list = list(lines[1].strip().split())
    res = solve(word_list, start_word, target_word)
    for path in res:
        print(*path)

# bat coz
# pat bot pot poz coz  
# Course Schedule I
""" There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false. """


import sys
from collections import deque


# BFS solution - Kahn's algorithm
def solve(num_courses: int, prerequisites: list[list[int]]) -> bool:
    graph = [[] for _ in range(num_courses)]
    
    for course, prerequisite in prerequisites:
        graph[prerequisite].append(course)
        
    indegree = [0] * num_courses
    
    for node in range(num_courses):
        for neighbour in graph[node]:
            indegree[neighbour] += 1
    
    q = deque()
    for node in range(num_courses):
        if indegree[node] == 0:
            q.append(node)
    
    completed = 0
    while q:
        node = q.popleft()
        completed += 1
        
        for neighbour in graph[node]:
            indegree[neighbour] -= 1
            
            if not indegree[neighbour]:
                q.append(neighbour)
    
    return completed == num_courses     


# DFS solution - cycle detection in directed graph
""" def _dfs(node: int, graph: list[list[int]], visited: list[int]) -> bool:
    visited[node] = 2
    
    for neighbour in graph[node]:
        if not visited[neighbour]:
            if _dfs(neighbour, graph, visited):
                return True
        elif visited[neighbour] == 2:
            return True
        
    visited[node] = 1
    return False


def solve(num_courses: int, prerequisites: list[list[int]]) -> bool:
    graph = [[] for _ in range(num_courses)]
    
    for course, prerequisite in prerequisites:
        graph[prerequisite].append(course)
        
    visited = [0] * num_courses
    
    for node in range(num_courses):
        if not visited[node]:
            if _dfs(node, graph, visited):
                return False
    
    return True """


if __name__ == "__main__":
    lines = sys.stdin.readlines()
    courses = int(lines[0].strip())
    prerequisites = []
    for line in lines[1:]:
        prerequisites.append(list(map(int, line.strip().split())))
    print(solve(courses, prerequisites))

""" 
3
1 0
2 1
3 2 
"""
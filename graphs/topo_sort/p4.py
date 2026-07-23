# Course Schedule II
""" There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array. """


import sys
from collections import deque


# bfs kahn's algorithm
def solve(num_courses: int, prerequisites: list[list[int]]) -> list[int]:
    graph = [[] for _ in range(num_courses)]
    indegree = [0] * num_courses

    for course, prerequisite in prerequisites:
        graph[prerequisite].append(course)
        indegree[course] += 1
    
    q = deque()
    for node in range(num_courses):
        if not indegree[node]:
            q.append(node)
    
    topo = []
    while q:
        node = q.popleft()
        topo.append(node)
        
        for neighbour in graph[node]:
            indegree[neighbour] -= 1
            
            if not indegree[neighbour]:
                q.append(neighbour)
    
    return topo if len(topo) == num_courses else []


# dfs + topo sort 
""" def _dfs(node: int, graph: list[list[int]], visited: list[int], stack: list[int]) -> None:
    visited[node] = 2
    
    for neighbour in graph[node]:
        if not visited[neighbour]:
            if _dfs(neighbour, graph, visited, stack):
                return True
        elif visited[neighbour] == 2:
            return True
    
    visited[node] = 1
    stack.append(node)
    return False


def solve(num_courses: int, prerequisites: list[list[int]]) -> list[int]:
    graph = [[] for _ in range(num_courses)]
    
    for course, prerequisite in prerequisites:
        graph[prerequisite].append(course)
    
    visited = [0] * num_courses
    stack = []
    
    for node in range(num_courses):
        if not visited[node]:
            if _dfs(node, graph, visited, stack):
                return []
                
    return stack[::-1] """ 


if __name__ == "__main__":
    lines = sys.stdin.readlines()
    courses = int(lines[0])
    prerequisites = []
    for line in lines[1:]:
        prerequisites.append(list(map(int, line.strip().split())))
    print(*solve(courses, prerequisites))

"""
2
0 1
1 0
"""

"""
4
1 0
2 0
3 1
3 2
"""
    
from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {}
        required = [0]*numCourses
        for i in range(numCourses):
            preMap[i] = []
        for course, preReq in prerequisites:
            preMap[preReq].append(course)
            required[course] += 1
        q = deque()
        for i in range(numCourses):
            if required[i] == 0:
                q.append(i)
        output = []
        while q:
            curr = q.popleft()
            output.append(curr)
            for course in preMap[curr]:
                required[course] -= 1
                if required[course] == 0:
                    q.append(course)
        if len(output) == numCourses:
            return output
        return []

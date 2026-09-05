class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {}
        for i in range(numCourses):
            preMap[i] = []
        for course, prereq in prerequisites:
            preMap[course].append(prereq)
        visited, inCycle = set(), set()
        output = []
        def dfs(course):
            if course in inCycle:
                return False
            if course in visited:
                return True
            inCycle.add(course)
            for pre in preMap[course]:
                if not dfs(pre):
                    return False
            inCycle.remove(course)
            visited.add(course)
            output.append(course)
            return True
        for i in range(numCourses):
            if not dfs(i):
                return []
        return output
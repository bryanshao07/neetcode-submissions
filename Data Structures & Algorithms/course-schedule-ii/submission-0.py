class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {}
        for i in range(numCourses):
            preMap[i] = []
        for course, preReq in prerequisites:
            preMap[course].append(preReq)
        output = []
        visit, cycle = set(), set() 
        def dfs(course):
            if course in cycle:
                return False
            if course in visit:
                return True
            cycle.add(course)
            for pre in preMap[course]:
                if dfs(pre) == False:
                    return False
            cycle.remove(course)
            visit.add(course)
            output.append(course)
            return True
        for i in range(numCourses):
            if dfs(i) == False:
                return []
        return output
        
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #graph: prereq -> courses that need it
        graph = {}
        for i in range(numCourses):
            graph[i] = []

        #how many prereqs does a course have
        inDegrees = [0]*numCourses

        for course, prereq in prerequisites:
            graph[prereq].append(course)
            inDegrees[course] +=1
        
        q = collections.deque()
        for i in range(numCourses):
            if inDegrees[i] == 0:
                q.append(i)
        path = []
        visited = set()

        while q:
            curr = q.popleft()
            path.append(curr)
            visited.add(curr)
            for course in graph[curr]:
                inDegrees[course] -= 1
                if inDegrees[course] == 0 and course not in visited:
                    q.append(course)
        return True if len(path) == numCourses else False
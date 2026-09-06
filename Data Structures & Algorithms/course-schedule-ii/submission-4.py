class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # prereq -> courses that need it 
        graph = {} 

        #how many prereqs a course has
        inDegree = [0]*numCourses

        output = []
        for i in range(numCourses):
            graph[i] = []
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            inDegree[course] += 1
        q = collections.deque()
        for i in range(numCourses):
            if inDegree[i] == 0:
                q.append(i)
        while q:
            curr = q.popleft()
            output.append(curr)
            for course in graph[curr]:
                inDegree[course] -= 1
                if inDegree[course] == 0:
                    q.append(course)
        return output if len(output) == numCourses else []

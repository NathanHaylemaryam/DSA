class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        indegree = [0] * numCourses
        

        for pre, course in prerequisites:
            graph[pre].append(course)
            indegree[course] += 1
        
        prereq = [set() for _ in range(numCourses)]
        

        q = deque([i for i in range(numCourses) if indegree[i] == 0])
        
        while q:
            cur = q.popleft()
            for nxt in graph[cur]:
          
                prereq[nxt].add(cur)
                prereq[nxt] |= prereq[cur]
                
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    q.append(nxt)
        
        res = []
        for u, v in queries:
            res.append(u in prereq[v])
        return res
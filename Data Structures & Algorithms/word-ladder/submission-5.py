class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        neighbors = collections.defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for char in range(len(word)):
                pattern = word[:char] + "*" + word[char + 1:]
                neighbors[pattern].append(word)
        
        visited = set()
        q = deque([beginWord])
        ret = 1
        visited.add(beginWord)
        while q:
            for i in range(len(q)):
                curr = q.popleft()
                if curr == endWord:
                    return ret
                for char in range(len(curr)):
                    pattern = curr[:char] + "*" + curr[char + 1:]
                    for neighborWord in neighbors[pattern]:
                        if neighborWord not in visited:
                            q.append(neighborWord)
                            visited.add(neighborWord)
            ret += 1
        return 0
            
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        neighbors = collections.defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i]+"*"+word[i+1:]
                neighbors[pattern].append(word)
                
        visited = set()
        q = deque([beginWord])
        visited.add(beginWord)
        result = 1
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return result
                for i in range(len(word)):
                    pattern = word[:i]+"*"+word[i+1:]
                    for neighborWord in neighbors[pattern]:
                        if neighborWord not in visited:
                            visited.add(neighborWord)
                            q.append(neighborWord)
            result +=1
        return 0
                
        
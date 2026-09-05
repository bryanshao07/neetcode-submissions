class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        neighbors = collections.defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*"+word[i+1:]
                neighbors[pattern].append(word)

        visited = set()
        visited.add(beginWord)
        q = deque([beginWord])
        ret = 1
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return ret
                for j in range(len(word)):
                    pattern = word[:j] + "*"+word[j+1:]
                    for neighborWord in neighbors[pattern]:
                        if neighborWord not in visited:
                            visited.add(neighborWord)
                            q.append(neighborWord)
            ret += 1
        return 0
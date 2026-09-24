class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        neighbors = collections.defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                neighbors[pattern].append(word)
        visited = set()
        q = collections.deque()
        q.append(beginWord)
        visited.add(beginWord)
        output = 1
        while q:
            for j in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return output
                for i in range(len(word)):
                    pattern = word[:i] + "*" + word[i+1:]
                    for neighborWord in neighbors[pattern]:
                        if neighborWord not in visited:
                            q.append(neighborWord)
                            visited.add(neighborWord)
            output += 1
        return 0
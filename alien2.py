class Solution:
    def alienOrder(self, words: List[str]) -> str:
        """TC- Let C be the total length of all the words in the input list, added together. - O(c);
        n be the total number of strings bu they are said to be constant
        so o(1) for it
        unique letters in the alhphabet are also constant 26 so O(1)

        sc also o(1) but can go till min (usquare, n )
        """
        result = ""
        if words is None:
            return result
        self.hashmap = {}
        self.indegree = [0] * 26
        self.buildgraph(words)
        """        
        we have indegree and adjacency list
        so now we make a queue
        independent elements to be added in the q
        """
        q = collections.deque()
        for k in self.hashmap.keys():
            if self.indegree[ord(k) - ord('a')] == 0:
                q.append(k)
                result += k

        while q:
            ##visit babies and reduce their degrees
            c = q.popleft()
            self.indegree[ord(c) - ord('a')] -= 1
            children = self.hashmap[c]
            if children is not None:
                for child in children:
                    self.indegree[ord(child) - ord('a')] -= 1
                    if self.indegree[ord(child) - ord('a')] == 0:
                        q.append(child)
                        result += child
        if len(result) == len(self.hashmap):
            return result
        else:
            return ""

    def buildgraph(self, word):
        for w in word:
            for i in range(len(w)):
                c = w[i]
                if c not in self.hashmap:
                    self.hashmap[c] = []
                # else:
                #     hashmap[c].append()
        for i in range(len(word) - 1):
            out = word[i]
            inw = word[i + 1]

            m = len(out)
            n = len(inw)
            if m > n and out.startswith(inw):
                ###invalid
                self.hashmap.clear()
                return
            # for j in range(m):
            j = 0
            while j < m and j < n:
                outchar = out[j]
                inchar = inw[j]
                if outchar != inchar:
                    self.indegree[ord(inchar) - ord('a')] += 1
                    self.hashmap[outchar].append(inchar)
                    break
                j += 1













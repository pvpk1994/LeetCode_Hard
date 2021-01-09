# Word Ladder - Using Breadth First Search
# Leetcode Hard 
# Time Complexity: O(M^2*N) - M is the len(word) and N is the total number of words in WordList
# Leetcode Question: https://leetcode.com/problems/word-ladder/solution/

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        lowercase =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p'
                   ,'q','r','s','t','u','v','w','x','y','z']
        # Convert into hash-set as the words in worlist are already unique
        hash_set = set(wordList)
        # basic check : if endword is not in hash_set: cannot reach so output: 0
        if endWord not in hash_set:
            print("poop")
            return 0
        # Initialize a queue for Breadth-frist search --> Level order traversal
        # Init queue with beginWord
        que = deque([beginWord,])
        # IInit the level for BFS
        level =1
        # perform actual BFS starting here
        while que:
            len_q = len(que)
            # print(len_q)
            for _ in range(0, len_q):
                word = que.popleft()
                # python strings are immutable 
                for j in range(0, len(word)):
                    original_char = word[j]
                    for c in lowercase:
                        if word[j] == c:
                            continue
                        word = word[0:j]+c+word[j+1:]
                        # print(word)
                        if word == endWord:
                            return level+1
                        if word in hash_set:
                            # append it to que
                            que.append(word)
                            # print(que)
                            # Remove it from the hash-set 
                            hash_set.remove(word)
                    word = word[0:j]+original_char+word[j+1:]
            level+=1 
            
        return 0

#without data structure O(NM) N-number M-length K-number with constraint length
class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict=set()
        

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        self.dict.add(word)
        
    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        for i in self.dict:
            if len(i)==len(word):
                idx=0
                for j in word:
                    if j =='.' or j==i[idx]:
                        idx+=1
                    else:
                        break
                if idx==len(i):
                    return True
        return False
                
#without data structure but limitations O(MK) K<<N 92ms 19.6MB
class WordDictionary(object):
    def __init__(self):
        self.dict = collections.defaultdict(list)
        

    def addWord(self, word):
        if word:
            self.dict[len(word)].append(word)

    def search(self, word):
        if not word or len(self.dict)==0:
            return False
        if '.' not in word:
            return word in self.dict[len(word)]
        for v in self.dict[len(word)]:
            for idx,char in enumerate(word):
                if char != v[idx] and char != '.':
                    break
            else:
                return True
        return False

#Trie+DFS O(M)+O(M) 384ms,27.1MB 
class TrieNode(object):
    def __init__(self):
        self.word = False
        self.children = {}
class WordDictionary(object):
    def __init__(self):
        self.trie={}
    def addWord(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.word = True
    def search(self, word):
        return self.searchFrom(self.root, word)
    def searchFrom(self, node, word):
        for i in range(len(word)):
            c = word[i]
            if c == '.':
                for k in node.children:
                    if self.searchFrom(node.children[k], word[i+1:]):
                        return True
                return False
            elif c not in node.children:
                return False
            node = node.children[c]
        return node.word
# use dict to build a trie tree 292 ms 21.9MB
class WordDictionary(object):

    def __init__(self):
        self.trie = {}
    def addWord(self, word):
        trie = self.trie
        for c in word:
            trie = trie.setdefault(c, {})
        trie['word'] = word
        
    def search(self, word):
        return self.helper(self.trie, word)
    
    def helper(self, trie, word):
        if not word:
            return True if trie.get('word') else False
        if word[0] == '.':
            for c in trie:
                if c != 'word' and self.helper(trie[c], word[1:]):
                    return True
        elif word[0] in trie:
            return self.helper(trie[word[0]], word[1:])
        return False

class Solution:
    def canConstruct(self, ransomNote: list, magazine: list) -> bool:
        # for i in ransomNote:
        #     if i not in magazine:
        #         return False
        map1 = {}
        map2 = {}
        map1 = {i:ransomNote.count(i) for i in set(ransomNote)}
        map2 = {i:magazine.count(i) for i in set(magazine)}
        try:
            for i in map1:
                if map1[i] > map2[i]:
                    return False
        except:
            return False
        return True
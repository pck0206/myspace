class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        a = {}
        for i in strs:
            k = "".join(sorted(i))
            if k in a:
                a[k].append(i)
            else:
                a[k] = [i]
        return list(a.values())
strs = ["act","pots","tops","cat","stop","hat"]
print(Solution().groupAnagrams(strs))


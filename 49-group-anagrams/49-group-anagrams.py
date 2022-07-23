class Solution:
    def groupAnagrams(self, strs):
        anagrams = defaultdict(list)
        for s in strs:
            key = s.sort()
            anagrams[key].append(s)
        groupedAnagrams = []
        for key in anagrams:
            groupedAnagrams.append(anagrams[key])
        return groupedAnagram
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq_temp = [0] * 26
        uq_freqs = {}
        for s in strs:
            s_freq = freq_temp.copy()
            for c in s:
                s_freq[ord(c) - 97] += 1
            s_freq = tuple(s_freq)
            if s_freq in uq_freqs:
                uq_freqs[s_freq].append(s)
            else:
                uq_freqs[s_freq] = [s]
        return list(uq_freqs.values())
        
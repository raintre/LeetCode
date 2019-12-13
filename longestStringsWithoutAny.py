class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        :type s: str
        :rtype: int
        """
        output = 0
        track = ""
        for char in s:
            if char in track:
                while True:
                    if track[0] == char:
                        track = track[1:]
                        track += char
                        break
                    else:
                        track = track[1:]
            else:
                track += char
            if len(track) > output:
                output = len(track)
        return output

def lengthOfLongestSubstring(self, s):
    """
    :type s: str
    :rtype: int
    """
    
    str_list = []
    max_length = 0
    
    for x in s:
        if x in str_list:
            str_list = str_list[str_list.index(x)+1:]
            
        str_list.append(x)    
        max_length = max(max_length, len(str_list))
        
    return max_length
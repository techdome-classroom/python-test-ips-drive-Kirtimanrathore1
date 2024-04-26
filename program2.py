def longest_substring(s: str) -> int:
    
    """"
    
    Implement the function longest_substring 
    using the provided longest_substring function to find 
    the length of the longest substring without repeating characters.

    """ 
  
    if not s:
        return 0

    max_length = 0
    start = 0
    char_index_map = {}

    for end in range(len(s)):
        if s[end] in char_index_map:
            
            start = max(start, char_index_map[s[end]] + 1)

       
        char_index_map[s[end]] = end

       
        max_length = max(max_length, end - start + 1)

    return max_length


input_str = "abcabcbb"
print("Input:", input_str)
print("Output:", longest_substring(input_str))






class Solution:
    
    # Function to check if two strings are isomorphic.
    def areIsomorphic(self, str1, str2):
        # If lengths are not equal, they can't be isomorphic.
        if len(str1) != len(str2):
            return False
        
        # Initialize dictionaries to store mapping from str1 to str2 and vice versa.
        mapping_str1_to_str2 = {}
        mapping_str2_to_str1 = {}
        
        # Iterate through each character in both strings.
        for char1, char2 in zip(str1, str2):
            # Check if the current character in str1 has been mapped to a different character in str2.
            if char1 in mapping_str1_to_str2 and mapping_str1_to_str2[char1] != char2:
                return False
            
            # Check if the current character in str2 has been mapped to a different character in str1.
            if char2 in mapping_str2_to_str1 and mapping_str2_to_str1[char2] != char1:
                return False
            
            # If the characters are not mapped, create a mapping.
            if char1 not in mapping_str1_to_str2:
                mapping_str1_to_str2[char1] = char2
            
            if char2 not in mapping_str2_to_str1:
                mapping_str2_to_str1[char2] = char1
        
        # If all characters are mapped without conflicts, the strings are isomorphic.
        return True

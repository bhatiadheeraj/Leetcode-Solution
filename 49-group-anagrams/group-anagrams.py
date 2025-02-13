class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1 :
            return [[strs[0]]]
        # Input: strs = ["eat","tea","tan","ate","nat","bat"]
        # Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
        ret = []
        input_to_sorted = {

        }
        string_to_anangram = {
        }
        for input in strs:
            sorted_input = sorted(input)
            input_match = get_key_by_value(input_to_sorted, sorted_input) 
            if input_match != None:
                string_to_anangram[input_match].append(input)
            else:
                input_to_sorted[input] = sorted_input
                string_to_anangram[input] = [input]
        
        print(string_to_anangram)

        for key,values in string_to_anangram.items():
           ret.append(values)

        return ret

    
def get_key_by_value(input_dict, val):
    for key,value in input_dict.items():
        if value == val:
            return key
    return None






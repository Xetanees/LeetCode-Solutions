import json

class Solution(object):
    """
    Description:
        You are given a string s and an integer k. Find the length of the longest substring 
        that contains at most k distinct characters.

    Constraints:
        1 <= s.length <= 5 * 10^4
        0 <= k <= 50
        
    """
    def longestUniqueSubstringAnnotated(self, s, k):
        """
        :type arr: List[int]
        :rtype: int
        """
        from collections import defaultdict
        
        window = defaultdict(int)
        left = 0

        for c in s:
            print(dict(window))
            print(f"Add {c}")
            window[c] += 1
            print(dict(window))

            #Retains best potential string length (left to len(s))
            if len(window) > k:
                print(f"len(window) > {k}. Decrement window['{s[left]}']")
                window[s[left]] -= 1
                print(dict(window))
                
                if window[s[left]] == 0:
                    print(f"window['{s[left]}'] = 0, removing")
                    del window[s[left]]
                    print(dict(window))
                left += 1
            
            print(f"Best potentional: {len(s) - left}")
            print()

        print(f"Best: {len(s) - left}\n")

        return len(s) - left
    
    def longestUniqueSubstring(self, s, k):
        """
        :type arr: List[int]
        :rtype: int
        """
        from collections import defaultdict

        window = defaultdict(int)
        left = 0

        for c in s:
            window[c] += 1

            if len(window) > k:
                window[s[left]] -= 1

                if window[s[left]] == 0:
                    del window[s[left]]

                left += 1

        return len(s) - left

def main():
    #Setup of solution with LeetCode example input
    solution = Solution()
    
    with open('./Problem Inputs/_Example_1_Input.json') as f:
        JSON = json.loads(f.read())

    for object in JSON:
        print(f"Input: s = {object['s']}, k = {object['k']}")
        output = solution.longestUniqueSubstring(object['s'], object['k'])
        print(f"Output: {output}")
        print(f"Expected Output: {object['expected']}")

        if output == object['expected']:
            print("PASS")
        else:
            print("FAIL")
        print()

if __name__ == "__main__":
    main()
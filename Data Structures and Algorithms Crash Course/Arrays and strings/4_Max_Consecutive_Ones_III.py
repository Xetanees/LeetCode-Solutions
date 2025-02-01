import json

class Solution(object):
    """
    Constraints:
        1 <= nums.length <= 10^5
        nums[i] is either 0 or 1.
        0 <= k <= nums.length
    """
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left = curr = ans = 0
        
        for right, num in enumerate(nums):
            if num == 0:
                curr += 1
            
            while curr > k:
                if nums[left] == 0:
                    curr -= 1
                left += 1
                
            ans = max(ans, right - left + 1)
            
        return ans

def main():
    #Setup of solution with LeetCode example input
    solution = Solution()
    
    with open('./Problem Inputs/4_Input.json') as f:
        JSON = json.loads(f.read())

    for object in JSON:
        print(f"Input: nums = {object['nums']}, k = {object['k']}")
        output = solution.longestOnes(object['nums'], object['k'])
        print(f"Output: {output}")
        print(f"Expected Output: {object['expected']}")

        if output == object['expected']:
            print("PASS")
        else:
            print("FAIL")
        print()

if __name__ == "__main__":
    main()
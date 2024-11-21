class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        nums_dict = {}
        nums_set = set(nums)
        for num in nums_set:
            num_count = nums.count(num)
            if num_count not in nums_dict:
                nums_dict[num_count] = [num]
            else:
                nums_dict[num_count].append(num)

        frequencies = sorted(list(nums_dict.keys()), reverse = True)
        res = []
        i=0
        while i < len(frequencies) and i < k:
            j = 0
            while j < len(nums_dict[frequencies[i]]) and len(res)<k:
                res.append(nums_dict[frequencies[i]][j])
                j+=1
                #res.append(num)
            i+=1
        return res
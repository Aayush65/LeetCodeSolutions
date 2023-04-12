class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        preSum = [0]
        for i in nums:
            preSum.append(preSum[-1] + i)

        hashset = {nums[i] for i in range(k)}
        hashmap = defaultdict(int)
        for i in range(k):
            hashmap[nums[i]] += 1

        maxSum = preSum[k] if len(hashset) == k else 0
        for i in range(k, len(nums)):
            if nums[i - k] in hashset:
                if hashmap[nums[i - k]] == 1:
                    hashset.remove(nums[i - k])
                hashmap[nums[i - k]] -= 1
            hashset.add(nums[i])
            hashmap[nums[i]] += 1
            if len(hashset) == k:
                maxSum = max(maxSum, preSum[i + 1] - preSum[i - k + 1])
        return maxSum
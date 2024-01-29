class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = set()


        sortNums = sorted(nums)

        for i in range(len(nums)):
            j = i+1
            z = len(nums) - 1

            while (j < z):
                if (sortNums[i] + sortNums[j] + sortNums[z] == 0):
                    answer.add((sortNums[i], sortNums[j], sortNums[z]))
                    j += 1
                elif (sortNums[i] + sortNums[j] + sortNums[z] > 0):
                    z -= 1
                elif (sortNums[i] + sortNums[j] + sortNums[z] < 0):
                    j += 1
        
        return answer
class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        people.sort()
        n = len(people)
        left, right = 0, n - 1
        boats = 0
        while left <= right:
            if people[left] + people[right] > limit:
                right -= 1
                boats += 1
            else:
                left += 1
                right -= 1
                boats += 1
        return boats

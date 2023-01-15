from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        Smax = 0
        index1h=0
        index2h = (len(height)-1)
        while index2h > index1h:
            Smax = max(Smax,(min(height[index2h],height[index1h]) * (index2h-index1h)))
            if height[index1h] > height[index2h]:
                index2h-=1
            else:
                index1h+=1             
        return Smax


def main():
    """Проверка алгоритма"""
    ex_S=Solution()
    height = [1,8,6,2,5,4,8,3,7]
    print(ex_S.maxArea(height))

    height = [1,1]
    print(ex_S.maxArea(height))

    height = [1]
    print(ex_S.maxArea(height))


if __name__ == "__main__":
    main()
'''
题目：二维数组中，每行从左到右递增，每列从上到下递增，给出一个数，判断它是否在数组中
思路：从左下角或者右上角开始比较
'''
# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        if not array:
            return False
        i=0
        j=len(array[0])-1
        while i<len(array) and j>=0:
            if array[i][j]==target:
                return True
            if array[i][j]<target:
                i+=1
            elif array[i][j]>target:
                j-=1
        return False

target=7
array=[[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]

s=Solution()

print(s.Find(target,array))

assert s.Find(target,array)==True
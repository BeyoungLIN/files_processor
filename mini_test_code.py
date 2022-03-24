# -*- coding: utf-8 -*-
# @Time   : 2021/12/29 20:09
# @Author : beyoung
# @Email  : linbeyoung@stu.pku.edu.cn
# @File   : mini_test_code.py

# import math
# a = math.ceil(float(5)/2)
# print(a)

def heapify(parent_index, length, nums):
    temp = nums[parent_index]
    child_index = 2 * parent_index + 1
    while child_index < length:
        if child_index + 1 < length and nums[child_index + 1] > nums[child_index]:
            child_index = child_index + 1
        if temp > nums[child_index]:
            break
    nums[parent_index] = nums[child_index]
    parent_index = child_index
    child_index = 2 * parent_index + 1
    nums[parent_index] = temp


def heapsort(nums):
    for i in range((len(nums) - 2) // 2, -1, -1):
        heapify(i, len(nums), nums)

    for j in range(len(nums) - 1, 0, -1):
        nums[j], nums[0] = nums[0], nums[j]
        heapify(0, j, nums)


def mergesort(nums, left, right):
    if right <= left:
        return
    mid = (left + right) >> 1
    mergesort(nums, left, mid)
    mergesort(nums, mid + 1, right)
    merge(nums, left, mid, right)


def merge(nums, left, mid, right):
    temp = []
    i = left
    j = mid + 1
    while i <= mid and j <= right:
        if nums[i] <= nums[j]:
            temp.append(nums[i])
            i += 1
        else:
            temp.append(nums[j])
            j += 1
    while i <= mid:
        temp.append(nums[i])
        i += 1
    while j <= right:
        temp.append(nums[j])
        j += 1
        nums[left:right + 1] = temp


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quickSort(nums, 0, len(nums) - 1)
        return nums

    def quickSort(self, arr, l, r):
        if l >= r:
            return
        pivot = self.partition(arr, l, r)
        self.quickSort(arr, l, pivot)
        self.quickSort(arr, pivot + 1, r)

    def partition(self, a, l, r):
        pivot = random.randint(l, r)
        pivotVal = a[pivot]
        while l <= r:
            while a[l] < pivotVal:
                l += 1
            while a[r] > pivotVal:
                r -= 1
            if l == r:  # 说明排好了?
                break
            if l < r:
                a[l], a[r] = a[r], a[l]
                l += 1
                r -= 1
        return r


def heapify(parent_index, length, nums):
    temp = nums[parent_index]
    child_index = 2 * parent_index + 1


while child_index < length:
    if child_index + 1 < length and nums[child_index + 1] > nums[child_index]:
        child_index = child_index + 1
    if temp > nums[child_index]:
        break
    nums[parent_index] = nums[child_index]
    parent_index = child_index
    child_index = 2 * parent_index + 1
    nums[parent_index] = temp


def heapsort(nums):
    for i in range((len(nums) - 2) // 2, -1, -1):
        heapify(i, len(nums), nums)
        for j in range(len(nums) - 1, 0, -1):
            nums[j], nums[0] = nums[0], nums[j]
            heapify(0, j, nums)

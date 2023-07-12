"""
Given the list of integers ( positive , negative, zeros)
Find max multiplication of three values in list
l1 = [-7, 1, 2, 0, 3, 12, -24, 5, -1, 6]

Input: [-1, 1, 2, 0, 3, 12, 4, 5, -1, 6]
Output: Max value = "360". Nums are: (12, 5, 6)

Input: [-7, 1, 2, 0, 3, 12, -24, 5, -1, 6]
Output: Max value = "2016". Nums are: (-7, 12, -24)
"""
def find_max_product(nums):
    max1 = max2 = max3 = float('-inf')
    min1 = min2 = float('inf')

    for num in nums:
        if num > max1:
            max3 = max2
            max2 = max1
            max1 = num
        elif num > max2:
            max3 = max2
            max2 = num
        elif num > max3:
            max3 = num

        if num < min1:
            min2 = min1
            min1 = num
        elif num < min2:
            min2 = num

    product1 = max1 * max2 * max3
    product2 = max1 * min1 * min2

    if product1 > product2:
        nums_used = (max1, max2, max3)
        max_product = product1
    else:
        nums_used = (max1, min1, min2)
        max_product = product2

    return max_product, nums_used


# Example usage:
l1 = [-7, 1, 2, 0, 3, 12, -24, 5, -1, 6]
max_product, used_nums = find_max_product(l1)
print("Max value =", max_product)
print("Nums are:", used_nums)
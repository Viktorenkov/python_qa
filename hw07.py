"""
Convert a non-negative integer num to its English words representation.
Example 1:
Input: num = 123
Output: "One Hundred Twenty Three"

let's take that number always > 100 and only three digits
100 <= num <= 999
"""


def numberToWords(num):
    # Define the words for numbers up to 19
    less_than_20 = [
        "", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine",
        "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen",
        "Seventeen", "Eighteen", "Nineteen"
    ]
    # Define the words for tens
    tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
    # Define the words for thousands
    thousands = ["", "Thousand", "Million", "Billion"]

    if num == 0:
        return "Zero"

    def convert_three_digits(n):
        if n == 0:
            return ""
        elif n < 20:
            return less_than_20[n] + " "
        elif n < 100:
            return tens[n // 10] + " " + convert_three_digits(n % 10)
        else:
            return less_than_20[n // 100] + " Hundred " + convert_three_digits(n % 100)

    result = ""
    for i in range(len(thousands)):
        if num % 1000 != 0:
            result = convert_three_digits(num % 1000) + thousands[i] + " " + result
        num //= 1000

    return result.strip()


# Test the function
num = 333
print(numberToWords(num))

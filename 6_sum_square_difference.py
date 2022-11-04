# The sum of the squares of the first ten natural numbers is, 1**2 + 2**2 + ... + 10**2 = 385
# The square of the sum of the first ten natural numbers is, (1+2+...+10)**2 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025-385=2640.
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

class Solution:
    def sum_square_difference(max_val: int) -> int:
        sum_of_sqs = 0
        total = 0
        for n in range(1,max_val+1):
            total += n
            sum_of_sqs += n**2

        return total**2 - sum_of_sqs

# tests
tests = [ 
    (10, 2640),
    (100, 25164150)
]

for max_val, solution in tests:
    sol = Solution.sum_square_difference(max_val)
    # print(sol)
    print( sol == solution )
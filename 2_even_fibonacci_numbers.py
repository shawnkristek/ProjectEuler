# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

class Solution:
    def evenFibonacciSum(upto: int) -> int:

        last = 1
        next = 2
        _sum = 0
        while (next < upto):
            if next % 2 == 0:
                _sum += next
            temp = next
            next += last
            last = temp
        return _sum

# tests
tests = [ 
    ( 20,   10),
    (
        4000000,
        4613732 
    )
]

for upto, solution in tests:
    sol = Solution.evenFibonacciSum(upto)
    # print(sol)
    print( sol == solution )
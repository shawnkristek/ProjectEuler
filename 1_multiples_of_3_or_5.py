# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

class Solution:
    def sumMultiples35(upto: int) -> int:

        multiples = set()
        i = 1
        while (i*3 < upto):
            multiples.add(i*3)

            if i*5 < upto:
                multiples.add(i*5)
        
            i += 1
        return sum(multiples)
        

# tests
tests = [ 
    (
        10,     23
    ),
    (
        1000,   233168
    )
]

for upto, solution in tests:
    sol = Solution.sumMultiples35(upto)
    # print(sol)
    print( sol == solution )
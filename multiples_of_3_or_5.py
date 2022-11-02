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
    print(sol)
    print( sol == solution )
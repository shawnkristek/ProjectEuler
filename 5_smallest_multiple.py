from math import prod
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

class Solution:
    def smallestMultiple(start: int, end: int) -> int:
        """ Returns the smallest number that satisfies Ans%[start:end] == 0. """
        prime_factors = {}
        factors_seen = set() 
        # find prime factors for each number
        for n in range(start, end+1):
            num = n
            while num > 1:
                if num % 2 == 0:
                    factor = 2
                if num % 3 == 0:
                    factor = 3
                if num%2!=0 and num%3!=0:
                    factor = num
                prime_factors[n] = prime_factors.get(n, [])
                prime_factors[n].append(factor)
                factors_seen.add(factor)
                num = num // factor            

        # append highest count of a prime factor to final calculation
        output = []
        for f in factors_seen:
            f_max_count = 0
            for k,v in prime_factors.items():
                f_max_count = max(v.count(f), f_max_count)
            for i in range(f_max_count):
                output.append(f)

        return prod(output)

        

# tests
tests = [ 
    (1, 10, 2520),
    (1, 20, 232792560),
]

for start, end, solution in tests:
    sol = Solution.smallestMultiple(start, end)
    # print(sol)
    print( sol == solution )
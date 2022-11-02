import math

# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

class Solution:
    def largestPrimeFactor(num: int) -> int:
        # def isPrime(num: int) -> bool:
        #     for i in range(2,int(math.sqrt(num))+1):
        #         if (num%i) == 0:
        #             return False
        #     return True
        n = num
        max_factor = 1
        while n % 2 == 0:
            max_factor = 2
            n = n / 2

        for i in range(3,int(math.sqrt(n))+1, 2):
            while (n % i == 0):
                max_factor = i
                n = n / i

        if n > 2:
            max_factor = n

        return max_factor

# tests
tests = [ 
    ( 13195,    29),
    ( 600851475143, 6857 ) # timeout
]

for num, solution in tests:
    sol = Solution.largestPrimeFactor(num)
    # print(sol)
    print( sol == solution )
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

class Solution:
    def findPrime(num: int) -> int:
        """ using num as a counter within the list of all prime numbers, return prime at that location """
        """ 6*num - 1 and 6*num + 1 then eliminate multiples of prime numbers """
        # calculate prime at i using 6*i +/- 1... issue with this approach is the need to eliminate multiples...
        # calculate primes using 6*i+/-1 and testing for primes, counting as we go. no need to store more than two prime values
        # space 0(1)
        # time 0(num) for main algorithm... this increases when considering the isPrime testing... 0(num*sqrt(num))

        def isPrime(num: int) -> bool:
            if num < 2: return False
            for x in range(2, int(num**0.5) + 1):
                if num % x == 0:
                    return False
            return True

        primes = [2,3]
        counter = 2
        i = 0
        while counter < num:
            i += 1
            j = 0
            if isPrime(6*i-1):
                primes[j] = 6*i-1
                counter += 1
                j = 1
            if isPrime(6*i+1):
                primes[j] = 6*i+1
                counter += 1

        if counter == num:
            return primes[j]
        else:
            return primes[0]

# tests 
tests = [ 
    (10, 29),
    (10001, 104743),
]

for num, solution in tests:
    sol = Solution.findPrime(num)
    # print(sol)
    print( sol == solution )
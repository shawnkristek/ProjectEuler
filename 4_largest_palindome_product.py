# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

class Solution:
    def largestPalindromeProduct(min_val: int, max_val: int) -> int:
        """
            - find largest palidromic product of two 3-digit numbers
            - starting with highest possible value the next largest palindromic number can be found by mirroring the digits
                ex. start=998001  6 digits, mirror first 3 => 998899 but this is larger, decrease third mirror digit and repeat => 997799
            - next we need to check if two three digit numbers have a product equal to 997799
            - check by modulus 999, then 998... if %n > 999 before finding a solution, move to next palindromic
        """

        # def isPalindrome(s: str) -> bool:
        #     """ Checks if string is palindrome. """
        #     l, r = 0, -1
        #     while (l < len(s)+r):
        #         if s[l] != s[r]:
        #             return False
        #         l += 1
        #         r -= 1
        #     return True

        def nextPalidromic(num: int) -> int:
            """ Returns the next largest palindomic number. result < num ... assumes even number of digits """
            string = str(num)
            first_half_str = string[:len(string)//2]
            first_half_int = int(first_half_str)

            _next = int(first_half_str + first_half_str[::-1])
            # this likely only does 1 iteration, TODO work out a proof to justify eliminating loop
            while _next >= num:
                first_half_int -= 1 # potential error if number were to go negative
                first_half_str = str(first_half_int)
                _next = int(first_half_str + first_half_str[::-1])
            return _next

        pal = nextPalidromic(max_val*max_val)
        # loop for all palindromic numbers < max_val*max_val
        while pal > 0:
            # check multiples
            n = max_val
            quo = pal // n
            while ( quo <= max_val ):
                if pal == quo*n:
                    return pal
                n -= 1
                quo = pal // n

            pal = nextPalidromic(pal)
        
        return -1

# tests
tests = [ 
    ( 10, 99 , 9009),
    ( 100, 999, 906609),
]

for min_val, max_val, solution in tests:
    sol = Solution.largestPalindromeProduct(min_val, max_val)
    # print(sol)
    print( sol == solution )
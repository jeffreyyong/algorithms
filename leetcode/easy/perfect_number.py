'''
We define the perfect number is a positive integer that is equal to the sum of all its 
positive divisors except itself.

Noew, given an integer n, write a function that returns true when it is a perfect number
and false when it is not.

Example:
    Input: 28
    Output: True
    Explanation: 28 = 1 + 2 + 4 + 7 + 14
'''

'''
It just checks whether the number has a certain form (k + 1 one-bits followed by k zero-bits). That form
is necessary (at least for the numbers in the allowed range) but not sufficient. It incorrectly returns
True for the following numbers, so those should be added to the test suite.
'''

class Solution:
    '''
    Approach #1 Brute Force

    In brute force approach, we consider every possible number to be a divisor of the given number `num`,
    by iterating over all the numbers lesser than `num`. Then, we add up all the factors to check if the
    given number satisfies the Perfect Number property. This appraoch obviously fails if the number `num`
    is very large.

    Time complexity: O(n). We iterate over all the numbers lesser than n.
    Space complexity: O(1). Constant extra space is used.
    '''

    def check_perfect_number_1(self, num):
        if num <= 0:
            return False

        sum = 0
        for i in range(1,num):
            if num % i == 0:
                sum += i

        return sum == num

    '''
    Apprach #2 Better Brute Force

    Algorithm:
    We can little optimize the brute force by breaking the loop when the value `sum` increase the value of 
    `num`. In that case, we can directly return `false`.

    Time complexity: O(n). In worst case, we iterate over all the numbers lesser than n.
    Space complexity: O(1). Constant extra space is used.
    '''

    def check_perfect_number_2(self, num):
        if num <= 0:
            return False

        sum = 0
        for i in range(1, num):
            if num % i == 0:
                sum += i

            if sum > num:
                return False

        return sum == num

    '''
    Approach #3 Optimal Solution [Accepted]

    In this method, instead of iterating over all the integers to find the factors of `num`, we only iterate upto
    the square root of n. The reasoning behind this can be understood as follows.

    Consider the given number `num` which can have `m` distinct factors, namely n1, n2, ...,nm. Now, since the number
    `num` is divisiby by ni, it is also divisble by nj = num/n1 i.e. ni * nj = `num`. Thus we can get a significant
    reduction in the run-time by iterating only upto the square root of `num`  and considering such ni's and nj's
    in a single pass directly.

    Further if square root of `num` is also a factor, we have to consider the factor only once while checking for 
    the perfect number property.

    We sum up all such factors and check if the given number is a Perfect Number or not. Another point to be observed
    is that while considering 1 as such a factor, `num` will also be considered as the other factor.

    Thus, we need to subtract `num` from the `sum`.
    '''

    def check_perfect_number_3(self, num):
        if num <= 0:
            return False

        sum = 0

        for i in range(1, int(num ** 0.5)):
            if num % i == 0:
                sum += i
                if i * i != num:
                    sum += num / i


        return sum - num == num

    '''
    Approach #4 Euclid Euler Theorem [Accepted]

    Algorithm
    Euclid proved that 2^(p-1) * (2^p - 1) is an even perfect number whenever 2^p - 1 is prime,
    where `p` is prime. For example, the first four perfect numbers are generatted by the formula
    2^(p-1) * (2^p - 1), with `p` a prime number, as follows:

    for p = 2: 2^1(2^2 - 1) = 6
    for p = 3: 2^2(2^3 - 1) = 28
    for p = 5: 2^4(2^5 - 1) = 496
    for p = 7: 2^6(2^7 - 1) = 8128

    Prime numbers of the form 2^p - 1 are known as Mersenne primes. For 2^p -1 to be prime, it is necessary that
    p itself be prime. However not all the numbers of the form 2^p -1 with a prime `p` are prime; for example
    2^11 - 1 = 2047 = 23 * 89 is not a prime number

    You can see that for small value of `p`, its related perfect number goes very high. So, we need to evaluate
    perfect numbers for som eprimes (2,3,5,7,13,17,19,31) only, as for bigger prime its perfect number will not
    fit in 64 bits
    '''


    def check_perfect_number_4(self, num):
        def pn(p):
            return (1 << (p - 1)) * ((1 << p) - 1)
        primes = [2,3,5,7,13,17,19,31]
        for prime in primes:
            if pn(prime) == num:
                return True
             
        return False





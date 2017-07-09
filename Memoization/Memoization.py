class Fibber:

    def __init__(self):
        self.memo = {}

    def fib(self, n):
        if n < 0:
            raise Exception("Index was negative")

        elif n in [0, 1]:
            return n

        if n in self.memo:
            print("grabbing memo[%i]") % n
            return self.memo[n]

        print("computing fib(%i)") %n
        result = self.fib(n - 1) + self.fib(n - 2)

        # memoize
        self.memo[n] = result

        return result

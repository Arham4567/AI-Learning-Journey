# Create an iterator for fibonacci series in such a way that each next returns the next element from fibonacci series.
# The iterator should stop when it reaches a limit defined in the constructor.

class Fibonacci:
    def __init__(self, limit):
        self.limit = limit
        self.previous = 0
        self.previous_previous = 1
        self.n=1

    def __iter__(self):
        return self
    def __next__(self):
        if self.n < self.limit:
            result=self.previous+self.previous_previous
            self.previous=self.previous_previous
            self.previous_previous=result
            self.n+=1
            return result
        else:
            raise StopIteration


f=iter(Fibonacci(10))
while True:
    try:
        print(next(f))
    except StopIteration:
        break
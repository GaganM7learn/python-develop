class Counter :
    def __init__(self):
        self.value = 10

    def increment(self):
        self.value += 1

counter = Counter()

counter.increment()
counter.increment()
counter.increment()

print(counter.value)
class RingBuffer:
    def __init__(self, capacity: int):
        assert capacity > 0
        self.capacity = capacity
        self.data = []
        self.current_index = 0

    def append(self, item):
        if self.capacity != len(self.data):
            self.data.append(item)
        else:
            self.data[self.current_index] = item
        self.current_index = (self.current_index + 1) % self.capacity

    def get(self):
        return self.data[:]

if __name__ == "__main__":
    thing = RingBuffer(2)

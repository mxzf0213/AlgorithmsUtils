class heap(object):
    def __init__(self):
        self.heap_size = 0
        self.h = [0]

    def cmp(self, i, j):
        return i < j

    def build_heap(self, h):
        self.heap_size = len(h)
        for val in h:
            self.h.append(val)
        for i in range(self.heap_size // 2, 0, -1):
            self.down(i)

    def push(self, val):
        self.heap_size = self.heap_size + 1
        self.h.append(val)
        self.up(self.heap_size)

    def pop(self):
        if self.heap_size < 1:
            print("heap underflow")
            return
        self.h[1], self.h[self.heap_size] = self.h[self.heap_size], self.h[1]
        self.heap_size = self.heap_size - 1
        min = self.h.pop()
        self.down(1)
        return min

    def up(self, pos):
        parent = pos // 2
        while pos > 1 and self.cmp(self.h[pos], self.h[parent]):
            self.h[pos], self.h[parent] = self.h[parent], self.h[pos]
            pos = parent
            parent = pos // 2

    def down(self, pos):
        l = 2 * pos
        r = l + 1
        if l <= self.heap_size and self.cmp(self.h[l], self.h[pos]):
            minimum = l
        else:
            minimum = pos
        if r <= self.heap_size and self.cmp(self.h[r], self.h[minimum]):
            minimum = r
        if minimum != pos:
            self.h[pos], self.h[minimum] = self.h[minimum], self.h[pos]
            self.down(minimum)


if __name__ == "__main__":
    heap = heap()
    h = [2, 1, 5]
    heap.build_heap(h)
    heap.push(3)
    while heap.heap_size > 0:
        print(heap.pop())

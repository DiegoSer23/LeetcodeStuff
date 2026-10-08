class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.queue = deque()
        self.window_sum = 0

    def next(self, val: int) -> float:
        self.queue.append(val)
        self.window_sum += val
        
        if len(self.queue) > self.size:
            removed = self.queue.popleft()
            self.window_sum -= removed
            
        return self.window_sum / len(self.queue)

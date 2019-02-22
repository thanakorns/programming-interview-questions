class logSystem:

    def __init__(self, N):
        self.cur_index = 0
        self.itemlist = [None] * N

    def record(self, order_id):
        self.itemlist[self.cur_index] = order_id
        self.cur_index += 1
        if self.cur_index > len(self.itemlist)-1:
            self.cur_index = 0

    def get_last(self, i):
        start_index = self.cur_index - i
        if start_index < 0:
            return self.itemlist[start_index:] + self.itemlist[:self.cur_index]
        else:
            return self.itemlist[start_index:]


ls = logSystem(4)
for id in range(0, 4):
    ls.record(id)
print(ls.get_last(4))

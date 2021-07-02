class Stack:
    """栈"""
    def __init__(self):
        # 用顺序表模拟栈
        self.stack = []

    def is_empty(self):
        return self.stack == []

    def push(self, value):
        """压栈"""
        self.stack.append(value)

    def pop(self):
        """弹栈"""
        return self.stack.pop()

    def peak(self):
        """返回栈顶元素"""
        if self.stack:
            return self.stack[-1]
        else:
            return None

    def size(self):
        return len(self.stack)


class Queue:
    """队列"""
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return self.queue == []

    def enqueue(self, value):
        """进队"""
        self.queue.insert(0, value)

    def dequeue(self):
        """出队"""
        return self.queue.pop()

    def size(self):
        return len(self.queue)


if __name__ == "__main__":
    # 创建对象
    s = Stack()
    s.push('hello')
    s.push('world')
    s.push('python')
    print(f"栈的元素个数:{s.size()}")
    #print(f"第一次出栈:{s.pop()}")
    print(f"第二次出栈:{s.pop()}")

    # 创建队列
    q = Queue()
    q.enqueue('hello')
    q.enqueue('world')
    q.enqueue('python')
    print(q.dequeue())
    print(q.dequeue())
    print(q.size())
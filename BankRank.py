import LinkList
import StaQue

class BankRank:

    def __init__(self):
        self.num = 5
        self.cus = StaQue.Queue()
        self.runwin = StaQue.Queue()
        self.restwin = StaQue.Queue()
    # 顾客代码
    def customer(self):
        print(f"请触屏进行业务办理")
        if self.restwin.size()>0:
           cur = self.restwin.pop()
           self.runwin.enqueue(cur)
           print(f"请到{cur}号窗口办理业务")
        else:
            self.cus.enqueue(self.num)
            print(f"您当前的号码为{self.num},前面有{self.cus.size()-1}人在等待")
            self.num += 1;
    #服务员代码,只有restwin为空才会启用
    def waiter(self):
        if(self.cus.size()>0):
            cur = self.runwin.dequeue()
            print(f"请{self.cus.dequeue()}号到{cur}号窗口办理业务")
            self.runwin.enqueue(cur)
        else:
            self.restwin.enqueue(self.runwin.dequeue())
    #初始化一个例子
    def pre(self):
        self.runwin.enqueue(2)
        self.runwin.enqueue(4)
        self.runwin.enqueue(3)
        self.customer()
        self.customer()
        self.customer()
        self.customer()
        self.waiter()
        self.waiter()
        self.customer()
        self.waiter()
        self.waiter()
if __name__ == "__main__":
    b = BankRank()
    b.pre()
        



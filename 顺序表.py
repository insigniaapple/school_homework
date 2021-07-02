from collections.abc import Iterable


class BasicList:
    """基础顺序表"""
    # ln = l0 + (n-1)*c
    # int类型 c=4
    def __init__(self, max=10):
        """
        初始化方法
        @program max是指最大容量
        """
        # 构造表头
        self.max = max
        # 当前的存储个数
        self.num = 0
        # 数据区
        self.data = [None] * self.max

    def is_empty(self):
        """判断当前顺序表中是否含有元素"""
        return self.num == 0

    def is_full(self):
        """判断当前顺序表中元素是否存满"""
        return self.num == self.max

    def show(self):
        """
        显示所有顺序表中存储的数据
        :return:
        """
        print('<', end='')
        # 遍历
        for i in range(self.num):
            if i != self.num - 1:
                # 如果能来到这里说明i不是最后一个索引
                print(self.data[i], end=',')
            else:
                print(self.data[i], end='>')
        print('')

    def add(self, value):
        """
        从头部添加元素
        将添加的数据加到头部, 然后原有的数据依次后移一个单位,
        self.num += 1
        :return:
        """
        # 如果元素满了就直接返回不允许添加
        if self.is_full():
            print("容量已经满!")
            return

        for i in range(self.num, 0, -1):
            self.data[i] = self.data[i-1]
        # 插入要添加的头部元素
        self.data[0] = value
        # 计算
        self.num += 1

    def append(self, value):
        """
        向尾部追加数据
        :return:
        """
        if self.is_full():
            print("容量已经满!")
            return
        self.data[self.num] = value
        self.num += 1

    def insert(self, index, value):
        """
        在指定位置插入元素
        :param index: 将要插入的位置
        :param value: 将要插入的值
        :return:
        """
        if not isinstance(index, int):
            # 如果index不是int类型.那么就抛类型错误的异常
            raise TypeError
        if index < 0:
            # 头插法
            self.add(value)
        if index > self.num:
            # 尾插
            self.append(value)
        # 中间插入
        for i in range(self.num, index, -1):
            self.data[i] = self.data[i-1]
        self.data[index] = value
        self.num += 1

    def length(self):
        return self.num


if __name__ == '__main__':
    pass
    # 创建对象
    bl = BasicList()
    # <__main__.BasicList object at 0x0000024910231BB0>
    # bl.add(1)

    # 添加元素
    # bl.add(1)  # 1
    # bl.add(2)  # 2 1
    # bl.show()

    # for x in y: y必须是可迭代对象
    # print(isinstance([], Iterable))


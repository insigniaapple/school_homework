

class Node:
    """单链表节点"""
    def __init__(self, value):
        """初始化节点"""
        # 数据区/元素区
        self.value = value
        # 链接域
        self.next = None

    def __str__(self):
        return str(self.value)


class D_Node(Node):
    """供双链表使用"""
    def __init__(self, value):
        super().__init__(value)
        # 前继指针
        self.pre = None

    def __str__(self):
        return super().__str__()


class BaseLinkList:
    """链表的基类"""
    def __init__(self, node=None):
        # 指定p指定指向第一个元素
        self.__head = node

    def is_empty(self):
        """判断链表是否为空"""
        return self.__head is None

    def length(self):
        """获取链表的长度"""
        # 定义初始游标
        cur = self.__head
        # 记数
        count = 0
        while cur is not None:
            count += 1
            # 将游标后移, 指向下一个节点
            cur = cur.next
        return count

    def show(self):
        """遍历链表中的所有节点"""
        # 获取游标
        cur = self.__head
        while cur is not None:
            # 输出当前元素
            print(cur.value, end=' ')
            cur = cur.next
        print("\n")

    def add(self, value):
        node = Node(value)
        node.next = self.__head
        self.__head = node

    def append(self, value):
        cur = self.__head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def insert(self, index, value):
        if index >self.length():
            print("溢出")
            return
        cur = self.__head
        tmp = Node(value)
        for i in range(index-2):
            cur = cur.next
        tpp = cur.next
        cur.next = tmp
        cur.next.next=tpp

    def remove(self, value):
        if self.__head.value == value:
            self.__head = self.__head.next
            return
        cur = self.__head
        while cur.next.value != value:
            cur = cur.next
            if cur == None:
                print("no such a value")
                return
        
        cur.next = cur.next.next

    def find(self, value):
        count = 1
        cur = self.__head
        while cur.vaule is not value:
            cur = cur.next
            count += 1
            if cur == None:
                return 0
        return count

class SingleLinkList(BaseLinkList):
    def add(self, value):
        """
        重写基类的方法:链表头部添加节点
        :param value: 添加的节点
        :return: None
        """
        # 初始化节点
        node = Node(value)
        # 指向插入节点的n区
        node.next = self.__head
        # 变更头指针
        self.__head = node

    def append(self, value):
        """
        重写基类的方法
        在链表的尾部添加节点
        :param value: 添加节点的值
        :return: None
        """
        # 初始化节点
        node = Node(value)
        if self.is_empty():
            #   空链表
            # self.add(value)
            self.__head = node
        else:
            # 遍历,找到最后一个节点
            cur = self.__head
            while cur.next is not None:
                # 控制游标移动
                cur = cur.next
            cur.next = node
            node.next = None

    def insert(self, pos, value):
        """
        指定位置添加元素
        :param index:
        :param value:
        :return:
        """
        if pos <= 0:
            # 头插
            self.add(value)
        elif pos > (self.length() - 1):
            # 尾插
            self.append(value)
        else:
            # 创建节点
            node = Node(value)
            # 游标
            cur = self.__head
            # 统计移动次数
            count = 0
            while cur.next is not None:
                # 获取要插入位置的上一个节点位置
                if pos - 1 == count:
                    # 插入节点的下一个节点
                    node.next = cur.next
                    cur.next = node
                # 控制游标向下移动
                cur = cur.next
                count += 1

    def remove(self, value):
        """
        删除节点
        :param value:
        :return:
        """
        # 游标
        cur = self.__head
        while cur is not None:
            if cur.next.value == value:
                cur.next = cur.next.next
                break
            # 如果没找到,继续向下
            cur = cur.next

    def find(self, value):
        """
        查找链表中是否存在某个节点
        :param value:
        :return:
        """
        cur = self.__head
        index = 0
        while cur is not None:
            if cur.value == value:
                return index
            cur = cur.next
            index += 1

        # 在链表中没有找到元素
        if index == self.length():
            index = -1
        return index


class DoubleLinkList(BaseLinkList):
    """双链表"""
    def add(self, value):
        """
        双链表头插
        :param value:
        :return:
        """
        # 创建节点
        node = D_Node(value)
        if self.is_empty():
            self.__head = node
        else:
            # 获取当前的头部
            cur = self.__head
            # 插入的节点n区指向p区
            node.next = cur
            cur.pre = node
            self.__head = node

    def append(self, value):
        """
        双链表的尾插
        :param value:
        :return:
        """
        node = D_Node(value)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            # 遍历找到最后一个节点
            while cur.next is not None:
                cur = cur.next
            # 尾部添加节点
            cur.next = node
            node.pre = cur

    def insert(self, index, value):
        """
        双链表指定位置添加
        :param index:
        :param value:
        :return:
        """
        if index <= 0:
            # 头插
            self.add(value)
        elif index > (self.length() - 1):
            # 尾插
            self.append(value)
        else:
            # 创建节点
            node = D_Node(value)
            # 游标
            cur = self.__head
            # 统计移动次数
            count = 0
            while cur.next is not None:
                # 到达指定位置
                if index - 1 == count:
                    # 插入节点的下一个节点
                    node.next = cur.next
                    cur.next.pre = node
                    # 处理上一个节点
                    cur.next = node
                    node.pre = cur
                # 没到达指定位置那么就继续移动
                count += 1
                cur = cur.next

    def remove(self, value):
        """
        双链表的删除
        :param value:
        :return:
        """
        if self.is_empty():
            return
        else:
            cur = self.__head
            # 删除的是首节点
            if cur.value == value:
                self.__head = cur.next
                cur.next.pre = None
            else:
                # 删除其他节点
                while cur.next is not None:
                    if cur.value == value:
                        #  假设链表[1, 2, 3]
                        # 删除2  [1, 3]
                        cur.pre.next = cur.next
                        cur.next.pre = cur.pre
                    cur = cur.next
                # 删除尾部节点
                if cur.value == value:
                    cur.pre.next = None

    def find(self, value):
        """
        :param value:
        :return:
        """
        if self.is_empty():
            return -1
        else:
            cur = self.__head
            index = 0
            while cur.next is not None:
                if cur.value == value:
                    return index
                index += 1
                cur = cur.next
        
        # 假设还找不到
        if index == self.length() - 1:
            return -1


if __name__ == '__main__':
    b = BaseLinkList()
    b.add(3)
    b.add(4)
    b.append(5)
    b.insert(2,100)
    print("单链表前插2,4后插5，位置2插100 \n")
    b.show()
    print("链表 rmove 5 \n")
    b.remove(5)
    b.show()





class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    # 定义一个空链表
    def __init__(self):
        self.size=0
        self.head=None
        self.last=None
    #输出定位的链表节点
    def get(self,index):
        if index<0 or index>=self.size:
            raise Exception('超出链表节点范围')
        p=self.head
        for i in range(index):
            p=p.next
        return p
    # 插入链表
    def insert(self,data,index):
        if index <0 or index > self.size:
            raise Exception('超出链表节点范围')
        node=Node(data)
        # 空链表
        if self.size==0:
            self.head=node
            self.last=node
        #     插入头部
        elif index==0:
            node.next=self.head
            self.head=node
        # 插入尾部
        elif self.size==index:
            self.last.next=node
            self.last=node
        # 插入中间
        else:
            prev_node=self.get(index-1)
            node.next=prev_node.next
            prev_node.next=node
        self.size+=1

        # 删除
    def remove(self,index):
        if index<0 or index>=self.size:
            raise Exception('超出链表节点范围')
        # 删除头节点
        if index==0:
            removed_node=self.head
            self.head=self.head.next
        # 删除尾节点
        elif index==self.size-1:
            prev_node=self.get(index-1)
            prev_node.next=None
            self.last=prev_node
        #  删除中间节点
        else:
            # 获取中间节点的前一个节点
            prev_node=self.get(index-1)
            # 获取中间节点的下一个节点
            next_node=prev_node.next.next
            # 删除中间节点
            removed_node=prev_node.next
            # 连接上一节点和下一节点
            prev_node.next=next_node
        self.size-=1
        return removed_node
    #     输出链表
    def output(self):
        p=self.head
        while p is not None:
            print(p.data)
            p=p.next

linkedlist=LinkedList()
# 表头插入数据
linkedlist.insert(3,0)
linkedlist.output()
print('*'*60)
linkedlist.insert(4,0)
# 中间插入
linkedlist.insert(9,2)
linkedlist.insert(5,3)
linkedlist.insert(6,1)
linkedlist.output()
print('*'*60)
# 删除
linkedlist.remove(3)
linkedlist.output()




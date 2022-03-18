class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Queue:
    # 큐의 제일 앞이 없다
    def __init__(self):
        self.front = None

    # 큐가 빈것이라면:
    def is_empty(self):
        return self.front is None

    # 큐에 무엇을 넣는다
    def push(self, value):
        # 만약 비었다면
        if not self.front:
            self.front = Node(value, None) #새로 만든 벨류를 넣어준다
            return

        #만약 안비었다면
        node = self.front #앞에 있는에를 node에 저장
        #다음이 존재하는한, 계속 끝까지 간다
        while node.next:
            node = node.next

        node.next = Node(value, None)

    def pop(self):
        if not self.front:
            return None

        node = self.front #제일 앞에 있는 녀석을 꺼낸다
        self.front = self.front.next
        return node.item


d = Queue()
d.push("hello")
result = d
print(result)
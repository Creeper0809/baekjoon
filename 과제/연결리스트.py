# 연결 리스트를 표현하는 클래스
import random
import time


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    # 요소(Element) 추가
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.length += 1
            return
        last_node = self.head
        while last_node.next is not None:
            last_node = last_node.next
        last_node.next = new_node
        self.length += 1

    # 요소(Element) 삭제
    def delete(self, data):
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            self.length -= 1
            return
        current_node = self.head
        while current_node.next is not None:
            if current_node.next.data == data:
                current_node.next = current_node.next.next
                self.length -= 1
                return
            current_node = current_node.next

    # 리스트 삽입
    def insert(self, index, data):
        new_node = Node(data)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            self.length += 1
            return
        current_node = self.head
        current_index = 0
        while current_node.next is not None:
            if current_index == index - 1:
                new_node.next = current_node.next
                current_node.next = new_node
                self.length += 1
                return
            current_node = current_node.next
            current_index += 1
        if current_index == index - 1:
            current_node.next = new_node


    # 요소(Element) 출력
    def display(self):
        if self.head is None:
            return
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next

    def search(self, data):
        count = 1
        if self.head is None:
            return False
        current_node = self.head
        while current_node is not None:
            if current_node.data == data:
                print("프리패스를 가지고 있던 손님은:",count,"번째에 있습니다")
                return count
            count += 1
            current_node = current_node.next

#사용법
N = 10000
# 1~n까지 중복되지 않는 숫자 뽑기
notDuplicationNum = [i for i in range(1, N+1)]
random.shuffle(notDuplicationNum)

#100가지의 사람 뽑기
freepass = list()
for i in range(10):
    num = random.randrange(1,N+1)
    if num not in freepass:
        freepass.append(num)

for i in range(len(freepass)):
    print(i+1,"번째 프리패스를 가지고 있는 사람은",freepass[i])
print("-"*30)
# 링크드 리스트 데이터 추가
start_time = time.time()
linkedlist = LinkedList()
for i in notDuplicationNum:
    linkedlist.append(i)
end_time = time.time()
print("연결 리스트 데이터 추가까지 걸린 시간: ", end_time - start_time, "초")
print("-"*30)
# 링크드 리스트 데이터 찾기
temp = list()
start_time = time.time()
for i in freepass:
    index = linkedlist.search(i)
    temp.append((index,i))
end_time = time.time()
print("연결 리스트 데이터 찾기까지 걸린 시간: ", end_time - start_time, "초")
print("-"*30)
# 링크드 리스트 데이터 삭제
print("현재 연결 리스트 길이는:",linkedlist.length)
start_time = time.time()
for i in freepass:
    linkedlist.delete(i)
end_time = time.time()
print("연결 리스트 데이터 삭제까지 걸린 시간: ", end_time - start_time, "초")
print("삭제 후 연결 리스트 길이는:",linkedlist.length)
print("-"*30)
# 링크드 리스트 데이터 삽입
start_time = time.time()
for i,num in temp:
    linkedlist.insert(i,num)
end_time = time.time()
print("연결 리스트 삽입에 걸린 시간: ", end_time - start_time, "초")


print("-"*30)


start_time = time.time()
linearList = list()
for i in notDuplicationNum:
    linearList.append(i)
end_time = time.time()
print("선형 리스트 데이터 추가에 걸린 시간: ", end_time - start_time, "초")

print("-"*30)

temp = list()
start_time = time.time()
for i in freepass:
    index = linearList.index(i)
    print("프리패스를 가지고 있던 손님은:", index, "번째에 있습니다")
    temp.append((index,i))
end_time = time.time()
print("선형 리스트 데이터 검색에 걸린 시간: ", end_time - start_time, "초")

print("-"*30)

start_time = time.time()
print("삭제 전 선형 리스트 크기", len(linearList))
for i in freepass:
    linearList.remove(i)
print("선형 리스트 데이터 검색에 걸린 시간: ", end_time - start_time, "초")
print("삭제 후 선형 리스트 크기", len(linearList))
end_time = time.time()

print("-"*30)

start_time = time.time()
for i,num in temp:
    linearList.insert(i,num)
end_time = time.time()
print("선형 리스트 삽입에 걸린 시간: ", end_time - start_time, "초")
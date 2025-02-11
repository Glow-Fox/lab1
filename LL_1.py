class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node

        
    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True
        

    # WRITE FIND_MIDDLE_NODE METHOD HERE #
    def find_middle_node(self):
        if self.head is None:
            return None

        slow = self.head
        fast = self.head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        return slow
    ######################################



def get_linked_list_from_input():
    while True:
        try:
            values = list(map(int, input("Ievadiet skaitļus ar atstarpi: ").split()))
            if not values:
                raise ValueError("Saraksts nedrīkst būt tukšs")
            break
        except ValueError:
            print("Kļūda! Ievadiet tikai veselus skaitļus.")
    
    linked_list = LinkedList(values[0])
    for value in values[1:]:
        linked_list.append(value)
    
    return linked_list


my_linked_list = get_linked_list_from_input()

middle_node = my_linked_list.find_middle_node()
if middle_node:
    print("Vidējais elements:", middle_node.value)

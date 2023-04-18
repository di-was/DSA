class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
   
class LinkedList:
    def __init__(self):
        self.head = None
        
    def add_head(self, val):
        self.head = ListNode(val, self.head)
        
    def add_tail(self, val):
        if not self.head:
            self.head = ListNode(val)
            return 
        current = self.head
        while current.next:
            current = current.next
            
        current.next = ListNode(val)
        
    def get(self, index):
        counter = 0
    
        if (counter == index):
            return self.head
            
        current = self.head
        while current.next:
            counter += 1
            target = current.next
            
            if counter == index:
                return target
        return None
        
    def delete_at_index(self, index):
        counter = 0
        if (counter == index):
            self.head = self.head.next
            return 
        
        current = self.head
        while current.next:
            counter += 1
            target = current.next
            
            if (counter == index):
                target = target.next
                current.next = target
                return 
        return None
    
    def add_item(self, element):
        current = self.head
        if current == None:
            return 0

        if self.head.val >= element:
            new_node = ListNode(self.head.val, self.head.next)
            self.head.val = element
            self.head.next = new_node
            return 0


        while current.next and  current.next.val < element:
            current = current.next

            new_node = ListNode(element, current.next)
            current.next = new_node



    def merge_list(self, target):
        current = target.head
        if (current != None):
            while current.next:
                self.add_item(current.val)
                current = current.next
        self.add_item(current.val)

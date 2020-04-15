# Problem: Given a list of n numbers, determine if it contains any duplicate numbers

def find_dups(arry):
	for i in range(len(arry)):
		for j in range(len(arry)):
			if arry[i] == arry[j] and i is not j:
				return True
	return False


dups_false = [1,2,3,4]
# Returns False
print(find_dups(dups_false))

dups_true = [1,2,3,4,2]
# Returns true
print(find_dups(dups_true))

# Find the middle item in a singly linked list, or two middle items if it contains an even number of nodes.

class Node: 
  
    def __init__(self, data): 
        self.data = data   
        self.next = None   
  
  

class LinkedList: 
  
    def __init__(self): 
        self.head = None



def find_middle_node(head):
	first = head
	second = head
	while second.next is not None:
		first = first.next
		second = second.next.next
	return first.data


a = Node("Mondale")
b = Node("Is")
c = Node("Cool")
a.next = b
b.next = c

print(find_middle_node(a))
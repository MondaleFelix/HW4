# Problem: Given a list of n numbers, determine if it contains any duplicate numbers

def find_dups(arry):
	for i in range(len(aryy)):
		for j in range(len(arry)):
			if arry[i] == arry[j] and i is not j:
				return True

find_dups(nums)



# Find the middle item in a singly linked list, or two middle items if it contains an even number of nodes.

def find_middle_node(head):
	first = head
	second = head
	While second.next is not None:
		First = first.next
		Second = second.next.next
	Return first 

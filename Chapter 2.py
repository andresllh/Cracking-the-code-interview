# Problem  2.3 Delete middle node
"""
I: Delete the middle node.
D: Find a way to advance through the list and find the middle node to remove it. 
E/A: Used Duke's 7 steps. After reading through Chapter 2, the author talked about the runner approach for linked lists.
	 This approach was based on keeping track of two nodes, while iterating only once through the linked list. When running through test cases
	 I noticed that the pointer would always end on the node to be removed, not the one before it, therefore the reference could not be changed.
	 To fix this, I added a pointer called prev, that would keep track of the previous node at all times, so once the loop breaks, the node can be removed. 
L: I utilized the approach discussed in the book, that we had also seen in class for this problem. I utilized a pointer that would move twice as fast as
   the other node, so that when it ended, the loop would have one pointer on the node that needed to be removed. 
"""
def remove_middle_node(head):
	if head is None:
		return head
	second_pointer = head
	prev = None
	while(head.next.next is not None):
		prev = head
		head = head.next
		second_pointer = head.next.next
	head = prev
	head.next = second_pointer
	return 

# Problem  2.1 Remove Dups
"""
I: Remove duplicates from linked list
D: Find a way to remove duplicates from an unsorted linked list
E/A: Used Duke's 7 steps. Simliarly to problem 2.3, the pointer for the previous node had to be kept, so that if a duplicate node was found, it could
	 be removed from the list. Therefore, whenever a duplicate node is found, the head becomes the previous node, and the head.next node, which is the one
	 to be deleted, gets skipped over and head.next.next becomes head.next.  For edge cases I had to take into account an empty list and a case where
	 the list was shorter than 3 nodes. 
L: From this problem I was able to revisit basic linked list operations and freshen up my memory on them. 
"""
def remove_duplicates(head):
	if head is None:
		return 

	if head.next.next is None:
		if head.data is head.next.data:
			head = head.next
		return 

	hash_set = set()
	prev = None

	while (head.next.next is not None):
		if head.data in hash_set:
			head = prev
			head.next = head.next.next
			head = head.next 
		else:
			hash_set.add(head.data)
			prev = head
			head = head.next

	return

# Problem 2.2 Return kth to last element
"""
I: Find the kth to last element in a list.
D: Create a method that will return the kth to last element in a list, given that k is always valid
E/A: Used Duke's 7 steps. Some assumptions were made regarding the value of k, i.e., that k < n where n is the length of the list.
     My approach for this problem was to iterate k amount of times first. By iterating k amount of times on another pointer, once that pointer
     reaches the end of the list, your secondary pointer will be right before the kth element 
L: This problem was conducted in class, so I used the approach that we derived from our group work for this problem.
"""
def kth_to_last_element(head, k):
	if head is None:
		return None
	if head.next is None:
		return None
	i = 0
	second_pointer = head
	while (second_pointer.next is not None):
		if (i < k):
			second_pointer = second_pointer.next
		else:
			second_pointer = second_pointer.next
			head = head.next
		i += 1

	return head.next 

# Problem 2.5 Sum Lists
"""
I: Sum two lists together where each node represents a digit in the whole number.
D: Find a way to sum two lists together where each node represents a digit in the whole number when the order is reversed and when it is not.
E/A: Used Dukes' 7 steps. Assumptions were made when it came to edge cases. If both lists were empty, then -1 would be returned. If only one of the lists
	 were empty, then the other list will be returned. The issue came up, if the lists were not of equal length, so that was included in the solution. The 
	 problem asked to solve the question in two different ways, one where th order was reversed and one wehere it is not. Both solutions are provided. 
L: In this problem I learnt that slicing in Python comes in very handy in these types of problems. By applying the [::-1] slice, I was able to reverse
   the order of the string, then casted it into an integer so it could be added for the final result. 
"""
def sum_lists(list1, list2): # when order is reversed
	s1 = ''
	s2 = ''
	if list1 is None and list2 is None:
		return -1

	if list2 is None:
		while(list1.next is not None):
			s1 += str(list1.data)
			list1 = list1.next
		return int(s1[::-1])

	if list1 is None:
		while(list2.next is not None):
			s2 += str(list2.data)
			list2 = list2.next
		return int(s2[::-1])

	while (list1.next is not None):
		s1 += str(list1.data)
		list1 = list1.next
	while (list2.next is not None):
		s2 += str(list2.data)
		list2 = list2.next

	s1 = int(s1[::-1])
	s2 = int(s2[::-1])
	return s1 + s2

def sum_lists(list1, list2): # when order is correct
	s1 = ''
	s2 = ''
	if list1 is None and list2 is None:
		return -1

	if list2 is None:
		while(list1.next is not None):
			s1 += str(list1.data)
			list1 = list1.next
		return int(s1)

	if list1 is None:
		while(list2.next is not None):
			s2 += str(list2.data)
			list2 = list2.next
		return int(s2)

	while (list1.next is not None):
		s1 += str(list1.data)
		list1 = list1.next
	while (list2.next is not None):
		s2 += str(list2.data)
		list2 = list2.next

	return int(s1) + int(s2)

# Problem 2.8 Loop Detection
"""
I: Detect if there is a loop in the list
D: Create a method that will detect if there is loot in the list and return the node where the loop begins.
E/A: Used Duke's 7 steps. For this problem I began with a less optimized solution. In the less optimized solution, I would store
	 every new node in a hash set, until a collision was found, then return that node. In the more optimized solution, I use a secondary pointer
	 the purpose of the secondary pointer is to iterate at double the pace of the first pointer, so when the first pointer checks every node once and
	 is about to start again in the loop, the second pointer will be starting a loop as well.  
L: In this problem I reused the runner trick that is given in chapter 2 in order to come up with the more optimized solution with regards to space
   complexity. This problem was the same as one of the ones given in class, therefore I had some insight as to how to tackle this problem. 
"""
def loop_detection(head):
	if head or head.next is None:
		return None
	if head.next.next is None:
		if head.next == head.next.next:
			return head.next
		if head == head.next.next or head = head.next:
			return head

	second_pointer = head
	while(second_pointer.next.next is not None):
		if second_pointer == head:
			return head
		else:
			head = head.next
			second_pointer = second_pointer.next.next

	return None

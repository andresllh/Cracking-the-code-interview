# Problem 3.2 Stack Min
"""
I: Create a stack that has Min function that works in O(1) as well as push and pop in O(1)
D: Find a way to create a stack that can perform min, push, and pop in O(1) time complexity
E/A: Used Duke's 7 steps. This problem was discussed during class, so I had a similar approach to the problem.
	 While the syntax might not be correct for creating objects and its functions, the ideas are still there
	 this problem is written in something that resembles pseudo code. My approach for this problem was to create
	 a stack object that will be in the stack. This stack object will store the min value of the stack plus it's own data.
	 By storing the min value in the object, you are able to obtain O(1) time complexity for all 3 functions.
L: For this problem I utilized the structure that was given to us by the Professor. Since a stack can store any object you
   want to store in it. You are able to store any type of data when you push and have that be available in a O(1) response time. 
"""
def stack (stack_object):
	self.stack_object
	self.min_value

	def stack_object(self, data):
		self.data = data
		self.min_value = stack.min_value

	def push(self, stack_object):
		if stack_object.min_value < stack.min_value:
			stack.min_value = stack_object.min_value

	def pop(self):
		return stack.stack_object

	def peek(self):
		return stack_object.data, stack_object.min_value

	def isEmpty(self):
		return stack == None

	def Min(self):
		return stack_object.min_value

# Problem 3.4 Queue via Stacks
"""
I: Implement a queue using two stacks.
D: Find a way to implement a queue using two stacks. 
E/A: Used Duke's 7 steps. This problem was discussed in class. During the class discussion I had come up with a solution that
	 ran in O(n) time complexity, but another solution was shown that had the same time complexity, but only in specific cases. 
	 The idea was to create two stacks, one where everything will be pushed and the second one, where everything will be popped.
	 Since the stacks only have one purpose to them, as long as the dequeue stack is not empty the queue will dequeu in O(1) time 
	 complexity. The case where you don't achieve constant time operations is when the dequeue stack is empty, so everything from
	 the enqueue stack needs to be popped and pushed into the dequeue stack. 
L: From the idea that was given in class I was able to design a queue that uses two stacks to implement it's functionality. Using
   the idea given in class, the time complexity for most operations would be O(1), unless you have an empty dequeue stack, which will
   be O(n) running time, where n is the size of the enqueue stack. 
"""
def queue():
	stack1 = stack()
	stack2 = stack()
	last_stack_one = True

	def enqueue(data):
		stack2.push()

	def dequeue():
		if self.isEmptyQueue:
			throw exception
		if stack1.isEmpty():
			while not(stack2.isEmpty):
				stack1.push(stack2.pop())
		else:
			stack1.pop()
		return

	def peekQueue():
		if self.isEmptyQueue:
			throw exception
		if stack1.isEmpty():
			while not(stack2.isEmpty):
				stack1.push(stack2.pop())
		else:
			return stack1.peek()

	def isEmptyQueue():
		return stack1.isEmpty() and stack2.isEmpty()

# Problem 3.5 Sort Stack
"""
I: Sort a stack with the smallest items on top.
D: Find a way to sort a stack with the smallest items ontop while using no additional data structures, except a temporary stack.
E/A: For this problem, I first get the size of the stack, which also returns the first largest item in the stack. I then created a loop that
	 iterates until the whole stack is ordered. By using the size of the stack, every time I find the next largest item in the stack, I decrease
	 the size variable by 1. The size variable stops the popping of the stack right before the last ordered item was popped and iterates through
	 the remaining elements in the stack until it finds the next largest element and pushing it back into the stack and once again decreasing
	 the size by 1, until the size is 1, which means the smallest item is at the top, then it terminates the loop. 
L: For this problem I learned how to use a temporary stack in combination with some other variables to order the stack from the largest
   to smallest element. 
"""
def sort_stack(stack1):
	def get_size(stack1):
		size = 0
		largest_item = None
		while not(stack1.isEmpty):
			curr = stack1.pop()
			if curr > largest_item or largest_item is None:
				largest_item = curr
			size += 1
		return size, largest_item

	if stack1.isEmpty():
		return

	temp_stack = stack()
	temp_stack.push(largest_item)
	size, largest_item = get_size(stack1)
	index = 0
	while True:
		if size == 1:
			break
		curr = stack1.pop()
		if index < size:
			if curr > largest_item or largest_item is None:
				largest_item = curr
			temp_stack.push(curr)
			index += 1

		stack1.push(largest_item)
		index = 0
		largest_item = None
		size -= 1

# Problem 3.6 Animal Shelter
"""
I: Design a queue where the eldest animal is adopted.
D: Design a queue where the eldest animal is adopted, but they may select their preference of dog or cat, else they get the eldest animal. 
E/A: Used Duke's 7 steps. For this problem I had to freshen up on my queue structure by reading over the sample code that was given to us in the book.
	 After reading up on queues I created a modified queue for the animal shelter that contains two different queues, one for cats and one for dogs.
	 For enqueueing, you just need to check the animal type, which is an attribute from the animal object that I created. If the animal is a dog, it 
	 will be enqueued in the dog queue, else it will be enqueued into the cat queue. For dequeueing, 3 different methods were created, one to dequeue the
	 oldest animal, and 2 more methods to dequeue a dog or cat. 
L: For this problem I had to relearn how to create a queue by utilizing the book as a resource. From the sample code that was given, I was able to implement
   my solution to the problem.
"""
public void animal_shelter() {
	void Animal(String name, String type, int time) {
		this.name = name;
		this.type = type;
	}

	Node first_dog;
	Node last_dog;
	Node first_cat;
	Node last_cat;

	void enqueue(Animal animal) {
		Node temp = new Node(animal);
		if (animal.type.equals('dog')) {
			if (last_dog != null) {
				last_dog.next = temp;
				
			} 
			last_dog = temp;
			if (first_dog == null) {
				first_dog = last_dog;
			}
		} else {
			if (last_cat != null) {
				last_cat.next = temp;
			}
			last_cat = temp;
			if (first_cat == null) {
				first_cat = last_cat;
			}
		}
	}

	void dequeue_cat() {
		if (first_cat == null) {
			throw exception
			return;
		} 
		Node temp = first_cat.data;
		first_cat = first_cat.next;
		if (first_cat == null) {
			last_cat = null;
		}
	}

	void dequeue_dog() {
		if (first_dog == null) {
			throw exception
			return;
		}
		Node temp = first_dog.data;
		first_dog = first_dog.next;
		if (first_dog == null) {
			last_dog = null;
		}
	}

	void dequeue_any() {
		if (first_dog == null && first_cat == null) {
			throw exception
			return;
		}
		if (first_dog == null) {
			dequeue_cat();
		}
		if (first_cat == null) {
			dequeue_dog();
		}
		if (first_cat.data.time > first_dog.data.time) {
			dequeue_cat();
		} else {
			dequeue_dog()
		}
	}

}

# Problem 3.1 Three in One
"""
I: Describe how you could use a single array to implement 3 stacks
D: Find a way to implement 3 stacks using an array without writing code. 
E/A: Did not use all of Duke's 7 steps. For this problem, no code was required to be written. The way that I came up with to 
	 accomplish this task was to keep track of the indeces in the array. This array would have to large enough so that indeces do
	 not overlap at any single operation. The array would be divided into 3 sections for each stack. Each stack will have a pointer
	 to its first and last element. Whenever push is called the new item will be inserted at the [last_index + 1] position in the 
	 array for its specific stack. The last_index will be updated to the new item, which is the one that gets returned when pop is
	 called. When pop is called last_index will be reduced by 1 and the item that was in the last_index position gets returned. For
	 the peek method, the item at last_index will be returned, but the last_index variable will not be updated. For the isEmpty method
	 the first and last index will be compared, and if they are equal, then the stack is in fact empty. There would also be a need to 
	 check if any indexes between stacks overlap, which would mean that they got corrupted, and will no longer functions. 
L: For this problem I learnt how to design my algorithm without writing any code by simply thinking about test cases and thinking
   about how I could implement this. While I did not use Duke's 7 steps, I treated this problem like if it were a conversation between
   two programmers that are discussing a hypothetical situatiion and trying to come up with a solution in this manner. 
"""
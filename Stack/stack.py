#stack algo implementation in python

#create stack
def create_stack():
	stack = []
	return stack

#creating empty stack
def check_empty(stack):
	return len(stack) ==  0

#add item to stack
def push(stack, item):
	stack.append(item)
	print("Pushed item:" +item)

#remove element from stack
def pop(stack):
	if(check_empty(stack)):
		return "Stack is empty"

	return stack.pop()

stack = create_stack()
push(stack, str(1))
push(stack, str(2))
push(stack, str(3))
push(stack, str(4))

print("popped item:" +pop(stack))
print("stack after popping: " + str(stack))

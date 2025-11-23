# %% [markdown]
# ### Object-Oriented Programming (OOP) Exercises
# 

# %%
#Task 1
import math

class circle:
    def __init__(self, radius):
        self.radius = radius
       
    def area(self):
        print( math.pi *self.radius **2)
    def perimeter(self):
        print(2 * math.pi *self.radius)

circle1 = circle(10)
circle1.area()
        

# %% [markdown]
# 

# %%
#Task 2

class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.name} is {self.age} years old"
    def birthday(self):
        self.age += 1
        return f"{self.name} is {self.age} years old"

person1 = person("John", 25)
print(person1)
person1.birthday()

# %%
#Task 3
class calculator:
    def __init__(self):
        self.result = 0
    def add(self, num):
        self.result += num
        return self.result    
    def subtract(self, num):
        self.result -= num
        return self.result
    def multiply(self, num):
        self.result *= num
        return self.result
    def divide(self, num):
        self.result /= num
        return self.result

calc = calculator()
print(calc.add(10))
print(calc.subtract(5))
print(calc.multiply(3))
print(calc.divide(2))

# %%
#Task 4

import math

class shapes:
    def area(self):
        raise NotImplementedError("Subclass must implement this method")
    def perimeter(self):
        raise NotImplementedError("Subclass must implement this method")
##################################################
class circle(shapes):
    def circle(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius ** 2
    def perimeter(self):        
        return 2 * math.pi * self.radius
circle1 = circle(10)
print(circle1.area())
print(circle1.perimeter())

##################################################

class square(shapes):
    def square(self, side):
        self.side =side
    def area(self):
        return self.side **2
    def perimeter(self):
        return 4 * self.side()

square1 = square(10)
print(square1.area())
print(square1.perimeter())


##################################################

class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        """Using Heron's Formula."""
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

triangle = Triangle(3, 4, 5)
print(triangle.perimeter())
print(triangle.area())

# %%
#Task 5

class Node:
    """Represents a single node in the binary search tree."""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    """Binary Search Tree implementation with insert and search."""
    
    def __init__(self):
        self.root = None

    def insert(self, value):
        """Insert a value into the BST."""
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, current, value):
        """Recursive insert helper."""
        if value < current.value:
            if current.left is None:
                current.left = Node(value)
            else:
                self._insert_recursive(current.left, value)

        elif value > current.value:
            if current.right is None:
                current.right = Node(value)
            else:
                self._insert_recursive(current.right, value)

    def search(self, value):
        """Search for a value in the BST."""
        return self._search_recursive(self.root, value)

    def _search_recursive(self, current, value):
        """Recursive search helper."""
        if current is None:
            return False

        if value == current.value:
            return True
        elif value < current.value:
            return self._search_recursive(current.left, value)
        else:
            return self._search_recursive(current.right, value)


# ---------------------------
# Testing the BST
# ---------------------------
bst = BinarySearchTree()
values = [50, 30, 20, 40, 70, 60, 80]

for v in values:
    bst.insert(v)

print(bst.search(60))  # True
print(bst.search(25))  # False


# %%
#Task 6
class Stack:
    def __init__(self):
        # internal list represents the stack
        self.items = []

    def push(self, item):
        """Add an item to the top of the stack."""
        self.items.append(item)
        print(f"Pushed: {item}")

    def pop(self):
        """Remove and return the top element of the stack."""
        if not self.is_empty():
            return self.items.pop()
        else:
            print("Stack is empty! Cannot pop.")
            return None

    def peek(self):
        """View the top element without removing it."""
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        """Check if stack is empty."""
        return len(self.items) == 0


# -----------------------------
# Testing the Stack
# -----------------------------
stack = Stack()

stack.push(10)
stack.push(20)
stack.push(30)

print("Popped:", stack.pop())  # 30
print("Top element:", stack.peek())  # 20
print("Is empty?", stack.is_empty())  # False


# %%
#Task 7 - Linked List Data Structure

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def print_list(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next

# -----------------------------
# Testing the Linked List
# -----------------------------
linked_list = LinkedList()

linked_list.append(10)
linked_list.append(20)
linked_list.append(30)

linked_list.print_list()


# %%
#Task 8 - Shopping Cart Class   

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)

    def view_cart(self):
        print("Items in the cart:")
        for item in self.items:
            print(item)

# -----------------------------
# Testing the Shopping Cart
# -----------------------------
cart = ShoppingCart()

cart.add_item("Laptop")
cart.add_item("Smartphone")
cart.view_cart()  # Output: Items in the cart: Laptop, Smartphone

cart.remove_item("Laptop")
cart.view_cart()  # Output: Items in the cart: Smartphone

# %%
# Task 9 Stack with Display
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
        print(f"Pushed: {item}")

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            print("Stack is empty! Cannot pop.")
            return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        return len(self.items) == 0

    def display(self):
        print("Stack contents:")
        for item in reversed(self.items):
            print(item)

# -----------------------------
# Testing the Stack with Display
# -----------------------------
stack = Stack()

stack.push(10)
stack.push(20)
stack.push(30)

stack.display()  # Output: Stack contents: 30, 20, 10

stack.pop()  # Output: Popped: 30

stack.display()  # Output: Stack contents: 20, 10

# %%
#Task 10. Queue Data Structure

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            print("Queue is empty! Cannot dequeue.")
            return None

    def is_empty(self):
        return len(self.items) == 0

# -----------------------------
# Testing the Queue
# -----------------------------
queue = Queue()

queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

print("Dequeued:", queue.dequeue())  # 10
print("Is empty?", queue.is_empty())  # False



# %%
#Task 11. Bank Class
accounts = {
    'John': 1000,
    'Alice': 500,
    'Bob': 200
}


class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, name, balance):
        self.accounts[name] = balance

    def deposit(self, name, amount):
        if name in self.accounts:
            self.accounts[name] += amount
        else:
            print("Account does not exist.")

    def withdraw(self, name, amount):
        if name in self.accounts and self.accounts[name] >= amount:
            self.accounts[name] -= amount
        else:
            print("Insufficient funds or account does not exist.")

    def display_balance(self, name):
        if name in self.accounts:
            print(f"{name}'s balance: {self.accounts[name]}")
        else:
            print("Account does not exist.")

# -----------------------------
# Testing the Bank
# -----------------------------
bank = Bank()

bank.create_account('John', 1000)
bank.deposit('John', 250)
bank.withdraw('John', 200)
bank.display_balance('John')

# %%




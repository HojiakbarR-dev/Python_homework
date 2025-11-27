# %% [markdown]
# ### Homework 1. ToDo List Application
# 
# 

# %%
# ------------------------------------------
# ToDo List Application (with comments)
# ------------------------------------------

from dataclasses import dataclass
from typing import List, Optional

# --------------------------------------------------
# 1. Task Class — represents a single to-do activity
# --------------------------------------------------
@dataclass
class Task:
    id: int                      # Unique ID for task
    title: str                   # Short title of the task
    description: str = ""        # Optional details
    due_date: Optional[str] = None  # Due date in string format
    completed: bool = False      # Flag: True if finished

    # Method to mark task as done
    def mark_complete(self):
        self.completed = True

    # Nicely formatted string for printing task
    def __str__(self):
        status = "✅ Done" if self.completed else "🕗 Incomplete"
        due = f" (Due: {self.due_date})" if self.due_date else ""
        return f"[{self.id}] {self.title}{due} — {status}\n    {self.description}"


# ------------------------------------------------------
# 2. ToDoList Class — manages all Task objects together
# ------------------------------------------------------
class ToDoList:
    def __init__(self):
        self._tasks: List[Task] = []  # List to store tasks
        self._next_id = 1             # Auto-increment task IDs

    # Add a new task to the list
    def add_task(self, title: str, description: str = "", due_date: Optional[str] = None) -> Task:
        task = Task(id=self._next_id, title=title, description=description, due_date=due_date)
        self._tasks.append(task)
        self._next_id += 1            # Increase ID for next task
        return task

    # Mark a task as complete by ID
    def mark_task_complete(self, task_id: int) -> bool:
        for t in self._tasks:
            if t.id == task_id:
                t.mark_complete()     # Change completed = True
                return True
        return False  # Task ID not found

    # Return all tasks
    def list_all_tasks(self) -> List[Task]:
        return list(self._tasks)       # Return a copy

    # Return only incomplete tasks
    def list_incomplete_tasks(self) -> List[Task]:
        return [t for t in self._tasks if not t.completed]

    # Find a task by ID (optional helper)
    def find_task(self, task_id: int) -> Optional[Task]:
        for t in self._tasks:
            if t.id == task_id:
                return t
        return None


# -----------------------------------------------------
# 3. CLI — Command Line Interface (interactive menu)
# -----------------------------------------------------
def run_cli():
    todo = ToDoList()

    # Small helper function to print menu options
    def print_menu():
        print("\n=== ToDo List Menu ===")
        print("1. Add a new task")
        print("2. Mark a task as complete")
        print("3. List ALL tasks")
        print("4. List INCOMPLETE tasks")
        print("5. Exit program")

    # Loop until user chooses Exit
    while True:
        print_menu()
        choice = input("Enter option (1–5): ").strip()

        # Option 1 — Add a task
        if choice == "1":
            title = input("Task title: ")
            desc = input("Description (optional): ")
            due = input("Due date YYYY-MM-DD (optional): ")
            due = due if due else None

            task = todo.add_task(title, desc, due)
            print("\nTask added successfully:")
            print(task)

        # Option 2 — Mark task complete
        elif choice == "2":
            try:
                task_id = int(input("Enter task ID to mark complete: "))
            except ValueError:
                print("❌ Invalid ID. Must be a number.")
                continue

            if todo.mark_task_complete(task_id):
                print("✔ Task marked as complete!")
            else:
                print("❌ Task ID not found.")

        # Option 3 — List all tasks
        elif choice == "3":
            print("\n=== All Tasks ===")
            for t in todo.list_all_tasks():
                print(t)

        # Option 4 — List incomplete tasks
        elif choice == "4":
            print("\n=== Incomplete Tasks ===")
            for t in todo.list_incomplete_tasks():
                print(t)

        # Option 5 — Exit
        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("❌ Invalid option. Please choose 1–5.")


# -----------------------------------------------------
# 4. Demo — Runs automatically to show how it works
# -----------------------------------------------------
def demo():
    todo = ToDoList()

    print("=== Adding sample tasks ===")
    t1 = todo.add_task("Finish homework", "Math and CS homework", "2025-12-01")
    t2 = todo.add_task("Grocery shopping", "Buy milk, eggs, bread", "2025-11-28")
    t3 = todo.add_task("Call Mom", "Check how she is doing")

    for t in todo.list_all_tasks():
        print(t)

    print("\n=== Marking task 2 as complete ===")
    todo.mark_task_complete(2)

    for t in todo.list_all_tasks():
        print(t)

    print("\n=== Listing incomplete tasks ===")
    for t in todo.list_incomplete_tasks():
        print(t)


# -----------------------------------------------------
# Run demo automatically (you can change to run_cli())
# -----------------------------------------------------
if __name__ == "__main__":
    demo()  # Change to run_cli() to use interactive menu



# %% [markdown]
# ### Homework 2. Simple Blog System

# %%
# ---------------------------------------------------------
# Blog System Application (with full comments for learning)
# ---------------------------------------------------------

from dataclasses import dataclass, field
from typing import List, Optional
import datetime

# ---------------------------------------------------------
# 1. POST CLASS
# Represents a single blog post
# ---------------------------------------------------------
@dataclass
class Post:
    id: int                      # Unique ID for each post
    title: str                   # Post title
    content: str                 # Body/content of the post
    author: str                  # Name of the author
    created_at: datetime.datetime = field(default_factory=datetime.datetime.now)

    # Method to update (edit) a post
    def update(self, title: Optional[str] = None, content: Optional[str] = None):
        if title is not None:
            self.title = title
        if content is not None:
            self.content = content

    # Method to convert post into readable text
    def __str__(self):
        created = self.created_at.strftime("%Y-%m-%d %H:%M:%S")
        return f"[{self.id}] {self.title} by {self.author} ({created})\n    {self.content}"


# ---------------------------------------------------------
# 2. BLOG CLASS
# Stores multiple Post objects and manages them
# ---------------------------------------------------------
class Blog:
    def __init__(self):
        self._posts: List[Post] = []   # List to store posts
        self._next_id = 1              # Auto-increment ID counter

    # Method to add a post
    def add_post(self, title: str, content: str, author: str) -> Post:
        p = Post(id=self._next_id, title=title, content=content, author=author)
        self._posts.append(p)
        self._next_id += 1
        return p

    # Return all posts
    def list_all_posts(self) -> List[Post]:
        return list(self._posts)

    # Return all posts by a specific author
    def posts_by_author(self, author: str) -> List[Post]:
        return [p for p in self._posts if p.author.lower() == author.lower()]

    # Find a post by ID
    def find_post(self, post_id: int) -> Optional[Post]:
        for p in self._posts:
            if p.id == post_id:
                return p
        return None

    # Delete a post
    def delete_post(self, post_id: int) -> bool:
        p = self.find_post(post_id)
        if p:
            self._posts.remove(p)
            return True
        return False

    # Edit an existing post
    def edit_post(self, post_id: int, title: Optional[str] = None, content: Optional[str] = None) -> bool:
        p = self.find_post(post_id)
        if p:
            p.update(title=title, content=content)
            return True
        return False

    # Show latest N posts (default = 5)
    def latest_posts(self, n: int = 5) -> List[Post]:
        return sorted(self._posts, key=lambda x: x.created_at, reverse=True)[:n]


# ---------------------------------------------------------
# 3. CLI (COMMAND-LINE MENU)
# Allows user to interact with the Blog system
# ---------------------------------------------------------
def run_cli():
    blog = Blog()

    # Menu helper function
    def print_menu():
        print("\n=== Blog Menu ===")
        print("1. Add a Post")
        print("2. List All Posts")
        print("3. Show Posts by Author")
        print("4. Edit a Post")
        print("5. Delete a Post")
        print("6. Show Latest Posts")
        print("7. Exit")

    # Main loop
    while True:
        print_menu()
        choice = input("Choose (1-7): ").strip()

        # Add post
        if choice == "1":
            title = input("Title: ")
            content = input("Content: ")
            author = input("Author: ")
            p = blog.add_post(title, content, author)
            print("\nPost added:\n", p)

        # List all posts
        elif choice == "2":
            print("\n=== All Posts ===")
            for p in blog.list_all_posts():
                print(p)

        # Posts by author
        elif choice == "3":
            author = input("Enter author name: ").strip()
            posts = blog.posts_by_author(author)
            if posts:
                print(f"\n=== Posts by {author} ===")
                for p in posts:
                    print(p)
            else:
                print("No posts from this author.")

        # Edit post
        elif choice == "4":
            try:
                pid = int(input("Post ID to edit: "))
            except ValueError:
                print("Invalid ID.")
                continue

            new_title = input("New title (leave empty to keep): ").strip()
            new_content = input("New content (leave empty to keep): ").strip()

            if blog.edit_post(pid, title=new_title or None, content=new_content or None):
                print("Post updated successfully!")
            else:
                print("Post not found.")

        # Delete post
        elif choice == "5":
            try:
                pid = int(input("Post ID to delete: "))
            except ValueError:
                print("Invalid ID.")
                continue

            if blog.delete_post(pid):
                print("Post deleted.")
            else:
                print("Post not found.")

        # Show latest posts
        elif choice == "6":
            try:
                n = int(input("How many latest posts? (default 5): ") or "5")
            except ValueError:
                n = 5

            print(f"\n=== Latest {n} Posts ===")
            for p in blog.latest_posts(n):
                print(p)

        # Exit program
        elif choice == "7":
            print("Goodbye!")
            break

        else:
            print("Invalid choice, try again.")


# ---------------------------------------------------------
# 4. DEMO FUNCTION (Runs automatically for testing)
# ---------------------------------------------------------
def demo():
    blog = Blog()

    print("=== ADDING SAMPLE POSTS ===")
    blog.add_post("Hello World", "My first blog post!", "Alice")
    blog.add_post("Python Tips", "Use dataclasses for cleaner code.", "Bob")
    blog.add_post("Travel", "I visited Rome last year.", "Alice")

    print("\n=== ALL POSTS ===")
    for p in blog.list_all_posts():
        print(p)

    print("\n=== POSTS BY ALICE ===")
    for p in blog.posts_by_author("alice"):
        print(p)

    print("\n=== EDITING POST 2 ===")
    blog.edit_post(2, title="Python Tips (Updated)", content="New tips about Python.")
    print(blog.find_post(2))

    print("\n=== DELETING POST 1 ===")
    blog.delete_post(1)

    print("\n=== LATEST 2 POSTS ===")
    for p in blog.latest_posts(2):
        print(p)


# ---------------------------------------------------------
# Run demo by default (change to run_cli() to use menu)
# ---------------------------------------------------------
if __name__ == "__main__":
    demo()


# %% [markdown]
# ### Homework 3. Simple Banking System

# %%
from dataclasses import dataclass

@dataclass
class Account:
    account_number: int
    holder_name: str
    balance: float = 0.0

    # Deposit money
    def deposit(self, amount: float):
        if amount <= 0:
            return False
        self.balance += amount
        return True

    # Withdraw money (with overdraft handling)
    def withdraw(self, amount: float):
        if amount <= 0:
            return False
        if amount > self.balance:  # overdraft not allowed
            return False
        self.balance -= amount
        return True

    # Display account details
    def details(self):
        return f"Account: {self.account_number}\nHolder: {self.holder_name}\nBalance: ${self.balance:.2f}"
    


class Bank:
    def __init__(self):
        self._accounts = {}
        self._next_acc = 1001  # Auto-increment account numbers

    # Add new account
    def add_account(self, holder_name: str, initial_deposit: float = 0.0):
        acc = Account(self._next_acc, holder_name, initial_deposit)
        self._accounts[self._next_acc] = acc
        self._next_acc += 1
        return acc

    # Find account by number
    def find_account(self, account_number: int):
        return self._accounts.get(account_number)

    # Check balance
    def check_balance(self, account_number: int):
        acc = self.find_account(account_number)
        return acc.balance if acc else None

    # Deposit money
    def deposit(self, account_number: int, amount: float):
        acc = self.find_account(account_number)
        if acc:
            return acc.deposit(amount)
        return False

    # Withdraw money
    def withdraw(self, account_number: int, amount: float):
        acc = self.find_account(account_number)
        if acc:
            return acc.withdraw(amount)
        return False

    # Transfer money between accounts
    def transfer(self, from_acc: int, to_acc: int, amount: float):
        sender = self.find_account(from_acc)
        receiver = self.find_account(to_acc)

        if sender and receiver and sender.balance >= amount and amount > 0:
            sender.withdraw(amount)
            receiver.deposit(amount)
            return True
        return False

    # Get account details
    def account_details(self, account_number: int):
        acc = self.find_account(account_number)
        return acc.details() if acc else None

def run_cli():
    bank = Bank()

    while True:
        print("\n===== BANK MENU =====")
        print("1. Create Account")
        print("2. Check Balance")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Transfer Money")
        print("6. Account Details")
        print("7. Exit")
        choice = input("Choose (1-7): ")

        # Create new account
        if choice == "1":
            name = input("Account holder name: ")
            try:
                initial = float(input("Initial deposit: "))
            except ValueError:
                initial = 0.0

            acc = bank.add_account(name, initial)
            print(f"Account created! Account Number = {acc.account_number}")

        # Check balance
        elif choice == "2":
            acc_no = int(input("Account number: "))
            bal = bank.check_balance(acc_no)
            print(f"Balance: ${bal:.2f}" if bal is not None else "Account not found")

        # Deposit
        elif choice == "3":
            acc_no = int(input("Account number: "))
            amount = float(input("Deposit amount: "))
            if bank.deposit(acc_no, amount):
                print("Deposit successful")
            else:
                print("Deposit failed")

        # Withdraw
        elif choice == "4":
            acc_no = int(input("Account number: "))
            amount = float(input("Withdraw amount: "))
            if bank.withdraw(acc_no, amount):
                print("Withdrawal successful")
            else:
                print("Withdrawal failed (insufficient balance or invalid input)")

        # Transfer money
        elif choice == "5":
            sender = int(input("Sender account number: "))
            receiver = int(input("Receiver account number: "))
            amount = float(input("Amount: "))

            if bank.transfer(sender, receiver, amount):
                print("Transfer successful")
            else:
                print("Transfer failed")

        # Account details
        elif choice == "6":
            acc_no = int(input("Account number: "))
            details = bank.account_details(acc_no)
            print(details if details else "Account not found")

        # Exit program
        elif choice == "7":
            print("Goodbye!")
            break

        else:
            print("Invalid option, try again.")


def demo():
    bank = Bank()

    # Create accounts
    acc1 = bank.add_account("Alice", 500)
    acc2 = bank.add_account("Bob", 300)

    print("\n--- Accounts Created ---")
    print(acc1.details())
    print(acc2.details())

    # Deposit
    bank.deposit(acc1.account_number, 200)

    # Withdraw
    bank.withdraw(acc2.account_number, 100)

    # Transfer
    bank.transfer(acc1.account_number, acc2.account_number, 150)

    print("\n--- After Transactions ---")
    print(acc1.details())
    print(acc2.details())
    
if __name__ == "__main__":
    # demo()      # runs automatic testing
    run_cli()     # runs interactive CLI



# %%




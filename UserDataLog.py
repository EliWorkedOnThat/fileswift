import sqlite3

# Connect to (or create) the database
connection = sqlite3.connect("user_profiles.db")
cursor = connection.cursor()

# Create tables if they don't exist
create_profile_table_command = """
CREATE TABLE IF NOT EXISTS Profile (
    Username TEXT PRIMARY KEY,
    Password TEXT NOT NULL
)
"""
create_tasks_table_command = """
CREATE TABLE IF NOT EXISTS Tasks (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Username TEXT NOT NULL,
    Task TEXT NOT NULL,
    Priority TEXT NOT NULL,
    Label TEXT NOT NULL,
    FOREIGN KEY (Username) REFERENCES Profile (Username) ON DELETE CASCADE
)
"""

# Execute the create table commands
cursor.execute(create_profile_table_command)
cursor.execute(create_tasks_table_command)


# Function to create a new profile
def create_profile(username, password):
    try:
        insert_command = "INSERT INTO Profile (Username, Password) VALUES (?, ?)"
        cursor.execute(insert_command, (username, password))
        connection.commit()
        print(f"Profile for {username} created successfully.")
    except sqlite3.IntegrityError:
        print(f"Username '{username}' already exists. Please choose another.")


# Function to check login credentials
def login(username, password):
    cursor.execute("SELECT * FROM Profile WHERE Username=? AND Password=?", (username, password))
    result = cursor.fetchone()
    if result:
        print("Login successful!")
        return True
    else:
        print("Invalid username or password.")
        return False


# Function to add a task
def add_task(username, task, priority, label):
    insert_command = "INSERT INTO Tasks (Username, Task, Priority, Label) VALUES (?, ?, ?, ?)"
    cursor.execute(insert_command, (username, task, priority, label))
    connection.commit()
    print(f"Task '{task}' added successfully.")


# Function to view tasks for a specific user
def view_tasks(username):
    cursor.execute("SELECT * FROM Tasks WHERE Username=?", (username,))
    tasks = cursor.fetchall()
    if tasks:
        print("Your tasks:")
        for task in tasks:
            print(f"ID: {task[0]}, Task: {task[2]}, Priority: {task[3]}, Label: {task[4]}")
    else:
        print("No tasks found.")


# Example of creating a new profile
create_profile("JohnDoe", "password123")

# Example of logging in
if login("JohnDoe", "password123"):
    # Add some tasks
    add_task("JohnDoe", "Finish homework", "High", "School")
    add_task("JohnDoe", "Go grocery shopping", "Medium", "Errands")

    # View tasks
    view_tasks("JohnDoe")

# Close the connection when done
connection.close()
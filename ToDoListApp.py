import sqlite3
import random
import time

# Connect to SQLite database
connection = sqlite3.connect("user_profiles.db")
cursor = connection.cursor()

# Create table for storing user profiles if it doesn't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS Profile (
    Username TEXT PRIMARY KEY,
    Password TEXT NOT NULL
)
""")
# Create Tasks Related To Username
cursor.execute("""
CREATE TABLE IF NOT EXISTS Tasks (
    TaskID INTEGER PRIMARY KEY AUTOINCREMENT,
    Username TEXT,
    Task TEXT NOT NULL,
    Priority TEXT NOT NULL,
    Label TEXT,
    FOREIGN KEY (Username) REFERENCES Profile(Username)
)
""")
connection.commit()

# Welcome message
print("Hello, welcome to the to-do list app")
print("")
time.sleep(0.3)

# To-Do Lists by Priority
Low_Level_Priority_List = []
Medium_Level_Priority_List = []
High_Level_Priority_List = []

# Dictionary to store task labels
task_labels = {}

#Note List
Note_List = []

#Def Daily Notes
def daily_notes(Note_List):

    print("Would you like to set a note or view note list?")
    time.sleep(0.4)
    choice2 = input("Chose: (1) Set Note (2)View Note List")

    if choice2 == "1":
            print("Daily note can be an affirmation or note to self maybe a random task or a quick task")
            print()
            Note_Daily = input("What would you like your note to be set to:") #Error in line 55 str cant be appended
            Note_List.append(Note_Daily)
            print("Note set Successeful !")
    elif choice2 == "2":
            print(f"This is your current note list for todays session: {Note_List}")


# Identify user and log in
def identify_user():
    logged_in = False
    while not logged_in:
        Username = input("Please provide your username: ")
        cursor.execute("SELECT * FROM Profile WHERE Username=?", (Username,))
        user = cursor.fetchone()

        if user:
            UserPassword = input("Please provide your password: ")
            if user[1] == UserPassword:
                print(f"Login successful! Welcome {Username}")
                logged_in = True
                return Username  # Return the logged-in username
            else:
                print("Incorrect password. Try again.")
        else:
            choice = input("Username not found. Would you like to create a new account (Y/N)? ").capitalize()
            if choice == "Y":
                new_password = input("Please create a password: ")
                cursor.execute("INSERT INTO Profile (Username, Password) VALUES (?, ?)", (Username, new_password))
                connection.commit()
                print(f"Account created successfully! You can now log in with your username: {Username}")
            else:
                print("Please try again.")

# Timer function
def Timer():
    timer_unit = int(input("How many minutes would you like to set the timer? "))
    timer_unit_inseconds = timer_unit * 60
    while timer_unit_inseconds > 0:
        print(f"Seconds left: {timer_unit_inseconds}")
        time.sleep(1)
        timer_unit_inseconds -= 1
    print("Time's up!")

# Search functionality
def search(username):
    user_search = input("What task would you like to look for? ").lower()

    # Query the database for tasks associated with the username
    cursor.execute("SELECT Task, Label FROM Tasks WHERE Username=? AND Task LIKE ?", (username, f'%{user_search}%'))
    found_tasks = cursor.fetchall()

    if found_tasks:
        print("Search Results:")
        for task, label in found_tasks:
            print(f"{label} - {task}")
    else:
        print("Search was not able to find this task!")

# Function to get a random motivational quote
def quotes():
    list_of_quotes = [
        "The only way to do great work is to love what you do.",
        "Success is not final, failure is not fatal: It is the courage to continue that counts.",
        "Your time is limited, so don’t waste it living someone else’s life.",
        "You miss 100% of the shots you don’t take.",
        "It does not matter how slowly you go as long as you do not stop.",
        "The best way to predict your future is to create it.",
        "What lies behind us and what lies before us are tiny matters compared to what lies within us.",
        "The only limit to our realization of tomorrow is our doubts of today."
    ]
    random_quote = random.choice(list_of_quotes)
    return random_quote

# Function to add tasks to the to-do list
def add_to_list(username):
    task = input("What would you like to add to your to-do list? ").lower()
    priority = input("What priority is your task (1)High , (2)Medium , (3)Low? ")
    label = input("Enter a word to describe the task: ")

    priority_dict = {"1": "High", "2": "Medium", "3": "Low"}
    if priority in priority_dict:
        cursor.execute("INSERT INTO Tasks (Username, Task, Priority, Label) VALUES (?, ?, ?, ?)",
                       (username, task, priority_dict[priority], label))
        connection.commit()
        print(f"Task '{task}' added to the {priority_dict[priority]} priority list.")
    else:
        print("Invalid priority choice.")

# Function to view the to-do list based on priority
def view_list(username):
    priority_choice = input("Which list would you like to see based on priority: (1)High, (2)Medium, (3)Low? ")

    priority_dict = {"1": "High", "2": "Medium", "3": "Low"}
    if priority_choice in priority_dict:
        cursor.execute("SELECT Task, Label FROM Tasks WHERE Username=? AND Priority=?",
                       (username, priority_dict[priority_choice]))
        tasks = cursor.fetchall()
        if tasks:
            print(f"{priority_dict[priority_choice]} Priority List:")
            for task, label in tasks:
                print(f"{label} - {task}")
        else:
            print(f"No tasks found in the {priority_dict[priority_choice]} priority list.")
    else:
        print("Invalid input. Please choose 1, 2, or 3.")

# Function to remove a task from the to-do list
def remove_from_list(username):
    priority = input("Which priority list is the task in? (1)High, (2)Medium, (3)Low? ")
    task_to_remove = input("What task would you like to remove? ").lower()

    priority_dict = {"1": "High", "2": "Medium", "3": "Low"}
    if priority in priority_dict:
        cursor.execute("DELETE FROM Tasks WHERE Username=? AND Task=? AND Priority=?",
                       (username, task_to_remove, priority_dict[priority]))
        connection.commit()
        print(f"Task '{task_to_remove}' removed from the {priority_dict[priority]} priority list.")
    else:
        print("Invalid priority choice.")

# Main loop to keep the program running
def work(username):
    is_running = True
    while is_running:
        # Display menu options
        print("\nChoose your next action:")
        print("1. View list")
        print("2. Add item")
        print("3. Remove item")
        print("4. Shut down")
        print("5. Motivational Quote")
        print("6. Search Task")
        print("7. Timer")
        print("8. Daily Notes")

        # Take user input
        try:
            choice = int(input("Enter your choice (1/2/3/4/5/6/7/8): "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        # Handle user's choice using match-case
        match choice:
            case 1:
                view_list(username)
            case 2:
                add_to_list(username)
            case 3:
                remove_from_list(username)
            case 4:
                print("Shutting down...")
                is_running = False
            case 5:
                print(f"Your motivational quote is: {quotes()}")
            case 6:
                search(username)
            case 7:
                Timer()
            case 8:
                daily_notes(Note_List)
            case _:
                print("Not a valid input. Please choose 1, 2, 3, 4, 5, 6, or 7.")

# Run the main loop
username = identify_user()
work(username)

# Close SQLite connection at the end
connection.close()
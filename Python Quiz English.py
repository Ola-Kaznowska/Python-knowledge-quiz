import os
import random

os.system("cls")

questions_answers = [
    ("Who created the Python language?", "Guido van Rossum"),
    ("In which year was Python created?", "1991"),
    ("What is the latest stable version of Python (as of September 2024)?", "Python 3.11"),
    ("What file extension does a Python script have?", ".py"),
    ("Which keyword is used to define a function in Python?", "def"),
    ("How do we write comments in Python?", "#"),
    ("What are the basic data types in Python?", "int, float, str, bool, list, tuple, dict, set"),
    ("What is a variable in Python?", "A memory location that stores data"),
    ("How do you display text on the screen in Python?", "print()"),
    ("What is the default encoding in Python?", "UTF-8"),
    ("How do you create a for loop in Python?", "for i in range():"),
    ("How do you define a while loop in Python?", "while condition:"),
    ("How do you stop a loop in Python?", "break"),
    ("How do you skip to the next iteration in a loop?", "continue"),
    ("How do you define a global variable inside a function?", "global"),
    ("What is the difference between a list and a tuple in Python?", "A list is mutable, while a tuple is not."),
    ("What are the built-in data structures in Python?", "list, tuple, dict, set"),
    ("What is a lambda expression in Python?", "An anonymous function"),
    ("What is the Python interpreter?", "A program that executes Python code"),
    ("What is PEP 8?", "Python's style guide for writing code"),
    ("Which tool do we use to manage Python packages?", "pip"),
    ("What is a module in Python?", "A file containing Python definitions and statements"),
    ("How do you import a module in Python?", "import module_name"),
    ("What does the value None mean in Python?", "No value"),
    ("Which keyword is used to handle exceptions in Python?", "try"),
    ("What does the keyword 'pass' do in Python?", "Does nothing, skips the block of code"),
    ("How do you create a list of numbers from 0 to 9 in Python?", "list(range(10))"),
    ("Can we write Python code in VSC?", "yes"),
    ("Which keyword is used to create a class in Python?", "class"),
    ("What is a class attribute in Python?", "A property of the class that stores data"),
    ("How do you define a class constructor in Python?", "__init__"),
    ("How do you write a conditional statement?", "if"),
    ("What are the conditional statements in Python?", "if, elif, else"),
]

def quiz():
    score = 0
    num_questions = 33
    asked_questions = random.sample(questions_answers, num_questions)
    
    for i, (question, correct_answer) in enumerate(asked_questions, 1):
        print(f"Question {i}: {question}")
        answer = input("Your answer: ")
        
        if answer.lower() == correct_answer.lower():
            print("Correct answer!\n")
            score += 1
        else:
            print(f"Incorrect answer. The correct answer is: {correct_answer}\n")
    
    print(f"Your score: {score}/{num_questions} correct answers.")

quiz()
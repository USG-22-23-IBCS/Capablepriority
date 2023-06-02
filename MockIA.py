from graphics import *
import random

# Define the coding flashcards
coding_flashcards = [
    ("what is a float?", "A decimal in Python"),
    ("what is a integer?", "A whole number or any number that is not a fraction or decimal"),
    ("what is a elif?", "A boolean conditional statement that happens if the conditional expression in the if statement is 0 or a FALSE value."),
    ("what is a for loop?", "A statement that allows code to be executed repeatedly based on a condition, once condition is met it stops."),
    ("what is a list?", "A collection of strings in a particular order"),
    ("what is a function?", "A named block of code that performs a specific task"),
    ("what is a dictionary?", "A collection of key-value pairs"),
    ("what is a string?", "A sequence of characters"),
    ("what is a boolean?", "A data type that can be either True or False"),
    ("what is a variable?", "A named constant used to store a value "),
    ("what is a loop?", "A programming construct that repeats a sequence of instructions until a specific condition is met"),
    ("How do you print 'Hello, World!' in Python?", "print('Hello, World!')"),
    ("How do you access the first element of a list in Python?", "first_element = list[0]"),
    ("What does the super() function do in Python?", "It is used to call a method from the parent class within a subclass."),
    ("What is the correct syntax to define a function in Python?", "def function_name():"),
    ("How do you convert a string to an integer in Python?", "integer_variable = int(string_variable)"),
    ("What is the result of the expression 'Hello' + 'World' in Python?", "'HelloWorld'"),
    ("How do you check if a key exists in a dictionary in Python?", "using the 'dict.get()' function"),
    ("What is the difference between '==' and '=' in Python?", "'==' means equals to and '=' means it is being assinged as equal to"),
    ("What is the word used to exit a loop prematurely in Python?", "break"),
    ("How do you find the length of a string in Python?", "len(string_variable)"),
    ("What is the purpose of the 'return' statement in a function?", "To specify the value to be returned by the function.")]


win = GraphWin("CS Coding Flashcards", 800, 400)
win.setBackground("white")

# Create the flashcard display
flashcard = Rectangle(Point(200, 75), Point(650, 275))
flashcard.setFill("light grey")
flashcard.draw(win)

# Create the text objects for question and answer
question_text = Text(Point(425, 150), "")
question_text.setSize(10)
question_text.setStyle("bold")
question_text.draw(win)

answer_text = Text(Point(425, 150), "")
answer_text.setSize(10)
answer_text.setStyle("bold")
answer_text.draw(win)

prompt_text = Text(Point(425, 260), "*click card for next question*")
prompt_text.setSize(10)
prompt_text.setStyle("bold")
prompt_text.draw(win)

header_text = Text(Point(120, 20), "Computer science flash cards")
header_text.setSize(13)
header_text.setStyle("bold")
header_text.draw(win)


# Create the tally boxes and text objects
correct_box = Rectangle(Point(100, 250), Point(170, 300))
correct_box.setFill("green")
correct_box.draw(win)
correct_text = Text(Point(135, 275), "Correct: 0")
correct_text.setSize(12)
correct_text.draw(win)

incorrect_box = Rectangle(Point(100, 310), Point(170, 360))
incorrect_box.setFill("red")
incorrect_box.draw(win)
incorrect_text = Text(Point(135, 335), "Incorrect: 0")
incorrect_text.setSize(12)
incorrect_text.draw(win)

correct_count = 0
incorrect_count = 0

# Randomly select a flashcard
def flashcard(correct_count, incorrect_count):
    if len(coding_flashcards) == 0:
        return  # Stop if all flashcards have been used

    question, answer = random.choice(coding_flashcards)
    coding_flashcards.remove((question, answer))

    question_text.setText("Question: " + question)
    answer_text.setText("")  
    win.getMouse()
    question_text.setText("")
    answer_text.setText("Answer: " + answer)
    win.getMouse()
    answer_text.setText("")
    question_text.setText("Look at the IDLE shell to answer a question.")



    # Update tally based on user input (correct/incorrect)
    user_input = input("Was your answer correct? (yes/no): ")
    if user_input.lower() == "yes":
        correct_count += 1
        correct_text.setText("Correct: " + str(correct_count))
    else:
        incorrect_count += 1
        incorrect_text.setText("Incorrect: " + str(incorrect_count))

    flashcard(correct_count, incorrect_count)

flashcard(correct_count, incorrect_count)

# Close the window when finished
win.close()

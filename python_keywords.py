import keyword
import tkinter as tk

# Get all the Python keywords
keywords = keyword.kwlist

# Create the Tkinter window
root = tk.Tk()
root.title("Python Keywords")
root.resizable(0, 0)

# Dictionary to map each keyword to its description message
DESCRIPTION_messages = {
'and': 'A logical operator',
'as': 'To create an alias',
'assert': 'For debugging',
'break': 'To break out of a loop',
'class': 'To define a class',
'continue': 'To continue to the next iteration of a loop',
'def': 'To define a function',
'del': 'To delete an object',
'elif': 'Used in conditional statements, same as else if',
'else': 'Used in conditional statements',
'except': 'Used with exceptions, what to do when an exception occurs',
'False': 'Boolean value, result of comparison operations',
'finally': 'Used with exceptions, a block of code that will be executed no matter if there is an exception or not',
'for': 'To create a for loop',
'from': 'To import specific parts of a module',
'global': 'To declare a global variable',
'if': 'To make a conditional statement',
'import': 'To import a module',
'in': 'To check if a value is present in a list, tuple, etc.',
'is': 'To test if two variables are equal',
'lambda': 'To create an anonymous function',
'None': 'Represents a null value',
'nonlocal': 'To declare a non-local variable',
'not': 'A logical operator',
'or': 'A logical operator',
'pass': 'A null statement, a statement that will do nothing',
'raise': 'To raise an exception',
'return': 'To exit a function and return a value',
'True': 'Boolean value, result of comparison operations',
'try': 'To make a try...except statement',
'while': 'To create a while loop',
'with': 'Used to simplify exception handling',
'yield': 'To end a function, returns a generator'
}

# Function to display the description message
def display_description(keyword):
    message_label.config(text=DESCRIPTION_messages.get(keyword, f"No description available for '{keyword}'."))

# Add a button for each keyword
for i, keyword in enumerate(keywords):
    button = tk.Button(root, text=keyword, height=2, width=10, command=lambda k=keyword: display_description(k))
    button.grid(row=i//5, column=i%5, padx=5, pady=5)

# Add a label to display the description message
message_label = tk.Label(root, text="")
message_label.grid(row=len(keywords)//5 + 1, columnspan=5)

# Run the main loop
root.mainloop()

###############################################################################################
# Semester Assignment for:
# Programming Languages and Compilers
# University of Piraeus
# April 2024
###############################################################################################
# A deterministic finite automaton (DFA) is a mathematical model that represents a finite 
# number of states and transitions between these states using a stack to store intermediate 
# results during the execution of a sequence of commands or actions. 
# These automata are used in various fields of computer science, such as syntactic analysis, 
# language processing, search algorithms, and more.
###############################################################################################
# This script receives a predetermined input alphabet "(" & ")" which for personalizing 
# current assignment should take the values "9" & "2" in the variables left_char and right_char
###############################################################################################

import os

# Function to clear the screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to push an item onto the stack
def push(stack, item):
    stack.append(item)

# Function to pop an item from the stack
def pop(stack):
    if not is_empty(stack):
        return stack.pop()
    return None
    
# Function to check if the stack is empty
def is_empty(stack):
    return len(stack) == 0

# Function to peek at the top item of the stack without pop'ing
def peek(stack):
    if not is_empty(stack):
        return stack[-1]

# DFA function to examine the expression
def check_DFA(expression, left_char, right_char, stack):
    move_counter = 1  # Counts the moves that were required from DFA to complete
    stack_level = 0  # This variable is to keep track how far far in the expression current position is
    remaining_expression = expression # To correctly keep track of the position in the input column 
    position = 0  # To correctly keep track of the position in the input column
    
    # Iterate through each character in the expression
    for char in expression:
        if char == left_char:
            push(stack, char)
            stack_level += 1  # Increment stack level when a left character is pushed
            remaining_expression = expression[position:]  # Calculate remaining expression
            print("Move:", move_counter, "|| Pushing '", char, "'", "|| Input: ", remaining_expression, " " * move_counter, "|| Stack level: V", "I" * (len(stack) -1), " "* stack_level ,"|| Current stack:", stack)
            move_counter += 1
        elif char == right_char:
            if not is_empty(stack) and peek(stack) == left_char:
                pop(stack)  # Pop the corresponding left character
                stack_level -= 1  # Decrement stack level if a left character is popped
            remaining_expression = expression[position:]  # Calculate remaining expression
            print("Move:", move_counter, "|| Pop'ing '", left_char, "'", "|| Input: ", remaining_expression, " " * move_counter  ,"|| Stack level: V", "I" * (len(stack) +1), " "* stack_level ,"|| Current stack:", stack)
            move_counter += 1  # Increment move counter for pop action
            if position == len(expression) - 1:
                print("Move:", move_counter, "|| **Finished** ", "|| Input: empty    ", "|| Stack level: V", "I" * (len(stack) -1))
        position += 1  # Increment position
    
    if not is_empty(stack):
        return "NO, Expression is not correct."
    

    print("Completion summary:\n", "Moves made: ", move_counter, "|| Input alphabet: '", left_char, "' and '", right_char, "'")
    return "YES, Expression is ok."


# Main program
# For ease of viewing left and right chars are left as parentheses
# Correct values are: 9 & 2
left_char = '9'
right_char = '2'

# Input expression from user
expression = input("Enter the expression: ")

clear_screen()

print("Initial expression:", expression)

# Call function to check DFA
result = check_DFA(expression, left_char, right_char, [])
print(result)

import re

def insert_multiplication_symbols(expression):
    # Pattern to match variables or numbers followed by variables
    pattern = r'(\d+)([a-zA-Z])|([a-zA-Z])(\d+)'
    # Replace the matched patterns with the appropriate multiplication symbol
    new_expression = re.sub(pattern, r'\1*\2\3', expression)
    return new_expression

# Ask the user for an algebraic expression
user_input = input("Enter an algebraic expression: ")

# Insert multiplication symbols
result = insert_multiplication_symbols(user_input)

# Print the modified expression
print("Modified expression:", result)

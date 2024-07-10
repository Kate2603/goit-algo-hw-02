def are_parentheses_balanced(input_string):
    stack = []
    opening_brackets = "({["
    closing_brackets = ")}]"
    match_bracket = {"(": ")", "{": "}", "[": "]"}
    
    for char in input_string:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack:
                return "Несиметрично"
            top_element = stack.pop()
            if match_bracket[top_element] != char:
                return "Несиметрично"
    
    if stack:
        return "Несиметрично"
    else:
        return "Симетрично"

# Приклади використання:
print(are_parentheses_balanced("( ){[ 1 ]( 1 + 3 )( ){ }}"))  # Виведе: Симетрично
print(are_parentheses_balanced("( 23 ( 2 - 3);"))  # Виведе: Несиметрично
print(are_parentheses_balanced("( 11 }"))  # Виведе: Несиметрично

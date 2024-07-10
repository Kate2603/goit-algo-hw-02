from collections import deque

def is_palindrome(input_string):
    # Ініціалізуємо deque для зберігання символів рядка
    char_deque = deque()

    # Перетворюємо рядок в нижній регістр і видаляємо пробіли
    processed_string = input_string.lower().replace(" ", "")

    # Додаємо символи рядка в deque
    for char in processed_string:
        char_deque.append(char)

    # Порівнюємо символи з обох кінців deque
    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False
    
    # Якщо всі символи збігаються, то рядок є паліндромом
    return True

# Приклад використання:
input_str = "A man a plan a canal Panama"
# palindrome: radar, level, noon, madam, A man a plan a canal Panama
if is_palindrome(input_str):
    print(f"{input_str} є паліндромом")
else:
    print(f"{input_str} не є паліндромом")

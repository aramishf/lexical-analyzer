import sys

def isDelimiter(ch):
    return ch in ' +-*/,;><=()[]{}' 

def isOperator(ch):
    return ch in '+-*/><='

def validIdentifier(s):
    if not s:
        return False
    # If it starts with a digit or is a delimiter, it's invalid
    if s[0].isdigit() or isDelimiter(s[0]):
        return False
    return True

def isKeyword(s):
    # Added common keywords
    keywords = {
        "if", "else", "while", "do", "break", "continue", "int", "double", 
        "float", "return", "char", "case", "sizeof", "long", "short", 
        "typedef", "switch", "unsigned", "void", "static", "struct", "goto",
        "def", "class", "try", "except" # Added Python keywords
    }
    return s in keywords

def isInteger(s):
    if not s:
        return False
    # Check if string is digits (handles negative check separately if needed)
    return s.isdigit()

def isRealNumber(s):
    if not s:
        return False
    try:
        float(s)
        return '.' in s
    except ValueError:
        return False

def parse(input_str):
    left = 0
    right = 0
    length = len(input_str)

    while right <= length and left <= right:
        if right < length and not isDelimiter(input_str[right]):
            right += 1
            continue

        if right < length and left == right:
            if isOperator(input_str[right]):
                print(f"'{input_str[right]}' IS AN OPERATOR")
            elif input_str[right] != ' ': # Ignore space
                 print(f"'{input_str[right]}' IS A SEPARATOR")
            
            right += 1
            left = right
        
        elif left != right:
            sub_str = input_str[left:right]

            if isKeyword(sub_str):
                print(f"'{sub_str}' IS A KEYWORD")
            elif isInteger(sub_str):
                print(f"'{sub_str}' IS AN INTEGER")
            elif isRealNumber(sub_str):
                print(f"'{sub_str}' IS A REAL NUMBER")
            elif validIdentifier(sub_str):
                print(f"'{sub_str}' IS A VALID IDENTIFIER")
            else:
                print(f"'{sub_str}' IS NOT A VALID IDENTIFIER")
            
            left = right

# Driver Code
if __name__ == "__main__":
    str_input = "int a = b + 1c;"
    parse(str_input)

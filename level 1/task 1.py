#level1-T1
#STRINGREVERSAL
#Create a Python function that takes astring as input and returns the reverse of that string. For example, if the input is"hello" the function should return "olleh"
def reverse_string(input_string):
    return input_string[::-1]

if __name__ == "__main__":
    input_str = input("Enter a string: ")
    reversed_str = reverse_string(input_str)
    print("Reversed string:", reversed_str)

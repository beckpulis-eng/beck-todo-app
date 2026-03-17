FILEPATH = "todos.txt"

def get_todos(filepath=r'C:\Users\Pulis\PycharmProjects\PythonProject/todos.txt'): #we define this func for opening/reading the .txt file to make the below program cleaner.

    """"Reads a text file and returns a list of the todos.""" #this is a doc-string which is output from help(get_todos) func.

    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines() #readlines func loads existing todos, list of strings. auto-closes file.
    return todos_local

def write_todos(todos_arg, filepath=r'C:\Users\Pulis\PycharmProjects\PythonProject/todos.txt'): #define this func for opening/writing to the .txt file.

    """Writes the todo items list in the text file.""" #doc-string

    with open(filepath, 'w') as file:
        file.writelines(todos_arg) #writelines func saves the list to the .txt file)

if __name__ == "__main__": #code written within this block is only executed when you write this .py file.
    print("Hello from functions")

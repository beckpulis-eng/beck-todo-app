import streamlit as st
import APP1_todo_functions

todos = APP1_todo_functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    print(todo)
    APP1_todo_functions.write_todos(todos)

#order matters for where you put your text instances!!!!

st.title("Beck's  Todo App")
st.subheader("Organizing the best and worst parts of your day.")
st.write("It is also the only thing Beck knew how to code.")

for index, todo in enumerate(todos): #How we remove todos via checkbox
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        APP1_todo_functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="", placeholder="What will you do today?",
              on_change=add_todo, key='new_todo')

print("Hello")

st.session_state

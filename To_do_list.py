import tkinter as tk

class Task:
    def __init__(self, description, status="incomplete", priority=None):
        self.description = description
        self.status = status
        self.priority = priority

    def __str__(self):
        return f"• {self.description}" if self.status == "completed" else self.description

tasks = []

def add_task():
    task = entry.get()
    tasks.append(Task(task))
    listbox.insert(tk.END, task)
    entry.delete(0, tk.END)

def mark_complete():
    index = listbox.curselection()[0]
    tasks[index].status = "completed"
    listbox.delete(index)
    listbox.insert(index, tasks[index])

def delete_task():
    index = listbox.curselection()[0]
    tasks.pop(index)
    listbox.delete(index)

def close_application():
    # Optionally, save task list to file here
    root.destroy()

root = tk.Tk()
root.title("To-Do List")

# Set contrasting colors
root.configure(bg="#333")  # Dark background
listbox_bg = "#eee"  # Light background for listbox

# Input field for adding tasks
entry = tk.Entry(root, width=50, bg="#fff")  # Light background for entry field
entry.pack()

# Buttons (placed on the right side, pink shade)
button_frame = tk.Frame(root)
button_frame.pack(side=tk.RIGHT)
add_button = tk.Button(button_frame, text="Add Task", command=add_task, bg="pink")
add_button.pack()
mark_button = tk.Button(button_frame, text="Mark Complete", command=mark_complete, bg="pink")
mark_button.pack()
delete_button = tk.Button(button_frame, text="Delete Task", command=delete_task, bg="pink")
delete_button.pack()
close_button = tk.Button(button_frame, text="Close", command=close_application, bg="pink")
close_button.pack()

# Listbox to display tasks
listbox = tk.Listbox(root, width=50, bg=listbox_bg)
listbox.pack()

root.mainloop()

import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Task Manager')
        self.geometry('600x450')
        self.tm = TaskManager(self)
        self.tm.config(background='white')
        self.tm.pack(fill=tk.BOTH, expand=True)

class Task:
    def __init__(self, name='', desc=''):
        self.name = name
        self.desc = desc
        self.completed=False

class TaskManager(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg='white')
        self.task_list=[]
        self.widgets()
    
    def widgets(self):
        #main label
        self.main_label=tk.Label(self, text='Tasks', font=('Helvetica',40), bg='white')
        self.main_label.pack(pady=50)
        
        self.display_tasks()
        
        #buttons
        add_button=tk.Button(self, text='Add Task', command=self.add_task, bg='white')
        add_button.pack(pady=20, side=tk.BOTTOM)
        
        delete_button=tk.Button(self, text='Delete Task', command=self.mark_selected_complete, bg='white')
        delete_button.pack(pady=5, side=tk.BOTTOM)
        
        mark_complete_button = tk.Button(self, text='Mark Selected as Complete', command=self.mark_selected_complete, background='white')
        mark_complete_button.pack(pady=5, side=tk.BOTTOM)
        
        edit_button = tk.Button(self, text='Edit', command=self.edit_selection)
        edit_button.pack(pady=5, side=tk.BOTTOM)
        
    def display_tasks(self):
        #clear existing task labels
        for widget in self.winfo_children():
            if isinstance(widget, tk.Frame) and widget != self.main_label:
                widget.destroy()
        #tasks
        if len(self.task_list)==0:
            task_frame = tk.Frame(self, bg='white')
            task_frame.pack(pady=5, padx=20, fill=tk.X)
            list_label=tk.Label(task_frame, text='No Tasks', font=('Helvetica',18), bg='white')
            list_label.pack(pady=10)
        else:
            for task in self.task_list:
                #set screen
                task_frame2 = tk.Frame(self, bg='white')
                task_frame2.pack(pady=5, padx=20, fill=tk.X)
                var = tk.BooleanVar(value=task.completed)
                var.trace_add("write", lambda *args, task=task, var=var: self.update_completion_status(task, var.get()))
                check=tk.Checkbutton(task_frame2, text=f'{task.name.title()} {task.desc.title()}', variable=var, bg='white')
                check.pack(padx=40, side=tk.LEFT)

    def add_task(self):
        add_task_screen = AddTaskScreen(self)
        
    def update_completion_status(self, task, completed):
        task.completed = completed

    def mark_selected_complete(self):
        tasks_to_remove = []
        for task in self.task_list:
            if task.completed:
                tasks_to_remove.append(task)
        for task in tasks_to_remove:
            self.task_list.remove(task)
        self.display_tasks()
        
    def edit_selection(self):
        selected_list=[]
        for task in self.task_list:
            if task.completed:
                selected_list.append(task)
        edit_screen = EditTaskScreen(self, selected_list[0])

class EditTaskScreen(tk.Toplevel):
    def __init__(self, master,task=''):
        super().__init__(master)
        self.master = master
        self.task = task
        self.config(bg='white')
        self.title('Edit Task')
        self.geometry('600x450')
        self.widgets()

    def widgets(self):
        # main label
        main_label = tk.Label(self, text='Edit Task', font=('Helvetica', 40), bg='white')
        main_label.pack(pady=50)
        # name entry
        name_label = tk.Label(self, text='Name:', font=('Helvetica', 14), bg='white')
        name_label.pack()
        self.name_box = tk.Entry(self, bg='#edf2f5')
        self.name_box.insert(0, self.task.name)
        self.name_box.pack(pady=10)
        # desc entry
        desc_label = tk.Label(self, text='Description:', font=('Helvetica', 14), bg='white')
        desc_label.pack()
        self.desc_box = tk.Entry(self, bg='#edf2f5')
        self.desc_box.insert(0, self.task.desc)
        self.desc_box.pack(pady=10)
        # submit button
        submit = tk.Button(self, text='Update Task', command=self.update_task)
        submit.pack(pady=20, side=tk.BOTTOM)

    def update_task(self):
        name = self.name_box.get()
        desc = self.desc_box.get()
        self.task.name = name
        self.task.desc = desc
        self.master.display_tasks()
        self.destroy()

class AddTaskScreen(tk.Toplevel):
    def __init__(self,master):
        super().__init__(master)
        self.master=master
        self.config(bg='white')
        self.title('Add Task')
        self.geometry('600x450')
        self.widgets()
    
    def widgets(self):
        #main label
        main_label=tk.Label(self, text='Add Task', font=('Helvetica',40), bg='white')
        main_label.pack(pady=50)
        #name entry
        name_label=tk.Label(self, text='Name:', font=('Helvetica',14), bg='white')
        name_label.pack()
        self.name_box=tk.Entry(self, bg='#edf2f5')
        self.name_box.pack(pady=10)
        #desc entry
        desc_label=tk.Label(self, text='Description:', font=('Helvetica',14), bg='white')
        desc_label.pack()
        self.desc_box=tk.Entry(self, bg='#edf2f5')
        self.desc_box.pack(pady=10)
        #submit button
        submit=tk.Button(self, text='Submit Task', command=self.add_task)
        submit.pack(pady=20, side=tk.BOTTOM)
        
    def add_task(self):
        name=self.name_box.get()
        desc=self.desc_box.get()
        task=Task(name,desc)
        self.master.task_list.append(task)
        self.master.display_tasks()
        self.destroy()

if __name__ == '__main__':
    app=App()
    app.mainloop()
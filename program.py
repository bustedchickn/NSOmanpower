import customtkinter as ctk

class variable_task_list():
    def __init__(self,name,col_pointer,starting_row):
        self.name = name
        self.col_pointer = col_pointer
        self.starting_row = starting_row
        self.row_pointer = starting_row
        self.button = None
        self.button2 = None
        self.value = []

    def appended(self,value):
        self.value.append(value)

    def add_tasks(self):
        
        # Generate Events
        self.col_pointer += 1
        if (self.col_pointer > 5):
            self.row_pointer += 1
            self.col_pointer = 2
            shift_down(self.row_pointer)
            
                    
        task_textbox = ctk.CTkTextbox(task_frame, width=325, height=100)
        task_textbox.grid(row=self.row_pointer, column=self.col_pointer, padx=5, pady=5)
        self.appended(task_textbox)
        self.button.grid(row=self.row_pointer, column=self.col_pointer+1, padx=5, pady=5)
        self.button2.grid(row=self.row_pointer, column=self.col_pointer+1, padx=5, pady=5)
                    
        print(f"{self.name} created a textbox in gridspace {self.col_pointer}, {self.row_pointer} with the button in {self.col_pointer+1}")

                    
        
        task_entries[self.starting_row] = self
    
    def remove_tasks(self):
        
        self.value.pop().destroy()
        self.col_pointer -= 1
        if (self.col_pointer<2):
            self.row_pointer -= 1
            self.col_pointer = 5
            shift_up(self.row_pointer)

        print(f"{self.name} says, 'My row pointer is at {self.row_pointer}'")
        print(f"{self.name} says, 'My col pointer is at {self.col_pointer}'")

        
        self.button.grid(row=self.row_pointer, column=self.col_pointer + 1, padx=5, pady=5)
        self.button2.grid(row=self.row_pointer, column=self.col_pointer + 1, padx=5, pady=5)
        
                
        
        task_entries[self.starting_row] = self
                
# Moves each of the task rows down
def shift_down(row):
    print("\n!shifting down")
    for item in range(task_entries[len(task_entries)-1].row_pointer,row-1,-1):
        task_entries[item].row_pointer += 1
        
        newrow=task_entries[item].row_pointer
        input(f"\nThe starting row of {task_entries[item].name} is {newrow}\n")
        for widget in task_frame.winfo_children():
            grid_info = widget.grid_info()
            # print(grid_info)
            if grid_info["row"] == newrow - 1:
                input(f"I should be moving the items on row {newrow - 1} to row {newrow}")
                widget.grid(row=newrow)

# Moves each of the task rows up
def shift_up(row):
    print("\n!shifting up")
    for item in range(task_entries[len(task_entries)-1].row_pointer,row,-1):
        task_entries[item].row_pointer -= 1
        
        newrow=task_entries[item].row_pointer
        print(f"\nThe starting row of {task_entries[item].name} is {newrow}\n")
        for widget in task_frame.winfo_children():
            grid_info = widget.grid_info()
            # print(grid_info)
            if grid_info["row"] == newrow:
                print(f"I should be moving the items on row {newrow} to row {newrow-1}")
                widget.grid(row=newrow)


def update_tasks():
    for widget in task_frame.winfo_children():
        widget.destroy()
    row = 0
    for object in task_entries:
        col = 2

        # spacing for asthetics
        spacer = ctk.CTkLabel(task_frame, text="",width=100)
        spacer.grid(row=row, column=0, padx=10, pady=5)
        event_label = ctk.CTkLabel(task_frame, text=object.name, font=("Helvetica", 12, "bold"))
        event_label.grid(row=row, column=1, padx=10, pady=5)
        for item in object.value:
            task_textbox = ctk.CTkTextbox(task_frame, width=325, height=100)
            task_textbox.grid(row=row, column=col, padx=5, pady=5)
            col += 1
            if col > 5:
                row += 1
                col = 2

        task_button = ctk.CTkButton(task_frame, text="Delete a task", command=object.remove_tasks)
        task_button.grid(row=row, column=col+1, padx=5, pady=5, sticky="s,w")
        
        object.button2 = task_button
        
        task_button = ctk.CTkButton(task_frame, text="Add a task")
        task_button.grid(row=row, column=3, padx=5, pady=5, sticky="n,w", command=object.add_tasks)
        object.button = task_button
        row+=1

# Do the stuff in here about redrawing the whole thing.

# Function to handle the names entered in the second tab
def process_names():
    global names_list
    raw_text = names_textbox.get("1.0", "end").strip()
    names_list = [name.strip() for name in raw_text.splitlines() if name.strip()]  # Clean up names
    label_names_status.configure(text=f"Processed {len(names_list)} names!", text_color="green")
    populate_spreadsheet()  # Update the grid with the names

# Function to populate the spreadsheet
def populate_spreadsheet():
    instruction_tab4.destroy()

    # Clear existing grid
    for widget in spreadsheet_frame.winfo_children():
        widget.destroy()

    # Generate headers (events)
    for col, (event_entry, time_entry) in enumerate(zip(event_entries, time_entries)):
        header_label = ctk.CTkLabel(spreadsheet_frame, text=f"{event_entry.get()}\n{time_entry.get()}", font=("Helvetica", 12, "bold"))
        header_label.grid(row=0, column=col + 1, padx=5, pady=5)

    # Generate rows (names) and cells
    for row, name in enumerate(names_list):
        # Name label on the left side
        name_label = ctk.CTkLabel(spreadsheet_frame, text=name, font=("Helvetica", 12))
        name_label.grid(row=row + 1, column=0, padx=5, pady=5)

        # Editable cells for each event
        for col in range(len(event_entries)):
            cell = ctk.CTkEntry(spreadsheet_frame, placeholder_text=    "", width=100)
            cell.grid(row=row + 1, column=col + 1, padx=5, pady=5)

# Function to create the tasks gui
def intialize_tasks():
    instruction_tab3.destroy()

    # Clear existing grid
    for widget in task_frame.winfo_children():
        widget.destroy()

    # Generate Events
    for row, (event_entry, time_entry) in enumerate(zip(event_entries, time_entries)):
        
        # Create a new list that holds the tasks
        l = variable_task_list(f"{event_entry.get()}\n{time_entry.get()}",2,row)
        print(f"l.name is {l.name}")
        print(f"l.value is {l.name}")
        
        # spacing for asthetics
        spacer = ctk.CTkLabel(task_frame, text="",width=100)
        spacer.grid(row=row, column=0, padx=10, pady=5)

        # Title label
        event_label = ctk.CTkLabel(task_frame, text=f"{event_entry.get()}\n{time_entry.get()}", font=("Helvetica", 12, "bold"))
        event_label.grid(row=row, column=1, padx=10, pady=5)
        task_textbox = ctk.CTkTextbox(task_frame, width=325, height=100)
        task_textbox.grid(row=row, column=2, padx=5, pady=5)
        l.appended(task_textbox)

        # Add the button for removing tasks
        task_button = ctk.CTkButton(task_frame, text="Delete a task")
        task_button.grid(row=row, column=3, padx=5, pady=5, sticky="s,w")

        l.button2 = task_button
        l.button2.configure(command=l.remove_tasks)
        print("Button configured")


        # Add the button for adding tasks
        task_button = ctk.CTkButton(task_frame, text="Add a task")
        task_button.grid(row=row, column=3, padx=5, pady=5, sticky="n,w")

        l.button = task_button
        l.button.configure(command=l.add_tasks)
        print("Button configured")
        
        task_entries.append(l)
        print(f"task_entries is now {task_entries}")











# Function to display event and time entries
def showentries():
    for i, (event_entry, time_entry) in enumerate(zip(event_entries, time_entries)):
        print(f"Event {i + 1}: {event_entry.get()} at {time_entry.get()}")
    intialize_tasks()

# Function to handle initial event creation
def submit():
    user_input = event_num_entry.get()
    try:
        user_input = int(user_input)
    except ValueError:
        event_num_entry.delete(0, "end")
        label_result.configure(text="Please enter a valid number!", text_color="red")
    else:
        label_result.configure(text="", text_color="black")
        create_event_fields(user_input)
        btn_submit.configure(command=eventUpdate)

# Function to dynamically update events
def eventUpdate():
    user_input = event_num_entry.get()
    try:
        user_input = int(user_input)
    except ValueError:
        event_num_entry.delete(0, "end")
        label_result.configure(text="Please enter a valid number!", text_color="red")
    else:
        difference = user_input - len(event_entries)
        if difference > 0:  # Add more entries
            create_event_fields(difference, start_index=len(event_entries))
        elif difference < 0:  # Remove extra entries
            remove_event_fields(abs(difference))

# Function to create event and time entry fields
def create_event_fields(count, start_index=0):
    for i in range(count):
        row_frame = ctk.CTkFrame(entries_frame)
        row_frame.pack(pady=5, fill="x")

        # Create Event Entry
        event_entry = ctk.CTkEntry(row_frame, placeholder_text=f"Event {start_index + i + 1}")
        event_entry.pack(side="left", padx=5, expand=True, fill="x")

        # Create Time Entry
        time_entry = ctk.CTkEntry(row_frame, placeholder_text="Time (ex: 10:00 AM)")
        time_entry.pack(side="left", padx=5, expand=True, fill="x")

        # Track the fields and their frames
        event_entries.append(event_entry)
        time_entries.append(time_entry)
        entry_frames.append(row_frame)

# Function to remove event and time fields
def remove_event_fields(count):
    for _ in range(count):
        last_frame = entry_frames.pop()
        event_entries.pop().destroy()
        time_entries.pop().destroy()
        last_frame.destroy()

# Create the main window
root = ctk.CTk()
root.title("NSO MANPOWER SHEET")
root.geometry("900x600")

# Data structures to track widgets and names
event_entries = []
time_entries = []
task_entries = []
entry_frames = []
names_list = []

# Add Tabview
tabview = ctk.CTkTabview(root, width=850, height=550)
tabview.pack(pady=10, padx=10, fill="both", expand=True)

# Tab 1: Event Management
event_tab = tabview.add("Events")

# Title for Tab 1
title = ctk.CTkLabel(event_tab, text="Build a MANPOWER Sheet", text_color="black", font=("Helvetica", 18, "bold"))
title.pack(padx=50, pady=10)

# Instructions for Tab 1
instruction = ctk.CTkLabel(event_tab, text="Input the number of events.", text_color="black", font=("Helvetica", 14, "italic"))
instruction.pack()

# Input field for number of events
event_num_entry = ctk.CTkEntry(event_tab, placeholder_text="Enter a number (ex: 1)", width=200)
event_num_entry.pack()

spacer = ctk.CTkLabel(event_tab, text="")
spacer.pack(pady=20)

# Submit Button
btn_submit = ctk.CTkButton(event_tab, text="Generate Events", command=submit)
btn_submit.pack(pady=10)

# Label to display results or errors
label_result = ctk.CTkLabel(event_tab, text="")
label_result.pack(pady=10)

# Scrollable Frame for events
scrollable_frame = ctk.CTkScrollableFrame(event_tab, width=850, height=400)
scrollable_frame.pack(pady=10, fill="both", expand=True)

entries_frame = ctk.CTkFrame(scrollable_frame)
entries_frame.pack(pady=10, fill="both", expand=True)

# Show Entries Button
btn_show = ctk.CTkButton(event_tab, text="Show Entries", command=showentries)
btn_show.pack(pady=10)

# Tab 2: Name Input
names_tab = tabview.add("Names")

# Title for Tab 2
names_title = ctk.CTkLabel(names_tab, text="Enter Names", text_color="black", font=("Helvetica", 18, "bold"))
names_title.pack(pady=10)

# Instructions for Tab 2
instruction = ctk.CTkLabel(names_tab, text="Enter each name on a new line", text_color="black", font=("Helvetica", 14, "italic"))
instruction.pack()

# Multiline Textbox for names
names_textbox = ctk.CTkTextbox(names_tab, width=800, height=350)
names_textbox.pack(pady=10)

# Process Names Button
btn_process_names = ctk.CTkButton(names_tab, text="Process Names", command=process_names)
btn_process_names.pack(pady=10)

# Label to show the status of name processing
label_names_status = ctk.CTkLabel(names_tab, text="")
label_names_status.pack(pady=10)

# Tab 3: Task List
task_tab = tabview.add("Tasks")

# Title for Tab 3
task_title = ctk.CTkLabel(task_tab, text="Tasks", text_color="black", font=("Helvetica", 18, "bold"))
task_title.pack(pady=10)

# Instructions for tab 3
instruction_tab3 = ctk.CTkLabel(task_tab, text="Please process events in the previous tab", text_color="black", font=("Helvetica", 14, "italic"))
instruction_tab3.pack()

# Scrollable frame for Tab 3
task_scrollable = ctk.CTkScrollableFrame(task_tab, width=850, height=400)
task_scrollable.pack(pady=10, fill="both", expand=True)
task_frame = ctk.CTkFrame(task_scrollable)
task_frame.pack(pady=10, fill="both", expand=True)


# for i in range(3):
#     task_frame.grid_rowconfigure(i, weight=1)     # Evenly distribute row space
#     task_frame.grid_columnconfigure(i, weight=1)


# Tab 4: Name Display (Spreadsheet)
spreadsheet_tab = tabview.add("Spreadsheet")

# Title for Tab 4
spreadsheet_title = ctk.CTkLabel(spreadsheet_tab, text="Spreadsheet View", text_color="black", font=("Helvetica", 18, "bold"))
spreadsheet_title.pack(pady=10)

# Instructions for Tab 4
instruction_tab4 = ctk.CTkLabel(spreadsheet_tab, text="Please process events, names, and tasks in the previous tabs", text_color="black", font=("Helvetica", 14, "italic"))
instruction_tab4.pack()

# Scrollable Frame for spreadsheet
spreadsheet_scrollable = ctk.CTkScrollableFrame(spreadsheet_tab, width=850, height=400)
spreadsheet_scrollable.pack(pady=10, fill="both", expand=True)

spreadsheet_frame = ctk.CTkFrame(spreadsheet_scrollable)
spreadsheet_frame.pack(pady=10, fill="both", expand=True)

# Run the application
root.mainloop()
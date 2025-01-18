import customtkinter as ctk


def showentries():
    for i, entry in enumerate(entries):
        print(f"Entry {i + 1}: {entry.get()}")


def submit():
    user_input = event_num_entry.get()
    try:
        user_input = int(user_input)
    except:
        event_num_entry.delete(0,"end")
    else:
        user_input = int(user_input)
        for i in range(user_input):
            event_entry = ctk.CTkEntry(root, placeholder_text=f"Entry {i + 1}")
            event_entry.pack( pady=5)
            entries.append(event_entry)
    label_result.configure(text=f"Created {user_input} events!")
    btn_submit.configure(command=showentries)

# Create the main window
root = ctk.CTk()
root.title("NSO MANPOWER SHEET")
root.geometry("900x500")

entries = []

title = ctk.CTkLabel(root, text="Build a MANPOWER Sheet", text_color="black",font=("Helvetica", 18, "bold"))
title.pack(padx=50, pady=10)


# Add an Entry widget
event_num_entry = ctk.CTkEntry(root, placeholder_text="Please insert a number.")
event_num_entry.pack( pady=20)

# Add a Submit button
btn_submit = ctk.CTkButton(root, text="Submit", command=submit)
btn_submit.pack(pady=10)

# Label to display the result
label_result = ctk.CTkLabel(root, text="")
label_result.pack(pady=10)



root.mainloop()

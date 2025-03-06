import customtkinter as ctk
import random
import openpyxl


string = "Number Required: 4"
raw = string.split()

if raw.pop() == "Required:":
    print("no number")
    raw.pop()
else:
    print("there was a number")
    raw.pop()
    raw.pop()

print(raw)






# # Initialize the main window
# root = ctk.CTk()
# root.geometry("500x300")

# # Create a frame to hold both text boxes
# frame = ctk.CTkFrame(root)
# frame.pack(pady=20, padx=20)





# root.mainloop()

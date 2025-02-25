import customtkinter as ctk
import random


x = ["rachel","susanna","sarah","LJ","Talmage"]
print(x[random.randint(0,len(x))])


'''
# Initialize the main window
root = ctk.CTk()
root.geometry("500x300")

# Create a frame to hold both text boxes
frame = ctk.CTkFrame(root)
frame.pack(pady=20, padx=20)

# Create two text boxes
text_box1 = ctk.CTkTextbox(frame, width=200, height=100)
text_box1.pack(side="left", padx=10)

text_box2 = ctk.CTkTextbox(frame, width=200, height=100)
text_box2.pack(side="left", padx=10)

text_box1.insert(0.0,"Hey this is the new text for textbox1!")

root.mainloop()
'''
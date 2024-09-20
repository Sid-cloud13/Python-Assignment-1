import tkinter as tk #GUI

# from a file organizer import organize_files
#  Create the main windows

root = tk.Tk()
root.title("File organizer")
root.geometry("400x250")

label = tk.Label(root, text="Label text content")
Entry.pack(pady=5)

button = tk.button(root, text="submit", command=show_input)
button.pack(pady=5)

root.mainloop()
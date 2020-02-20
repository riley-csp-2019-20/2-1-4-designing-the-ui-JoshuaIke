import tkinter as tk

# main window
root = tk.Tk()
root.wm_geometry("300x200")
root.title("tk")

blue = tk.Canvas(height = 120, width = 200,  background= "blue")
blue.grid(row = 0, column = 0)

red = tk.Canvas(height = 120, width = 200,  background= "red")
red.grid(row = 1, column = 0)

green = tk.Canvas(height = 120, width = 100,  background= "green")
green.grid(row = 0, column = 1)

yellow = tk.Canvas(height = 120, width = 100,  background= "yellow")
yellow.grid(row = 1, column = 1)

root.mainloop()
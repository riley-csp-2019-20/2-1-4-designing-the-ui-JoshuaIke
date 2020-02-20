##############################################################################
#   a113_TR_simple_window1.py
#   Example soulution: Change its size to 200 by 100 pixels.
##############################################################################
import tkinter as tk

# main window
root = tk.Tk()
root.wm_geometry("300x200")
root.title("Autherization")

# create empty frame
frame_login = tk.Frame(root)
frame_login.grid(row=0, column=0, sticky="news")

#Username space
lbl_username = tk.Label(frame_login, text='Username:',font='Courier')
lbl_username.pack(padx = 100)
ent_username = tk.Entry(frame_login, bd=3)
ent_username.pack(pady= 0)

#Password button
lbl_password = tk.Label(frame_login, text='Password:',font='Courier')
lbl_password.pack(pady = 0)
ent_password = tk.Entry(frame_login, bd=3, show = '*')
ent_password.pack(pady= 0)

def test_button():
    print("clicked")
    frame_auth.tkraise()
    password = ent_password.get()
    lbl_display_pass.config( text = password)

#Login Button
bnt_login = tk.Button(frame_login, text='Login', command = test_button)
bnt_login.pack(pady = 30)
bnt_login.pack(padx = 10)

#new frame
frame_auth = tk.Frame(root)
frame_auth.grid(row=0, column=0, sticky="news")

lbl_display_pass = tk.Label(frame_auth, text = "test")
lbl_display_pass.pack()

frame_login.tkraise()

root.mainloop()
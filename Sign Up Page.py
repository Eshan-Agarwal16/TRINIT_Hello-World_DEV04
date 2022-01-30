import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import *
#from test_motion import *
root = tk.Tk()
root.title("Login Page")
# root.iconbitmap(r'icon.ico')
# root.option_add("*tearOff", False) 
root.geometry("1000x600")
root.columnconfigure(index=0, weight=1)
root.columnconfigure(index=1, weight=1)
root.columnconfigure(index=2, weight=1)
root.rowconfigure(index=0, weight=1)
root.rowconfigure(index=1, weight=1)
root.rowconfigure(index=2, weight=1)
root.resizable(False,False)
sizegrip = ttk.Sizegrip(root)
sizegrip.grid(row=100, column=100, padx=(0, 5), pady=(0, 5))
style = ttk.Style(root)
widgets_frame = ttk.Frame(root, padding=(40,0, 0, 10))
widgets_frame.grid(row=0, column=1, padx=0, pady=(50,10), sticky="nsew", rowspan=3)
widgets_frame.columnconfigure(index=0, weight=1)
root.tk.call("source", r"proxttk-dark.tcl")

style.theme_use("proxttk-dark")

d = tk.IntVar(value=2)
# Label
text1 = ttk.Label(widgets_frame, text="CCTV Magnagement",font="colortube 20",foreground="white")
text1.grid(row=0, column=0, pady=50, columnspan=2)# Label
# text2 = ttk.Label(widgets_frame, text="email",font="colortube 12",foreground="white")
# text2.grid(row=2, column=0, pady=50, columnspan=2)# Label
# text3 = ttk.Label(widgets_frame, text="password",font="colortube 12",foreground="white")
# text3.grid(row=8, column=0, pady=50, columnspan=2)





d = tk.IntVar(value=2)

# Entry
box = ttk.Entry(widgets_frame)
box.insert(0, "Email")
box.grid(row=2, column=0, padx=200, pady=0, sticky="ew")



# Entry
box2 = ttk.Entry(widgets_frame)
box2.insert(0, "password")
box2.grid(row=8, column=0, padx=200, pady=50, sticky="ew")

password = ''
def login():
    if box.get == "" or box2.get() == "" :
        messagebox.showerror("Error","All the Fields are required",parent = root)
    else :
        email = box.get()
        # while password != 'helloworld':
        password = box2.get()
        # exec functions
        exec(open("test_motion.py").read())
        #execfile('test_motion.py') 
        # if __name__ == '__main__':
        #    
        #     print('good to go')
        print(email)

accentbutton = ttk.Button(widgets_frame,command = login, text="LOG IN", style="AccentButton")
accentbutton.grid(row=10, column=0, padx=300, pady=10, sticky="nsew")

root.mainloop()
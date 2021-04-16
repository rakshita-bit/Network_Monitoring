from tkinter import *
from pythonping import ping
 
def get_ping():
    result = ping(e.get(), verbose=True)
    res.set(result)
master = Tk()
master.configure(bg='light grey')
res = StringVar()
Label(master, text="Enter URL or IP :",
      bg="light grey").grid(row=0, sticky=W)
Label(master, text="Result :", bg="light grey").grid(row=1, sticky=W)
Label(master, text="", textvariable=res, bg="light grey").grid(
    row=1, column=1, sticky=W)

e = Entry(master)
e.grid(row=0, column=1)
b = Button(master, text="Show", command=get_ping)
b.grid(row=0, column=2, columnspan=2, rowspan=2, padx=5, pady=5)
 
mainloop()

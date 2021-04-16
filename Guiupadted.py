from tkinter import *
from pythonping import ping
import nmap3
import os
 
def get_ip():
    nmap = nmap3.Nmap()
    results = nmap.scan_top_ports("192.168.1.0/24", args="-sn")
    res1.set(results)
    ip = list(results.keys())
    for i in ip:
        print(i)
    
master = Tk()
master.configure(bg='light grey')
res1=StringVar()

Label(master,text="results :",bg="light grey").grid(row=1,sticky=W)
Label(master,text="",textvariable=res1,bg="lightgrey").grid(row=1,column=1,sticky=W)  

c=Entry(master)
c.grid(row=0,column=1)
d=Button(master,text="Showip",command=get_ip)
d.grid(row=0,column=2,columnspan=2,rowspan=2,padx=5,pady=5)
 
mainloop()

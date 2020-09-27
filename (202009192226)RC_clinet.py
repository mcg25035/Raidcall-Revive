import socket
import sys
from tkinter import *
import tkinter.ttk as ttk
class windows():
    def info_window():
        def confirm():
            info.destroy()
        info = Tk()
        info.title('Raidcall網路錯誤')
        info_label = Label(info,text='暫時無法連線至RC伺服端，可能是你沒有連上網路，或是伺服端無法連線，或是版本過舊。')
        info_label.pack()
        info_button = Button(info,text='確定',command=confirm)
        info_button.pack()
        info.update()
        a0000f = str(info.geometry()).split('+')
        a0000f = a0000f[0]
        a0000i = a0000f.split('x')
        a0000ih = a0000i[1]
        a0000iw = a0000i[0]
        a0000g = (mw.winfo_screenheight()/2)+int(a0000ih)
        a0000h = (mw.winfo_screenwidth()/2)-round(int(a0000iw)/2)
        info.geometry(str(a0000f)+'+'+str(round(a0000h))+'+'+str(round(a0000g)))
        info.resizable(width=0, height=0)
        info
def main_window(username):
    mw=Tk()#main_window create
    mw.geometry(str(mw.winfo_screenwidth())+'x'+str(mw.winfo_screenheight()))
    mw.title('Raidcall')
    a = 0
    #Connect to server and login and get Data
    Data = {'Image':'-','Name':'-','StatusBar':'-','FriendList':['-'],'InArea':'-'}
    #From link Data[Image] download image to temp/resourse2
    if Data['Name']=='-':
        windows.info_window()
    def join_area():
        windows.info_window()
    def set_page():
        global a,Data
        if a == 0:
            a=1
        elif a == 1:
            a=2
        elif a == 2:
            a=1
        if a == 1:
            page2.configure(state='normal')
            page1.configure(state='disabled')
            a0000000000.place_forget()
            a0000000000.place(x=0,y=64,relwidth=1)
            Me.place_forget()
            Me_info.place_forget()
            Go.place(x=150,y=33)
            ID_entry.place(x=0,y=33)
        elif a == 2:
            page1.configure(state='normal')
            page2.configure(state='disabled')
            Go.place_forget()
            ID_entry.place_forget()
            a0000000000.place_forget()
            a0000000000.place(x=0,y=136,relwidth=1)
            Me.place(x=0,y=33)
            Me_info.place(x=110,y=33)
    serverHost = '192.168.0.1'
    class LabeledEntry(Entry):
        def __init__(self, master=None, label="Search", **kwargs):
            Entry.__init__(self, master, **kwargs)
            self.label = label
            self.on_exit()
            self.bind('<FocusIn>', self.on_entry)
            self.bind('<FocusOut>', self.on_exit)
    
        def on_entry(self, event=None):
            if self.get() == self.label:
                self.delete(0, END)
    
        def on_exit(self, event=None):
            if not self.get():
                self.insert(0, self.label)
    
    
    photo1=PhotoImage(file="temp/resourse1")
    photo2=PhotoImage(file="temp/resourse2")
    page1=Button(mw,text="發現",command=set_page)
    page2=Button(mw,text="好友",command=set_page)
    page1.place(x=0,y=0)
    page2.place(x=53,y=0)
    a0000000000=ttk.Separator(mw,orient='horizontal')
    a0000000002=ttk.Separator(mw,orient='horizontal')
    a0000000000.place(x=0,y=64,relwidth=1)
    a0000000002.place(x=0,y=32,relwidth=1)
    ID_entry=LabeledEntry(mw,label="輸入群ID或群名稱")
    Go = Button(mw,image=photo1,command=join_area)
    Me = Button(mw,image=photo2)
    Me_info = Label(mw,text=Data['Name'],font=("",33))
    set_page()
    

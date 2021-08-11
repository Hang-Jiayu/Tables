import pymysql
import sys
import tkinter.messagebox

from tkinter import *
import tkinter.tix
root=tkinter.tix.Tk()
sDate=StringVar()
sname=StringVar()
snums=StringVar()


def turn_save(event):                    #自定义回调函数turn_property
    #top.date1.getvar(name=sDate)
    #top.name1.getvar(name=sname)
    #top.nums1.getvar(name=snums)
    #top.price.getvar(name=sprice)
    #top.Explain.getvar(name=sExplain)

    #============================往表插入新记录
    try:
        conn=pymysql.connect(host='localhost', user='root', passwd='test', db='test', port=3306,
                             charset='utf8')
        cur=conn.cursor()
        cur.execute("Insert into test values("+sDate.get()+",'"+sname.get()+"','"+snums.get()+"'); ")
        conn.commit()
        cur.close()
        conn.close()
        tkinter.messagebox.showinfo('Tips:','Save it successfuly!')
    except:
        tkinter.messagebox.showinfo('Tips:','There is something wrong with save it!')
        conn.close()


def turn_property(event):                    #自定义回调函数turn_property
    getSQLDate()
def getSQLDate():
    #============================显示表内容
    try:
        conn=pymysql.connect(host='localhost', user='root', passwd='test', db='test', port=3306,
                              charset='utf8')
        c=tree.get_children()
        for item in c:
            tree.delete(item)
        cur=conn.cursor()
        selectSQL='Select * from test'
        cur.execute(selectSQL)
        for row in cur.fetchall():
            tree.insert("",0,text=' ',values=(row[0],row[1],row[2])) #插入第1行记录
        cur.close()
        conn.close()
    except:
        tkinter.messagebox.showinfo('Tips:','There is something wrong with show it!')
        conn.close()

def deletethings(event):
    try:
        conn=pymysql.connect(host='localhost', user='root', passwd='test', db='test', port=3306,
                             charset='utf8')
        cur=conn.cursor()
        cur.execute("delete from test; ")
        conn.commit()
        cur.close()
        conn.close()
        tkinter.messagebox.showinfo('Tips:','Delete it successfuly!')
    except:
        tkinter.messagebox.showinfo('Tips:','There is something wrong with delete all of it!')
        conn.close()



import tkinter as tk
from tkinter.constants import *
from tkinter import ttk                              #导入ttk模块
from tkinter.constants import *


tree=ttk.Treeview(root)                              #创建树状结构列表实例
tree["columns"]=("name","age","thing")                      #设置二个列对象名
tree.column("name", width=50)                        #设置第一个列宽度
tree.column("age", width=50)                      #设置第二个列宽度
tree.column("thing", width=150)                        #设置第一个列宽度                 #设置第二个列宽度
tree.heading("name",text="Order")                      #给第一个列设置标题
tree.heading("age",text="Time")                      #给第一个列设置标题
tree.heading("thing",text="Things")              #给第二个列设置标题                 #给第二个列设置标题
tree.pack(side="top")
bs=tk.Button(root,text="Show Things",width=10)        #在标签框架上创建Button实例bs
bs.bind("<Button-1>",turn_property)           #bind()绑定鼠标进入事件
bs.pack(side="top")


top=tkinter.tix.Frame(root, relief=RAISED,bd=1)
top.pack(side='left')
top.date1=tkinter.tix.LabelEntry(top,label="Order:",labelside='top',)
top.date1.pack(side="left")
top.date1.entry['textvariable']=sDate
top.name1=tkinter.tix.LabelEntry(top,label="Time:",labelside='top',)
top.name1.pack(side="left")
top.name1.entry['textvariable']=sname
top.nums1=tkinter.tix.LabelEntry(top,label="Things:",labelside='top',)
top.nums1.pack(side="left")
top.nums1.entry['textvariable']=snums
Savebn=tk.Button(top,text="Save",width=30)        #在标签框架上创建Button实例bs
Savebn.bind("<Button-1>",turn_save)           #bind()绑定鼠标进入事件
Savebn.pack(side="left")
Delbn=tk.Button(top,text="Delete All",width=10)
Delbn.bind("<Button-1>",deletethings)
Delbn.pack(side="right")
root.mainloop()



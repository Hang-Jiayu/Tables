import pymysql
import sys
import tkinter.messagebox

from tkinter import *
import tkinter.tix
root=tkinter.tix.Tk()
sDate=StringVar()
sname=StringVar()
snums=StringVar()
swed=StringVar()
sthur=StringVar()
sfri=StringVar()
ssar=StringVar()
ssun=StringVar()
sextra=StringVar()
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
        cur.execute("Insert into weekly values('"+sDate.get()+"','"+sname.get()+"','"+snums.get()+"','"+swed.get()+"','"+sthur.get()+"','"+sfri.get()+"','"+ssar.get()+"','"+ssun.get()+"','"+sextra.get()+"'); ")
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
        selectSQL='Select * from weekly;'
        cur.execute(selectSQL)
        for row in cur.fetchall():
            tree.insert("",0,text=' ',values=(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8])) #插入第1行记录
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
        cur.execute("delete from weekly; ")
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
tree["columns"]=("name","age","thing","mon","thu","fri","sar","sun","extra")                      #设置二个列对象名
tree.column("name", width=50)                        #设置第一个列宽度
tree.column("age", width=100)                      #设置第二个列宽度
tree.column("thing", width=100)
tree.column("mon", width=100)
tree.column("thu", width=100)
tree.column("fri", width=100)
tree.column("sar", width=100)
tree.column("sun", width=100)
tree.column("extra", width=100)
tree.heading("name",text="Time")                      #给第一个列设置标题
tree.heading("age",text="Mon")                      #给第一个列设置标题
tree.heading("thing",text="Tue")
tree.heading("mon",text="Wed")
tree.heading("thu",text="Thu")
tree.heading("fri",text="Fri")
tree.heading("sar",text="Sat")
tree.heading("sun",text="Sun")
tree.heading("extra",text="Extra")
tree.pack(side="top")
bs=tk.Button(root,text="Show Things",width=10)        #在标签框架上创建Button实例bs
bs.bind("<Button-1>",turn_property)           #bind()绑定鼠标进入事件
bs.pack(side="top")


top=tkinter.tix.Frame(root, relief=RAISED,bd=1)
top.pack(side='left')
top.date1=tkinter.tix.LabelEntry(top,label="Time:",labelside='top',)
top.date1.pack(side="left")
top.date1.entry['textvariable']=sDate
top.name1=tkinter.tix.LabelEntry(top,label="Monday:",labelside='top',)
top.name1.pack(side="left")
top.name1.entry['textvariable']=sname
top.nums1=tkinter.tix.LabelEntry(top,label="Tuesday:",labelside='top',)
top.nums1.pack(side="left")
top.nums1.entry['textvariable']=snums
top.nums=tkinter.tix.LabelEntry(top,label="Wednesday:",labelside='top',)
top.nums.pack(side="left")
top.nums.entry['textvariable']=swed
top.nums11=tkinter.tix.LabelEntry(top,label="Thursday:",labelside='top',)
top.nums11.pack(side="left")
top.nums11.entry['textvariable']=sthur
top.nums12=tkinter.tix.LabelEntry(top,label="Friday:",labelside='top',)
top.nums12.pack(side="left")
top.nums12.entry['textvariable']=sfri
top.nums13=tkinter.tix.LabelEntry(top,label="Saturday:",labelside='top',)
top.nums13.pack(side="left")
top.nums13.entry['textvariable']=ssar
top.nums14=tkinter.tix.LabelEntry(top,label="Sunday:",labelside='top',)
top.nums14.pack(side="left")
top.nums14.entry['textvariable']=ssun
top.nums15=tkinter.tix.LabelEntry(top,label="Extra:",labelside='top',)
top.nums15.pack(side="left")
top.nums15.entry['textvariable']=sextra
Savebn=tk.Button(top,text="Save",width=30)        #在标签框架上创建Button实例bs
Savebn.bind("<Button-1>",turn_save)           #bind()绑定鼠标进入事件
Savebn.pack(side="left")
Delbn=tk.Button(top,text="Delete All",width=10)
Delbn.bind("<Button-1>",deletethings)
Delbn.pack(side="right")
root.mainloop()



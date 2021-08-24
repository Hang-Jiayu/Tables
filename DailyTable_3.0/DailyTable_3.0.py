import sys
import tkinter.tix
from tkinter import *
import json
import tkinter.messagebox
import tkinter.ttk
#实例化root
root=tkinter.tix.Tk()
delete=StringVar()
sDate=StringVar()
sname=StringVar()
snums=StringVar()
#窗体设置
root.geometry("700x510")
root.title("Daily")
#大标题
title=Label(root,text="Daily",font=('Arial', 22))
title.pack(side='top')
#-------------------------------
def shoe(event):
    tkinter.messagebox.showinfo("Detailed Information","Apply name：\n       Daily.exe\nEdition:\n       Daily 3.0\nVersion number:\n        20210807\nDeveloper:\n      HangJia-yu\nUpdate log:\n        reduced installation package \nvolume and lighter weight. \n        The saving and reading mech-\nanism is modified to make saving and \nreading faster and more convenient.")



def saveToJSON(dicObject,file):
    flag=False
    if type(dicObject)!=dict:
        return flag
    try:
        j_file=open(".\DailyFile\\"+file,'w')
        json.dump(dicObject,j_file,ensure_ascii=False)
        flag=True
    except:
        print('写数据出错!')
    finally:
        if flag:
            j_file.close()
    return flag
#=========================
def GetFromJSON(filename):
    flag=False
    dicObject={}
    try:
        way=".\DailyFile\\"+filename
        j_file=open(way,'r')
        dicObject=json.load(j_file)
        flag=True
    except:
        print('读JSON数据出错!')
    finally:
        if flag:
            j_file.close()
    return dicObject

#---------------------------
def saveall(event):
    try:
        Time = TE.get('1.0', 'end')
        Get = thft.get('1.0', 'end')
        Save = rema.get('1.0', 'end')
        a=GetFromJSON("Time.json")
        b = GetFromJSON("Things.json")
        c=GetFromJSON("Eles.json")
        if a["0"]=="NothingHere...":
            a["0"]=Time
            b["0"]=Get
            c["0"]=Save
            print("Change")
        else:
            a.setdefault(str(len(a)),Time)
            b.setdefault(str(len(b)),Get)
            c.setdefault(str(len(c)),Save)
            print("Change2")
            print(a,b,c)
        saveToJSON(a,"Time.json")
        saveToJSON(b,"Things.json")
        saveToJSON(c,"Eles.json")
        print("Save")
        x = table.get_children()
        for item in x:
            table.delete(item)
        print("Get2")
        a = GetFromJSON("Time.json")
        b = GetFromJSON("Things.json")
        c = GetFromJSON("Eles.json")
        for i in range(len(a)):
            d = str(i + 1)
            j = str(i)
            table.insert("", i, text='', values=(d, a[j], b[j], c[j]))
        table.update()
        print("update")
        TE.delete('1.0', END)
        thft.delete('1.0', END)
        rema.delete('1.0', END)
    except:
        tkinter.messagebox.showinfo("Tips:","There is something wrong with save it!")

def deles(event):
    if delete==None:
        return None

    if delete.get()=="*":
        d={"0":"NothingHere..."}
        saveToJSON(d,"Time.json")
        saveToJSON(d,"Things.json")
        saveToJSON(d,"Eles.json")
        x = table.get_children()
        for item in x:
            table.delete(item)
        a = GetFromJSON("Time.json")
        b = GetFromJSON("Things.json")
        c = GetFromJSON("Eles.json")
        for i in range(len(a)):
            d = str(i + 1)
            j = str(i)
            table.insert("", i, text='', values=(d, a[j], b[j], c[j]))
        table.update()
        delete.set('')
    a = GetFromJSON("Time.json")
    b = GetFromJSON("Things.json")
    c = GetFromJSON("Eles.json")
    try:
        d=int(delete.get())-1
        for i in range(len(a)):
            e=str(i)
            f=str(i+1)
            g=str(len(a)-1)
            print(i,e,f)
            if i==d:
                if i==len(a)-1:
                    a.pop(e)
                    b.pop(e)
                    c.pop(e)
                    break
                else :
                    print(a[e], a[f])
                    a[e] = a[f]
                    print(b[e],b[f])
                    b[e] = b[f]
                    print(c[e],c[f])
                    c[e] = c[f]
            if i == len(a) - 1:
                a.pop(e)
                b.pop(e)
                c.pop(e)
        if len(a) == 0:
            a = b = c = {"0":"NothingHere..."}
        saveToJSON(a, "Time.json")
        saveToJSON(b, "Things.json")
        saveToJSON(c, "Eles.json")

        a = GetFromJSON("Time.json")
        b = GetFromJSON("Things.json")
        c = GetFromJSON("Eles.json")
        x = table.get_children()
        for item in x:
            table.delete(item)
        for i in range(len(a)):
            d = str(i + 1)
            j = str(i)
            table.insert("", i, text='', values=(d, a[j], b[j], c[j]))
        table.update()
        delete.set('')
    except:
        print("Delete wrong")
#事件框架
frame=tkinter.Frame(root,height=300,width=5,relief=FLAT,bd=1)
frame.pack(side='bottom')

frame1=tkinter.Frame(frame,height=30,width=5,relief=GROOVE,bd=1)
frame1.pack(side='left')
#事件

T=tkinter.Label(frame1,text="Time")
T.pack(anchor='nw')
TE=tkinter.Text(frame1,width=30,height=2)
TE.pack(anchor='nw')

thf=tkinter.Label(frame1,text="Thing",font=('Arial', 10))
thf.pack(anchor='nw')
thft=tkinter.Text(frame1,width=30,height=3)
thft.pack(anchor='nw')

rem=tkinter.Label(frame1,text='Remark')
rem.pack(anchor='nw')
rema=tkinter.Text(frame1,width=30,height=3)
rema.pack(anchor='nw')
#标签
more=tkinter.Button(frame,text="Detailed Information")
more.pack(side='bottom')
more.bind("<Button-1>",shoe)
dele=tkinter.tix.LabelEntry(frame,label='ID to delete',labelside="top")
dele.pack(side='bottom')
dele.entry['textvariable']=delete
delet=tkinter.Button(frame,text="   Delete   ")
delet.pack(side='bottom')
delet.bind("<Button-1>",deles)
save=tkinter.Button(frame,text='    Save    ')
save.pack(side='bottom')
save.bind("<Button-1>",saveall)
#显示框架
sframe=tkinter.Frame(root,height=30,width=500,relief=RIDGE,bd=1)
sframe.pack(side="top")

#显示表格
table=tkinter.ttk.Treeview(sframe,columns=["ID","Time","Things","Remarks"],show='headings',height=300)
table["columns"]=("ID","Time","Things","Remarks")
table.column("ID",width=40)
table.column("Time",width=120)
table.column("Things",width=230)
table.column("Remarks",width=150)
table.heading("ID",text="ID")
table.heading("Time",text="Time")
table.heading("Things",text="Things")
table.heading("Remarks",text="Remarks")

table.pack(side='left')
s=tkinter.ttk.Scrollbar(sframe)
s.pack(side='right',fill=Y)
s.config(command=table.yview)
table.config(yscrollcommand=s.set)

a = GetFromJSON("Time.json")
b = GetFromJSON("Things.json")
c = GetFromJSON("Eles.json")
print(a,b,c)
try:
    for i in range(len(a)):
        d=str(i+1)
        j=str(i)
        table.insert("",i, text='', values=(d, a[j], b[j], c[j]))
        table.update()
    root.mainloop()
except:
    root.mainloop()


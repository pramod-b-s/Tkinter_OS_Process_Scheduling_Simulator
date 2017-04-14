from tkinter import *

q=[]
size=0
f=-1
r=-1
procount = 0
donearray = []
flag = 0
at = []
bt = []
ct = [int]
tat = [int]
wt = [int]
ts = []
k = 0
time = 0
localsize = 0
number = [int]


def nq(x):
    global r
    r=r+1
    global size
    size=size+1
    q[r]=x

def dq():
    global f
    f=f+1
    global size
    size = size-1
    return q[f]

def done(procount,donearray1):
    for i in (0,procount):
        if donearray1[i]==0 :
            return 0

    return 1

def set_flag():
    flag=1


def create_window(procount):
    new_window=Toplevel()

    one = Label(new_window, text="FCFS"+procount, bg="white", fg="black")
    one.pack()

    for i in (0, procount):
        donearray[i] = 0

    while (done(procount,donearray) == 0):
        while (k < procount):
            if (at[k] <= time):
                nq(number[k])
                k = k + 1
            else:
                break

        if size != 0:
            x = dq()
            time += bt[x]
            ct[x] = time
            done[x] = 1
        else:
            time = time + 1

    for i in (0, procount):
        print(ct[i])


def get_procount():
    global procount
    procount = entry_process.get()
    print(procount)

    at_box=[]
    bt_box=[]
    global ts
    global donearray
    global at
    global bt

    for i in (0, procount):
        label_processnum = Label(root, text="process ")
        label_processnum.pack()
        entry_at = Entry(root)
        at_box[i]=entry_at
        entry_at.pack()
        entry_bt = Entry(root)
        bt_box[i]=entry_bt
        entry_bt.pack()
        ts[i] = 0
        donearray[i] = 0

    for i in (0,procount):
        at[i]=at_box[i].__getitem__()
        bt[i]=bt_box
    create_window(procount)


root=Tk()

topframe=Frame(root)
topframe.pack()

bottomframe=Frame(root)
bottomframe.pack(side=BOTTOM)

btn1=Button(topframe,text="FCFS",command=create_window)
btn2=Button(topframe,text="SJF",fg="green")
btn3=Button(topframe,text="RR",fg="blue")

btn4=Button(bottomframe,text="button 4",fg="purple")

btn1.pack(side=LEFT)
btn2.pack()
btn3.pack()
btn4.pack()

label_process=Label(root,text="Number of processes")
label_process.pack()
entry_process=Entry(root)
entry_process.pack()
#global procount

btncreate = Button(root, text="Create processes", command=get_procount)
btncreate.pack()


root.mainloop()
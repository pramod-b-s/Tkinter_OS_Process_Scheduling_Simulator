from tkinter import *
from queue import *

root=Tk()

procount=0
at=[]
bt=[]
at_entry=[int]
bt_entry=[int]
entry_at=Entry()
entry_bt=Entry()
q=[]
f=-1
r=-1
size=0

def add_pro():
    global procount
    global at
    global bt
    global at_entry
    global bt_entry
    global entry_at
    global entry_bt

    label_pro=Label(root,text="process "+str(procount)).grid(row=procount+1)

    entry_at=Entry(root)
    entry_at.grid(row=procount+1,column=1)
    #at_entry[procount]=entry_at
    entry_bt = Entry(root)
    entry_bt.grid(row=procount + 1, column=2)
    #bt_entry[procount]=entry_bt
    procount=procount+1

def save_pro():
    global at
    global bt
    global at_entry
    global bt_entry
    global entry_at
    global entry_bt

    #print(entry_at.get())
    #print(entry_bt.get())
    at.append(entry_at.get())
    bt.append(entry_bt.get())
    #print(at[procount-1])
    #print(bt[procount-1])

def print_pro():
    global at
    global bt
    global procount

    print("procount ")
    print(procount)

    print("at")
    for i in range(len(at)):
        print(at[i])

    print("bt")
    for i in range(len(bt)):
        print(bt[i])

def done(donearray,procount):
    for i in range(len(donearray)):
        if donearray[i]==0:
            return 0
    return 1


def fcfs_display():
    global at
    global bt
    global procount
    size=0
    donearray=[0]*procount
    number=[]
    ts=[]
    ct=[0]*procount
    tat=[0]*procount
    wt=[0]*procount
    start=[0]*procount
    end=[0]*procount

    q=Queue(maxsize=100)

    time = 0
    localsize = 0
    avgwt = 0
    avgtat = 0
    k=0

    for i in range(len(at)):
        number.append(i)

    while done(donearray,procount)==0:
        #print(done(donearray,procount))
        while k < procount :
            if int(at[k]) <= time :
                q.put(k)
                k=k+1
            else :
                break

        if q.qsize()!= 0 :
            x=q.get()
            start[x]=time
            time =time+int(bt[x])
            while k < procount:
                if int(at[k]) <= time:
                    q.put(k)
                    k = k + 1
                else:
                    break

            ct[x] = time
            tat[x] = ct[x] - int(at[x])
            wt[x] = tat[x] - int(bt[x])
            donearray[x] = 1
            end[x]=time
        else :
            time=time+1
            while k < procount:
                if int(at[k]) <= time:
                    q.put(k)
                    k = k + 1
                else:
                    break


    label_ct=Label(root,text="CT").grid(row=0,column=3)
    label_tat=Label(root,text="TAT").grid(row=0,column=4)
    label_wt=Label(root,text="WT").grid(row=0,column=5)

    for i in range(len(ct)):
        label_ct = Label(root, text=ct[i]).grid(row=i+1, column=3)
        label_tat = Label(root, text=tat[i]).grid(row=i + 1, column=4)
        label_wt = Label(root, text=wt[i]).grid(row=i + 1, column=5)
        avgwt=avgwt+wt[i]
        avgtat=avgtat+tat[i]

    label_avgtat = Label(root, text="Average TAT "+str(avgtat)).grid(row=procount+3)
    label_avgwt = Label(root, text="Average WT "+str(avgwt)).grid(row=procount+4)

    w = Canvas(root, width=500, height=100, bg="white")
    color={"blue","green","red","white","black","purple","navy"}

    y=30
    label_color = Label(root, text="Color Guide").grid(row=y)
    y=y+1
    for i in range(len(start)):
        if i==0:
            label_color = Label(root, text="Process 0 - yellow2").grid(row=y)
        if i==1:
            label_color = Label(root, text="Process 1 - PaleGreen2").grid(row=y)
        if i==2:
            label_color = Label(root, text="Process 2 - green2").grid(row=y)
        if i==3:
            label_color = Label(root, text="Process 3 - khaki1").grid(row=y)
        if i==4:
            label_color = Label(root, text="Process 4 - OliveDrab1").grid(row=y)
        if i==5:
            label_color = Label(root, text="Process 5 - tan2").grid(row=y)
        if i==6:
            label_color = Label(root, text="Process 6 - firebrick1").grid(row=y)
        if i==7:
            label_color = Label(root, text="Process 7 - red2").grid(row=y)
        if i==8:
            label_color = Label(root, text="Process 8 - magenta4").grid(row=y)
        if i==9:
            label_color = Label(root, text="Process 9 - MediumPurple2").grid(row=y)
        if i==10:
            label_color = Label(root, text="Process 10 - maroon1").grid(row=y)
        y=y+1

    # dist from left,dist from top,width of each rect,height of each rectangle

    for i in range(len(start)):
        if i==0:
            w.create_rectangle(start[i]*10+5, 20, end[i]*10, 100, fill="yellow2")
        if i==1:
            w.create_rectangle(start[i] * 10 + 5, 20, end[i] * 10, 100, fill="PaleGreen2")
        if i==2:
            w.create_rectangle(start[i] * 10 + 5, 20, end[i] * 10, 100, fill="green2")
        if i==3:
            w.create_rectangle(start[i] * 10 + 5, 20, end[i] * 10, 100, fill="khaki1")
        if i==4:
            w.create_rectangle(start[i] * 10 + 5, 20, end[i] * 10, 100, fill="OliveDrab1")
        if i==5:
            w.create_rectangle(start[i] * 10 + 5, 20, end[i] * 10, 100, fill="tan2")
        if i==6:
            w.create_rectangle(start[i] * 10 + 5, 20, end[i] * 10, 100, fill="firebrick1")
        if i==7:
            w.create_rectangle(start[i] * 10 + 5, 20, end[i] * 10, 100, fill="red2")
        if i==8:
            w.create_rectangle(start[i] * 10 + 5, 20, end[i] * 10, 100, fill="magenta4")
        if i==9:
            w.create_rectangle(start[i] * 10 + 5, 20, end[i] * 10, 100, fill="MediumPurple2")
        if i==10:
            w.create_rectangle(start[i] * 10 + 5, 20, end[i] * 10, 100, fill="maroon1")

    w.grid(row=50)


def sjf(procount,vis,donearray):
    min=999
    mini=0
    global bt
    for i in range(procount):
        if (int(bt[i])<min) and (donearray[i]==0) and (vis[i]==0):
            min=int(bt[i])
            mini=i
    return mini

def sjf_display():
    global at
    global bt
    global procount
    size = 0
    donearray = [0] * procount
    number = []
    ts = []
    ct = [0] * procount
    tat = [0] * procount
    wt = [0] * procount
    start = [0] * procount
    end = [0] * procount
    vis=[0]*procount

    q = Queue(maxsize=100)

    time = 0
    localsize = 0
    avgwt = 0
    avgtat = 0
    k = 0

    for i in range(len(at)):
        number.append(i)

    while done(donearray, procount) == 0:
        # print(done(donearray,procount))
        while k < procount:
            if int(at[k]) <= time:
                localsize=localsize+1
                vis[k]=1
                k = k + 1
            else:
                break

        if localsize!= 0:
            x = sjf(procount,vis,donearray)
            print(x)
            start[x] = time
            time = time + int(bt[x])
            while k < procount:
                if int(at[k]) <= time:
                    localsize=localsize+1
                    vis[k]=1
                    k = k + 1
                else:
                    break

            ct[x] = time
            tat[x] = ct[x] - int(at[x])
            wt[x] = tat[x] - int(bt[x])
            donearray[x] = 1
            end[x] = time
            localsize=localsize-1
        else:
            time = time + 1
            while k < procount:
                if int(at[k]) <= time:
                    localsize=localsize+1
                    vis[k]=1
                    k = k + 1
                else:
                    break

    label_ct = Label(root, text="CT").grid(row=0, column=3)
    label_tat = Label(root, text="TAT").grid(row=0, column=4)
    label_wt = Label(root, text="WT").grid(row=0, column=5)

    for i in range(len(ct)):
        label_ct = Label(root, text=ct[i]).grid(row=i + 1, column=3)
        label_tat = Label(root, text=tat[i]).grid(row=i + 1, column=4)
        label_wt = Label(root, text=wt[i]).grid(row=i + 1, column=5)
        avgwt = avgwt + wt[i]
        avgtat = avgtat + tat[i]

    label_avgtat = Label(root, text="Average TAT " + str(avgtat)).grid(row=procount + 3)
    label_avgwt = Label(root, text="Average WT " + str(avgwt)).grid(row=procount + 4)

    w = Canvas(root, width=500, height=100, bg="white")
    color = {"blue", "green", "red", "white", "black", "purple", "navy"}

    y = 30
    label_color = Label(root, text="Color Guide").grid(row=y)
    y = y + 1
    for i in range(len(start)):
        if i == 0:
            label_color = Label(root, text="Process 0 - yellow2").grid(row=y)
        if i == 1:
            label_color = Label(root, text="Process 1 - PaleGreen2").grid(row=y)
        if i == 2:
            label_color = Label(root, text="Process 2 - green2").grid(row=y)
        if i == 3:
            label_color = Label(root, text="Process 3 - khaki1").grid(row=y)
        if i == 4:
            label_color = Label(root, text="Process 4 - OliveDrab1").grid(row=y)
        if i == 5:
            label_color = Label(root, text="Process 5 - tan2").grid(row=y)
        if i == 6:
            label_color = Label(root, text="Process 6 - firebrick1").grid(row=y)
        if i == 7:
            label_color = Label(root, text="Process 7 - red2").grid(row=y)
        if i == 8:
            label_color = Label(root, text="Process 8 - magenta4").grid(row=y)
        if i == 9:
            label_color = Label(root, text="Process 9 - MediumPurple2").grid(row=y)
        if i == 10:
            label_color = Label(root, text="Process 10 - maroon1").grid(row=y)
        y = y + 1

    # dist from left,dist from top,width of each rect,height of each rectangle

    for i in range(len(start)):
        if i == 0:
            w.create_rectangle(start[i] * 10 + 5, 20, end[i] * 10, 100, fill="yellow2")
        if i == 1:
            w.create_rectangle(start[i] * 10 + 5, 20, end[i] * 10, 100, fill="PaleGreen2")
        if i == 2:
            w.create_rectangle(start[i] * 10 + 5, 20, end[i] * 10, 100, fill="green2")
        if i == 3:
            w.create_rectangle(start[i] * 10 + 5, 20, end[i] * 10, 100, fill="khaki1")
        if i == 4:
            w.create_rectangle(start[i] * 10 + 5, 20, end[i] * 10, 100, fill="OliveDrab1")
        if i == 5:
            w.create_rectangle(start[i] * 10 + 5, 20, end[i] * 10, 100, fill="tan2")
        if i == 6:
            w.create_rectangle(start[i] * 10 + 5, 20, end[i] * 10, 100, fill="firebrick1")
        if i == 7:
            w.create_rectangle(start[i] * 10 + 5, 20, end[i] * 10, 100, fill="red2")
        if i == 8:
            w.create_rectangle(start[i] * 10 + 5, 20, end[i] * 10, 100, fill="magenta4")
        if i == 9:
            w.create_rectangle(start[i] * 10 + 5, 20, end[i] * 10, 100, fill="MediumPurple2")
        if i == 10:
            w.create_rectangle(start[i] * 10 + 5, 20, end[i] * 10, 100, fill="maroon1")

    w.grid(row=50)


def srtf_display():
    global at
    global bt
    global procount
    size=0
    donearray=[0]*procount
    number=[]
    ts=[]
    ct=[0]*procount
    tat=[0]*procount
    wt=[0]*procount

    q=Queue(maxsize=100)

    time = 0
    localsize = 0
    avgwt = 0
    avgtat = 0
    k=0

    for i in range(len(at)):
        number.append(i)

    while done(donearray,procount)==0:
        #print(done(donearray,procount))
        while k < procount :
            if int(at[k]) <= time :
                q.put(k)
                k=k+1
            else :
                break

        if q.qsize()!= 0 :
            x=q.get()
            time =time+int(bt[x])
            while k < procount:
                if int(at[k]) <= time:
                    k = k + 1
                else:
                    break

            ct[x] = time
            tat[x] = ct[x] - int(at[x])
            wt[x] = tat[x] - int(bt[x])
            donearray[x] = 1
        else :
            time=time+1
            while k < procount:
                if int(at[k]) <= time:
                    q.put(k)
                    k = k + 1
                else:
                    break

        isdone=1
        for i in range(len(donearray)):
            if donearray[i] == 0:
                isdone=0
                continue

        if isdone==1:
            break


    label_ct=Label(root,text="CT").grid(row=0,column=3)
    label_tat=Label(root,text="TAT").grid(row=0,column=4)
    label_wt=Label(root,text="WT").grid(row=0,column=5)

    for i in range(len(ct)):
        label_ct = Label(root, text=ct[i]).grid(row=i+1, column=3)
        label_tat = Label(root, text=tat[i]).grid(row=i + 1, column=4)
        label_wt = Label(root, text=wt[i]).grid(row=i + 1, column=5)
        avgwt=avgwt+wt[i]
        avgtat=avgtat+tat[i]

    label_avgtat = Label(root, text="Average TAT "+str(avgtat)).grid(row=procount+3)
    label_avgwt = Label(root, text="Average WT "+str(avgwt)).grid(row=procount+4)


def prionp_display():
    global at
    global bt
    global procount
    size=0
    donearray=[0]*procount
    number=[]
    ts=[]
    ct=[0]*procount
    tat=[0]*procount
    wt=[0]*procount

    q=Queue(maxsize=100)

    time = 0
    localsize = 0
    avgwt = 0
    avgtat = 0
    k=0

    for i in range(len(at)):
        number.append(i)

    while done(donearray,procount)==0:
        #print(done(donearray,procount))
        while k < procount :
            if int(at[k]) <= time :
                q.put(k)
                k=k+1
            else :
                break

        if q.qsize()!= 0 :
            x=q.get()
            time =time+int(bt[x])
            while k < procount:
                if int(at[k]) <= time:
                    k = k + 1
                else:
                    break

            ct[x] = time
            tat[x] = ct[x] - int(at[x])
            wt[x] = tat[x] - int(bt[x])
            donearray[x] = 1
        else :
            time=time+1
            while k < procount:
                if int(at[k]) <= time:
                    q.put(k)
                    k = k + 1
                else:
                    break

        isdone=1
        for i in range(len(donearray)):
            if donearray[i] == 0:
                isdone=0
                continue

        if isdone==1:
            break


    label_ct=Label(root,text="CT").grid(row=0,column=3)
    label_tat=Label(root,text="TAT").grid(row=0,column=4)
    label_wt=Label(root,text="WT").grid(row=0,column=5)

    for i in range(len(ct)):
        label_ct = Label(root, text=ct[i]).grid(row=i+1, column=3)
        label_tat = Label(root, text=tat[i]).grid(row=i + 1, column=4)
        label_wt = Label(root, text=wt[i]).grid(row=i + 1, column=5)
        avgwt=avgwt+wt[i]
        avgtat=avgtat+tat[i]

    label_avgtat = Label(root, text="Average TAT "+str(avgtat)).grid(row=procount+3)
    label_avgwt = Label(root, text="Average WT "+str(avgwt)).grid(row=procount+4)


def pempprio_display():
    global at
    global bt
    global procount
    size=0
    donearray=[0]*procount
    number=[]
    ts=[]
    ct=[0]*procount
    tat=[0]*procount
    wt=[0]*procount

    q=Queue(maxsize=100)

    time = 0
    localsize = 0
    avgwt = 0
    avgtat = 0
    k=0

    for i in range(len(at)):
        number.append(i)

    while done(donearray,procount)==0:
        #print(done(donearray,procount))
        while k < procount :
            if int(at[k]) <= time :
                q.put(k)
                k=k+1
            else :
                break

        if q.qsize()!= 0 :
            x=q.get()
            time =time+int(bt[x])
            while k < procount:
                if int(at[k]) <= time:
                    k = k + 1
                else:
                    break

            ct[x] = time
            tat[x] = ct[x] - int(at[x])
            wt[x] = tat[x] - int(bt[x])
            donearray[x] = 1
        else :
            time=time+1
            while k < procount:
                if int(at[k]) <= time:
                    q.put(k)
                    k = k + 1
                else:
                    break

        isdone=1
        for i in range(len(donearray)):
            if donearray[i] == 0:
                isdone=0
                continue

        if isdone==1:
            break


    label_ct=Label(root,text="CT").grid(row=0,column=3)
    label_tat=Label(root,text="TAT").grid(row=0,column=4)
    label_wt=Label(root,text="WT").grid(row=0,column=5)

    for i in range(len(ct)):
        label_ct = Label(root, text=ct[i]).grid(row=i+1, column=3)
        label_tat = Label(root, text=tat[i]).grid(row=i + 1, column=4)
        label_wt = Label(root, text=wt[i]).grid(row=i + 1, column=5)
        avgwt=avgwt+wt[i]
        avgtat=avgtat+tat[i]

    label_avgtat = Label(root, text="Average TAT "+str(avgtat)).grid(row=procount+3)
    label_avgwt = Label(root, text="Average WT "+str(avgwt)).grid(row=procount+4)

def rr_display():
    global at
    global bt
    global procount
    size=0
    donearray=[0]*procount
    number=[]
    ts=[]
    ct=[0]*procount
    tat=[0]*procount
    wt=[0]*procount

    q=Queue(maxsize=100)

    time = 0
    localsize = 0
    avgwt = 0
    avgtat = 0
    k=0

    for i in range(len(at)):
        number.append(i)

    while done(donearray,procount)==0:
        #print(done(donearray,procount))
        while k < procount :
            if int(at[k]) <= time :
                q.put(k)
                k=k+1
            else :
                break

        if q.qsize()!= 0 :
            x=q.get()
            time =time+int(bt[x])
            while k < procount:
                if int(at[k]) <= time:
                    k = k + 1
                else:
                    break

            ct[x] = time
            tat[x] = ct[x] - int(at[x])
            wt[x] = tat[x] - int(bt[x])
            donearray[x] = 1
        else :
            time=time+1
            while k < procount:
                if int(at[k]) <= time:
                    q.put(k)
                    k = k + 1
                else:
                    break

        isdone=1
        for i in range(len(donearray)):
            if donearray[i] == 0:
                isdone=0
                continue

        if isdone==1:
            break


    label_ct=Label(root,text="CT").grid(row=0,column=3)
    label_tat=Label(root,text="TAT").grid(row=0,column=4)
    label_wt=Label(root,text="WT").grid(row=0,column=5)

    for i in range(len(ct)):
        label_ct = Label(root, text=ct[i]).grid(row=i+1, column=3)
        label_tat = Label(root, text=tat[i]).grid(row=i + 1, column=4)
        label_wt = Label(root, text=wt[i]).grid(row=i + 1, column=5)
        avgwt=avgwt+wt[i]
        avgtat=avgtat+tat[i]

    label_avgtat = Label(root, text="Average TAT "+str(avgtat)).grid(row=procount+3)
    label_avgwt = Label(root, text="Average WT "+str(avgwt)).grid(row=procount+4)



btn_add=Button(root,text="add process",bg="white",fg="black",command=add_pro).grid(row=0)
label_at=Label(root,text="AT").grid(row=0,column=1)
label_bt=Label(root,text="BT").grid(row=0,column=2)
btn_save=Button(root,text="save process",bg="white",fg="black",command=save_pro).grid(row=0,column=6)
btn_print=Button(root,text="print process",bg="white",fg="black",command=print_pro).grid(row=0,column=7)
btn_fcfsdisplay=Button(root,text="display fcfs results",bg="white",fg="black",command=fcfs_display).grid(row=20)
btn_sjfdisplay=Button(root,text="display sjf results",bg="white",fg="black",command=sjf_display).grid(row=21)
btn_srtfdisplay=Button(root,text="display srtf results",bg="white",fg="black",command=srtf_display).grid(row=22)
btn_nppriodisplay=Button(root,text="display np prio results",bg="white",fg="black",command=prionp_display).grid(row=23)
btn_pemppriodisplay=Button(root,text="display pemp prio results",bg="white",fg="black",command=pempprio_display).grid(row=24)
btn_rrdisplay=Button(root,text="display rr results",bg="white",fg="black",command=rr_display).grid(row=25)

root.mainloop()
from tkinter import *
from queue import *

root=Tk()
root.title("Process Scheduling Simulator")
root.configure(background="#a1dbcd")

about=Tk()
about.title("About Process Scheduling Algorithms")
about.configure(background="#a1dbcd")

procount=0
at=[]
bt=[]
prio=[]
at_entry=[int]
bt_entry=[int]
entry_at=Entry()
entry_bt=Entry()
entry_prio=Entry()
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
    global entry_prio

    label_pro=Label(root,text="process "+str(procount)).grid(row=procount+1)

    entry_at=Entry(root)
    entry_at.grid(row=procount+1,column=1)
    #at_entry[procount]=entry_at
    entry_bt = Entry(root)
    entry_bt.grid(row=procount + 1, column=2)
    entry_prio = Entry(root)
    entry_prio.grid(row=procount + 1,column=3)
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
    prio.append(entry_prio.get())
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

    print("prio")
    for i in range(len(prio)):
        print(prio[i])

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


    label_ct=Label(root,text="CT").grid(row=0,column=4)
    label_tat=Label(root,text="TAT").grid(row=0,column=5)
    label_wt=Label(root,text="WT").grid(row=0,column=6)

    for i in range(len(ct)):
        label_ct = Label(root, text=ct[i]).grid(row=i+1, column=4)
        label_tat = Label(root, text=tat[i]).grid(row=i + 1, column=5)
        label_wt = Label(root, text=wt[i]).grid(row=i + 1, column=6)
        avgwt=avgwt+wt[i]
        avgtat=avgtat+tat[i]

    avgtat = avgtat / procount
    avgwt = avgwt / procount
    label_avgtat = Label(root, text="Average TAT "+str(avgtat)).grid(row=procount+3)
    label_avgwt = Label(root, text="Average WT "+str(avgwt)).grid(row=procount+4)

    w = Canvas(root, width=800, height=100, bg="white")
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
    for i in range(len(bt)):
        if (int(bt[i])<min) and (donearray[i]==0) and (vis[i]==1):
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
            x=sjf(procount,vis,donearray)
            #print("min "+str(min)+"mini"+str(x))
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

    label_ct = Label(root, text="CT").grid(row=0, column=4)
    label_tat = Label(root, text="TAT").grid(row=0, column=5)
    label_wt = Label(root, text="WT").grid(row=0, column=6)

    for i in range(len(ct)):
        label_ct = Label(root, text=ct[i]).grid(row=i + 1, column=4)
        label_tat = Label(root, text=tat[i]).grid(row=i + 1, column=5)
        label_wt = Label(root, text=wt[i]).grid(row=i + 1, column=6)
        avgwt = avgwt + wt[i]
        avgtat = avgtat + tat[i]

    avgtat=avgtat/procount
    avgwt=avgwt/procount
    label_avgtat = Label(root, text="Average TAT " + str(avgtat)).grid(row=procount + 3)
    label_avgwt = Label(root, text="Average WT " + str(avgwt)).grid(row=procount + 4)

    w = Canvas(root, width=800, height=100, bg="white")
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
    size = 0
    donearray = [0] * procount
    number = []
    ts = [0]*procount
    ct = [0] * procount
    tat = [0] * procount
    wt = [0] * procount
    start = [0] * procount
    end = [0] * procount
    vis = [0] * procount
    start = [0] * 100
    end = [0] * 100
    startvar=0
    endvar=0

    q = Queue(maxsize=100)

    time = 0
    localsize = 0
    avgwt = 0
    avgtat = 0
    k = 0
    count=0

    w = Canvas(root, width=800, height=100, bg="white")

    for i in range(len(at)):
        number.append(i)

    while done(donearray, procount) == 0:
        # print(done(donearray,procount))
        while k < procount:
            if int(at[k]) <= time:
                localsize = localsize + 1
                vis[k] = 1
                k = k + 1
            else:
                break

        if localsize != 0:
            x = sjf(procount, vis, donearray)
            # print("min "+str(min)+"mini"+str(x))
            #start[count]=time
            startvar =time
            count=count+1
            time = time + 1
            #end[count]=time

            endvar=time

            if x == 0:
                w.create_rectangle(startvar * 10, 20, endvar * 10, 100, fill="yellow2")
            if x == 1:
                w.create_rectangle(startvar * 10, 20, endvar * 10, 100, fill="PaleGreen2")
            if x == 2:
                w.create_rectangle(startvar * 10 , 20, endvar * 10, 100, fill="green2")
            if x == 3:
                w.create_rectangle(startvar * 10, 20, endvar * 10, 100, fill="khaki1")
            if x == 4:
                w.create_rectangle(startvar * 10, 20, endvar * 10, 100, fill="OliveDrab1")
            if x == 5:
                w.create_rectangle(startvar * 10 , 20, endvar * 10, 100, fill="tan2")
            if x == 6:
                w.create_rectangle(startvar * 10, 20, endvar * 10, 100, fill="firebrick1")
            if x == 7:
                w.create_rectangle(startvar * 10 , 20, endvar * 10, 100, fill="red2")
            if x == 8:
                w.create_rectangle(startvar * 10, 20, endvar * 10, 100, fill="magenta4")
            if x == 9:
                w.create_rectangle(startvar * 10 , 20, endvar * 10, 100, fill="MediumPurple2")
            if x == 10:
                w.create_rectangle(startvar * 10, 20, endvar * 10, 100, fill="maroon1")


            while k < procount:
                if int(at[k]) <= time:
                    localsize = localsize + 1
                    vis[k] = 1
                    k = k + 1
                else:
                    break

            ts[x]=ts[x]+1
            if(ts[x]>=int(bt[x])):
                ct[x] = time
                tat[x] = ct[x] - int(at[x])
                wt[x] = tat[x] - int(bt[x])
                donearray[x] = 1

                localsize = localsize - 1
            else:
                time=time+1
                while k < procount:
                    if int(at[k]) <= time:
                        localsize = localsize + 1
                        vis[k] = 1
                        k = k + 1
                    else:
                        break

        else:
            time = time + 1
            while k < procount:
                if int(at[k]) <= time:
                    localsize = localsize + 1
                    vis[k] = 1
                    k = k + 1
                else:
                    break

    label_ct = Label(root, text="CT").grid(row=0, column=4)
    label_tat = Label(root, text="TAT").grid(row=0, column=5)
    label_wt = Label(root, text="WT").grid(row=0, column=6)

    for i in range(len(ct)):
        label_ct = Label(root, text=ct[i]).grid(row=i + 1, column=4)
        label_tat = Label(root, text=tat[i]).grid(row=i + 1, column=5)
        label_wt = Label(root, text=wt[i]).grid(row=i + 1, column=6)
        avgwt = avgwt + wt[i]
        avgtat = avgtat + tat[i]

    avgtat = avgtat / procount
    avgwt = avgwt / procount
    label_avgtat = Label(root, text="Average TAT " + str(avgtat)).grid(row=procount + 3)
    label_avgwt = Label(root, text="Average WT " + str(avgwt)).grid(row=procount + 4)

    y = 30
    label_color = Label(root, text="Color Guide").grid(row=y)
    y = y + 1
    for i in range(len(at)):
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

    w.grid(row=50)


def pickprio(procount,vis,donearray,prio):
    min=999
    mini=0
    for i in range(len(prio)):
        if (int(prio[i])<min) and (donearray[i]==0) and (vis[i]==1):
            min=int(prio[i])
            mini=i
    return mini


def prionp_display():
    global at
    global bt
    global procount
    global prio
    size = 0
    donearray = [0] * procount
    number = []
    ts = []
    ct = [0] * procount
    tat = [0] * procount
    wt = [0] * procount
    start = [0] * procount
    end = [0] * procount
    vis = [0] * procount

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
                localsize = localsize + 1
                vis[k] = 1
                k = k + 1
            else:
                break

        if localsize != 0:
            x = pickprio(procount, vis, donearray,prio)
            # print("min "+str(min)+"mini"+str(x))
            start[x] = time
            time = time + int(bt[x])
            while k < procount:
                if int(at[k]) <= time:
                    localsize = localsize + 1
                    vis[k] = 1
                    k = k + 1
                else:
                    break

            ct[x] = time
            tat[x] = ct[x] - int(at[x])
            wt[x] = tat[x] - int(bt[x])
            donearray[x] = 1
            end[x] = time
            localsize = localsize - 1
        else:
            time = time + 1
            while k < procount:
                if int(at[k]) <= time:
                    localsize = localsize + 1
                    vis[k] = 1
                    k = k + 1
                else:
                    break

    label_ct = Label(root, text="CT").grid(row=0, column=4)
    label_tat = Label(root, text="TAT").grid(row=0, column=5)
    label_wt = Label(root, text="WT").grid(row=0, column=6)

    for i in range(len(ct)):
        label_ct = Label(root, text=ct[i]).grid(row=i + 1, column=4)
        label_tat = Label(root, text=tat[i]).grid(row=i + 1, column=5)
        label_wt = Label(root, text=wt[i]).grid(row=i + 1, column=6)
        avgwt = avgwt + wt[i]
        avgtat = avgtat + tat[i]

    avgtat = avgtat / procount
    avgwt = avgwt / procount
    label_avgtat = Label(root, text="Average TAT " + str(avgtat)).grid(row=procount + 3)
    label_avgwt = Label(root, text="Average WT " + str(avgwt)).grid(row=procount + 4)

    w = Canvas(root, width=800, height=100, bg="white")
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


def pempprio_display():
    global at
    global bt
    global procount
    global prio
    size = 0
    donearray = [0] * procount
    number = []
    ts = [0]*procount
    ct = [0] * procount
    tat = [0] * procount
    wt = [0] * procount
    start = [0] * procount
    end = [0] * procount
    vis = [0] * procount
    startvar = 0
    endvar = 0

    q = Queue(maxsize=100)

    time = 0
    localsize = 0
    avgwt = 0
    avgtat = 0
    k = 0
    count = 0

    w = Canvas(root, width=800, height=100, bg="white")

    for i in range(len(at)):
        number.append(i)

    while done(donearray, procount) == 0:
        # print(done(donearray,procount))
        while k < procount:
            if int(at[k]) <= time:
                localsize = localsize + 1
                vis[k] = 1
                k = k + 1
            else:
                break

        if localsize != 0:
            x = pickprio(procount, vis, donearray, prio)
            # print("min "+str(min)+"mini"+str(x))
            startvar = time
            time = time + 1
            endvar = time

            if x == 0:
                w.create_rectangle(startvar * 10, 20, endvar * 10, 100, fill="yellow2")
            if x == 1:
                w.create_rectangle(startvar * 10, 20, endvar * 10, 100, fill="PaleGreen2")
            if x == 2:
                w.create_rectangle(startvar * 10 , 20, endvar * 10, 100, fill="green2")
            if x == 3:
                w.create_rectangle(startvar * 10, 20, endvar * 10, 100, fill="khaki1")
            if x == 4:
                w.create_rectangle(startvar * 10, 20, endvar * 10, 100, fill="OliveDrab1")
            if x == 5:
                w.create_rectangle(startvar * 10 , 20, endvar * 10, 100, fill="tan2")
            if x == 6:
                w.create_rectangle(startvar * 10, 20, endvar * 10, 100, fill="firebrick1")
            if x == 7:
                w.create_rectangle(startvar * 10 , 20, endvar * 10, 100, fill="red2")
            if x == 8:
                w.create_rectangle(startvar * 10, 20, endvar * 10, 100, fill="magenta4")
            if x == 9:
                w.create_rectangle(startvar * 10 , 20, endvar * 10, 100, fill="MediumPurple2")
            if x == 10:
                w.create_rectangle(startvar * 10, 20, endvar * 10, 100, fill="maroon1")

            while k < procount:
                if int(at[k]) <= time:
                    localsize = localsize + 1
                    vis[k] = 1
                    k = k + 1
                else:
                    break

            ts[x] = ts[x] + 1
            if (ts[x] >= bt[x]):
                ct[x] = time
                tat[x] = ct[x] - int(at[x])
                wt[x] = tat[x] - int(bt[x])
                donearray[x] = 1

                localsize = localsize - 1
            else:
                time = time + 1
                while k < procount:
                    if int(at[k]) <= time:
                        localsize = localsize + 1
                        vis[k] = 1
                        k = k + 1
                    else:
                        break

        else:
            time = time + 1
            while k < procount:
                if int(at[k]) <= time:
                    localsize = localsize + 1
                    vis[k] = 1
                    k = k + 1
                else:
                    break

    label_ct = Label(root, text="CT").grid(row=0, column=4)
    label_tat = Label(root, text="TAT").grid(row=0, column=5)
    label_wt = Label(root, text="WT").grid(row=0, column=6)

    for i in range(len(ct)):
        label_ct = Label(root, text=ct[i]).grid(row=i + 1, column=4)
        label_tat = Label(root, text=tat[i]).grid(row=i + 1, column=5)
        label_wt = Label(root, text=wt[i]).grid(row=i + 1, column=6)
        avgwt = avgwt + wt[i]
        avgtat = avgtat + tat[i]

    avgtat = avgtat / procount
    avgwt = avgwt / procount
    label_avgtat = Label(root, text="Average TAT " + str(avgtat)).grid(row=procount + 3)
    label_avgwt = Label(root, text="Average WT " + str(avgwt)).grid(row=procount + 4)

    y = 30
    label_color = Label(root, text="Color Guide").grid(row=y)
    y = y + 1
    for i in range(len(at)):
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

    w.grid(row=50)


def rr_display():
    #global entry_tq
    tq=int(entry_tq.get())
    print(tq)
    global at
    global bt
    global procount
    global prio
    size = 0
    donearray = [0] * procount
    number = []
    ts = [0] * procount
    ct = [0] * procount
    tat = [0] * procount
    wt = [0] * procount
    start = [0] * procount
    end = [0] * procount
    vis = [0] * procount
    startvar = 0
    endvar = 0

    q = Queue(maxsize=100)

    time = 0
    localsize = 0
    avgwt = 0
    avgtat = 0
    k = 0
    count = 0

    w = Canvas(root, width=800, height=100, bg="white")

    for i in range(len(at)):
        number.append(i)

    while done(donearray, procount) == 0:
        print(done(donearray,procount))
        while k < procount:
            if int(at[k]) <= time:
                q.put(k)
                localsize = localsize + 1
                vis[k] = 1
                k = k + 1
            else:
                break

        if localsize != 0:
            x=q.get()
            startvar=time
            time = time + tq
            ts[x]=ts[x]+tq
            count+=1
            endvar=time

            if x == 0:
                w.create_rectangle(startvar * 10, 20, endvar * 10, 100, fill="yellow2")
            if x == 1:
                w.create_rectangle(startvar * 10, 20, endvar * 10, 100, fill="PaleGreen2")
            if x == 2:
                w.create_rectangle(startvar * 10 , 20, endvar * 10, 100, fill="green2")
            if x == 3:
                w.create_rectangle(startvar * 10, 20, endvar * 10, 100, fill="khaki1")
            if x == 4:
                w.create_rectangle(startvar * 10, 20, endvar * 10, 100, fill="OliveDrab1")
            if x == 5:
                w.create_rectangle(startvar * 10 , 20, endvar * 10, 100, fill="tan2")
            if x == 6:
                w.create_rectangle(startvar * 10, 20, endvar * 10, 100, fill="firebrick1")
            if x == 7:
                w.create_rectangle(startvar * 10 , 20, endvar * 10, 100, fill="red2")
            if x == 8:
                w.create_rectangle(startvar * 10, 20, endvar * 10, 100, fill="magenta4")
            if x == 9:
                w.create_rectangle(startvar * 10 , 20, endvar * 10, 100, fill="MediumPurple2")
            if x == 10:
                w.create_rectangle(startvar * 10, 20, endvar * 10, 100, fill="maroon1")

            while k < procount:
                if int(at[k]) <= time:
                    q.put(k)
                    localsize = localsize + 1
                    vis[k] = 1
                    k = k + 1
                else:
                    break

            if (ts[x] >= int(bt[x])):
                time=time-(ts[x]-int(bt[x]))
                ct[x]=time
                tat[x] = ct[x] - int(at[x])
                wt[x] = tat[x] - int(bt[x])
                donearray[x] = 1
                localsize = localsize - 1
            else:
                q.put(x)

        else:
            time = time + 1
            while k < procount:
                if int(at[k]) <= time:
                    q.put(k)
                    localsize = localsize + 1
                    vis[k] = 1
                    k = k + 1
                else:
                    break

    label_ct = Label(root, text="CT").grid(row=0, column=4)
    label_tat = Label(root, text="TAT").grid(row=0, column=5)
    label_wt = Label(root, text="WT").grid(row=0, column=6)

    for i in range(len(ct)):
        label_ct = Label(root, text=ct[i]).grid(row=i + 1, column=4)
        label_tat = Label(root, text=tat[i]).grid(row=i + 1, column=5)
        label_wt = Label(root, text=wt[i]).grid(row=i + 1, column=6)
        avgwt = avgwt + wt[i]
        avgtat = avgtat + tat[i]

    avgtat = avgtat / procount
    avgwt = avgwt / procount
    label_avgtat = Label(root, text="Average TAT " + str(avgtat)).grid(row=procount + 3)
    label_avgwt = Label(root, text="Average WT " + str(avgwt)).grid(row=procount + 4)

    y = 30
    label_color = Label(root, text="Color Guide").grid(row=y)
    y = y + 1
    for i in range(len(at)):
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

    w.grid(row=50)


def multi_display():
    tq = int(entry_tq.get())
    print(tq)
    global at
    global bt
    global procount
    global prio
    ind=0
    n1=0
    n2=0

    for i in range(len(prio)):
        if prio[i]==1:
            n1=n1+1
        if prio[i] == 2:
            n2 = n2 + 1

    #print(str(n1))
    size = 0
    donearray = [0] * procount
    number = []
    ts = [0] * procount
    ct = [0] * procount
    tat = [0] * procount
    wt = [0] * procount
    start = [0] * procount
    end = [0] * procount
    vis = [0] * procount
    startvar=0
    endvar=0

    q1 = Queue(maxsize=100)
    q2 = Queue(maxsize=100)

    time = 0
    localsizehigh = 0
    localsizelow = 0
    avgwt = 0
    avgtat = 0
    k1 = 0
    k2=n1
    count = 0

    w = Canvas(root, width=800, height=100, bg="white")

    for i in range(len(at)):
        number.append(i)

    while done(donearray, procount) == 0:
        #print(done(donearray, procount))
        while k1 < n1:
            if int(at[k1]) <= time:
                q1.put(k1)
                localsizehigh = localsizehigh + 1
                vis[k1] = 1
                k1 = k1 + 1
            else:
                break

        while k2 < procount:
            if int(at[k2]) <= time:
                q2.put(k2)
                localsizelow = localsizelow + 1
                vis[k2] = 1
                k2 = k2 + 1
            else:
                break

        if localsizehigh != 0:
            x = q1.get()
            startvar=time
            time = time + tq
            ts[x] = ts[x] + tq
            count+=1
            endvar=time

            if x == 0:
                w.create_rectangle(startvar * 10, 20, endvar * 10, 100, fill="yellow2")
            if x == 1:
                w.create_rectangle(startvar * 10, 20, endvar * 10, 100, fill="PaleGreen2")
            if x == 2:
                w.create_rectangle(startvar * 10 , 20, endvar * 10, 100, fill="green2")
            if x == 3:
                w.create_rectangle(startvar * 10, 20, endvar * 10, 100, fill="khaki1")
            if x == 4:
                w.create_rectangle(startvar * 10, 20, endvar * 10, 100, fill="OliveDrab1")
            if x == 5:
                w.create_rectangle(startvar * 10 , 20, endvar * 10, 100, fill="tan2")
            if x == 6:
                w.create_rectangle(startvar * 10, 20, endvar * 10, 100, fill="firebrick1")
            if x == 7:
                w.create_rectangle(startvar * 10 , 20, endvar * 10, 100, fill="red2")
            if x == 8:
                w.create_rectangle(startvar * 10, 20, endvar * 10, 100, fill="magenta4")
            if x == 9:
                w.create_rectangle(startvar * 10 , 20, endvar * 10, 100, fill="MediumPurple2")
            if x == 10:
                w.create_rectangle(startvar * 10, 20, endvar * 10, 100, fill="maroon1")

            while k1 < n1:
                if int(at[k1]) <= time:
                    q1.put(k1)
                    localsizehigh = localsizehigh + 1
                    vis[k1] = 1
                    k1 = k1 + 1
                else:
                    break

            while k2 < procount:
                if int(at[k2]) <= time:
                    q2.put(k2)
                    localsizelow = localsizelow + 1
                    vis[k2] = 1
                    k2 = k2 + 1
                else:
                    break

            if (ts[x] >= int(bt[x])):
                time = time - (ts[x] - int(bt[x]))
                ct[x] = time
                tat[x] = ct[x] - int(at[x])
                wt[x] = tat[x] - int(bt[x])
                donearray[x] = 1
                localsizehigh = localsizehigh - 1
            else:
                q1.put(x)

        elif localsizelow!=0:
            x = q2.get()
            startvar=time
            time = time + int(bt[x])
            count+=1
            endvar=time

            if x == 0:
                w.create_rectangle(startvar * 10, 20, endvar * 10, 100, fill="yellow2")
            if x == 1:
                w.create_rectangle(startvar * 10, 20, endvar * 10, 100, fill="PaleGreen2")
            if x == 2:
                w.create_rectangle(startvar * 10 , 20, endvar * 10, 100, fill="green2")
            if x == 3:
                w.create_rectangle(startvar * 10, 20, endvar * 10, 100, fill="khaki1")
            if x == 4:
                w.create_rectangle(startvar * 10, 20, endvar * 10, 100, fill="OliveDrab1")
            if x == 5:
                w.create_rectangle(startvar * 10 , 20, endvar * 10, 100, fill="tan2")
            if x == 6:
                w.create_rectangle(startvar * 10, 20, endvar * 10, 100, fill="firebrick1")
            if x == 7:
                w.create_rectangle(startvar * 10 , 20, endvar * 10, 100, fill="red2")
            if x == 8:
                w.create_rectangle(startvar * 10, 20, endvar * 10, 100, fill="magenta4")
            if x == 9:
                w.create_rectangle(startvar * 10 , 20, endvar * 10, 100, fill="MediumPurple2")
            if x == 10:
                w.create_rectangle(startvar * 10, 20, endvar * 10, 100, fill="maroon1")

            while k1 < n1:
                if int(at[k1]) <= time:
                    q1.put(k1)
                    localsizehigh = localsizehigh + 1
                    vis[k1] = 1
                    k1 = k1 + 1
                else:
                    break

            while k2 < procount:
                if int(at[k2]) <= time:
                    q2.put(k2)
                    localsizelow = localsizelow + 1
                    vis[k2] = 1
                    k2 = k2 + 1
                else:
                    break

            ct[x] = time
            tat[x] = ct[x] - int(at[x])
            wt[x] = tat[x] - int(bt[x])
            donearray[x] = 1
            localsizelow=localsizelow-1

        else:
            time=time+1


    label_ct = Label(root, text="CT").grid(row=0, column=4)
    label_tat = Label(root, text="TAT").grid(row=0, column=5)
    label_wt = Label(root, text="WT").grid(row=0, column=6)

    for i in range(len(ct)):
        label_ct = Label(root, text=ct[i]).grid(row=i + 1, column=4)
        label_tat = Label(root, text=tat[i]).grid(row=i + 1, column=5)
        label_wt = Label(root, text=wt[i]).grid(row=i + 1, column=6)
        avgwt = avgwt + wt[i]
        avgtat = avgtat + tat[i]

    avgtat = avgtat / procount
    avgwt = avgwt / procount
    label_avgtat = Label(root, text="Average TAT " + str(avgtat)).grid(row=procount + 3)
    label_avgwt = Label(root, text="Average WT " + str(avgwt)).grid(row=procount + 4)

    y = 30
    label_color = Label(root, text="Color Guide").grid(row=y)
    y = y + 1
    for i in range(len(at)):
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

    w.grid(row=50)




btn_add=Button(root,text="Add Process",bg="white",fg="black",command=add_pro).grid(row=0)
label_at=Label(root,text="AT").grid(row=0,column=1)
label_bt=Label(root,text="BT").grid(row=0,column=2)
label_prio=Label(root,text="Priority").grid(row=0,column=3)
btn_save=Button(root,text="Save Process",bg="white",fg="black",command=save_pro).grid(row=0,column=7)
btn_print=Button(root,text="Print Processes",bg="white",fg="black",command=print_pro).grid(row=0,column=8)
btn_fcfsdisplay=Button(root,text="Display FCFS Results",bg="white",fg="black",command=fcfs_display).grid(row=20)
btn_sjfdisplay=Button(root,text="Display SJF Results",bg="white",fg="black",command=sjf_display).grid(row=21)
btn_srtfdisplay=Button(root,text="Display SRTF Results",bg="white",fg="black",command=srtf_display).grid(row=22)
btn_nppriodisplay=Button(root,text="Display Non-preemptive Priority Results",bg="white",fg="black",command=prionp_display).grid(row=23)
btn_pemppriodisplay=Button(root,text="Display Pre-emptive Priority Results",bg="white",fg="black",command=pempprio_display).grid(row=24)
btn_rrdisplay=Button(root,text="Display RR Results",bg="white",fg="black",command=rr_display).grid(row=25)

btn_multidisplay=Button(root,text="Display MultiLevel Queue (MLQ) Results",bg="white",fg="black",command=multi_display).grid(row=25)

label_tq=Label(root,text="Enter time quantum for Round Robin").grid(row=18)
entry_tq=Entry(root)
entry_tq.grid(row=19)


def disp_fcfs():
    about_fcfs=Toplevel()
    about_fcfs.title("First Come First Serve (FCFS) Scheduling")
    about_fcfs.configure(background="#a1dbcd")
    txtabout = Label(about_fcfs, text="Other names of this algorithm are:\n" \
           "First-In-First-Out (FIFO)\n" \
           "Run-to-Completion\n" \
           "Run-Until-Done\n\n" \
           "Perhaps, First-Come-First-Served algorithm is the simplest scheduling algorithm is the simplest scheduling algorithm. \n" \
           "Processes are dispatched according to their arrival time on the ready queue. Being a nonpreemptive discipline, once a \n" \
           "process has a CPU, it runs to completion. The FCFS scheduling is fair in the formal sense or human sense of fairness \n" \
           "but it is unfair in the sense that long jobs make short jobs wait and unimportant jobs make important jobs wait.\n" \
           "\n\nFCFS is more predictable than most of other schemes since it offers time. FCFS scheme is not useful in scheduling \n" \
           "interactive users because it cannot guarantee good response time. The code for FCFS scheduling  is simple to write \n" \
           "and understand. One of the major drawback of this scheme is that the average time is often quite long. "
           "\n\nThe First-Come-First-Served algorithm is rarely used as a master scheme in modern operating systems but it is \n" \
           "often embedded within other schemes.").pack()

def disp_sjf():
    about_sjf = Toplevel()
    about_sjf.title("Shortest Job First (SJF) Scheduling")
    about_sjf.configure(background="#a1dbcd")
    txtabout = Label(about_sjf,
                text="Other name of this algorithm is Shortest-Process-Next (SPN).\n\n"
                    "Shortest-Job-First (SJF) is a non-preemptive discipline in which waiting job (or process) with the smallest \n"\
                     "estimated run-time-to-completion is run next. In other words, when CPU is available, it is assigned to the \n"\
                     "process that has smallest next CPU burst.The SJF scheduling is especially appropriate for batch jobs for \n"\
                     "which the run times are known in advance. Since the SJF scheduling algorithm gives the minimum average time \n"\
                     "for  a given set of processes, it is probably optimal.\n\n"\
                    "The SJF algorithm favors short jobs (or processors) at the expense of longer ones.\n"\
                     "The obvious problem with SJF scheme is that it requires precise knowledge of how long a job or process will \n"\
                     "run, and this information is not usually available.\n\n"\
                    "The best SJF algorithm can do is to rely on user estimates of run times.\n"\
                     "In the production environment where the same jobs run regularly, it may be possible to provide reasonable \n"\
                     "estimate of run time, based on the past performance of the process. But in the development environment \n"\
                     "users rarely know how their program will execute.\n"\
                     "Like FCFS, SJF is non preemptive therefore, it is not useful in timesharing environment in which reasonable\n"\
                    "response time must be guaranteed.\n").pack()

def disp_srtf():
    about_srtf = Toplevel()
    about_srtf.title("Shortest Remaining Time First (SRTF) Scheduling")
    about_srtf.configure(background="#a1dbcd")
    txtabout = Label(about_srtf,
                text="The SRTF is the preemptive counterpart of SJF and useful in time-sharing environment.\n"
                     "In SRTF scheduling, the process with the smallest estimated run-time to completion is run next,including new arrivals.\n\n"
                     "In SJF scheme, once a job begin executing, it run to completion.\n"
                     "In SRTF scheme, a running process may be preempted by a new arrival process with shortest estimated run-time.\n\n"
                     "The algorithm SRTF has higher overhead than its counterpart SJF.\n\n"
                     "The SRTF must keep track of the elapsed time of the running process and must handle occasional preemptions.\n"
                     "In this scheme, arrival of small processes will run almost immediately. However, longer jobs have even longer mean waiting time.\n").pack()

def disp_prio():
    about_prio = Toplevel()
    about_prio.title("Priority Scheduling")
    about_prio.configure(background="#a1dbcd")
    txtabout = Label(about_prio,
                text="Priority scheduling can be either preemptive or non preemptive\n" \
           "A preemptive priority algorithm will preemptive the CPU if the priority of the newly arrival process is higher \n"
            "than the priority of the currently running process.A non-preemptive priority algorithm will simply put the \n"
            "new process at the head of the ready queue.A major problem with priority scheduling is indefinite blocking \n"
            "or starvation. A solution to the problem of indefinite blockage of the low-priority process is aging.\n"
            "Aging is a technique of gradually increasing the priority of processes that wait in the system for a long period of time.\n" \
           "\n\nThe basic idea is straightforward: each process is assigned a priority, and priority is allowed to run.\n"
            "Equal-Priority processes are scheduled in FCFS order. The shortest-Job-First (SJF) algorithm is a special \n"
            "case of general priority scheduling algorithm. An SJF algorithm is simply a priority algorithm where the \n"
            "priority is the inverse of the (predicted) next CPU burst. That is, the longer the CPU burst, the lower the \n"
            "priority and vice versa. Priority can be defined either internally or externally. Internally defined \n"
            "priorities use some measurable quantities or qualities to compute priority of a process.\n" \
           "\n\nExamples of Internal priorities are\n" \
           "Time limits\n" \
           "Memory requirements.\n" \
           "File requirements,\n" \
           "    for example, number of open files.\n" \
           "CPU Vs I/O requirements.\n" \
           "\nExternally defined priorities are set by criteria that are external to operating system such as\n" \
           "The importance of process.\n" \
           "Type or amount of funds being paid for computer use.\n" \
           "The department sponsoring the work.\n" \
           "Politics.\n").pack()

def disp_rr():
    about_rr = Toplevel()
    about_rr.title("Round Robin Scheduling")
    about_rr.configure(background="#a1dbcd")
    txtabout = Label(about_rr,
                text="One of the oldest, simplest, fairest and most widely used algorithm is round robin (RR).In the round robin \n"
                     "scheduling, processes are dispatched in a FIFO manner but are given a limited amount of CPU time called a \n"
                     "time-slice or a quantum.If a process does not complete before its CPU-time expires, the CPU is preempted and \n"
                     "given to the next process waiting in a queue. The preempted process is then placed at the back of the ready list.\n\n"
                     "Round Robin Scheduling is preemptive (at the end of time-slice) therefore it is effective in time-sharing \n"
                     "environments in which the system needs to guarantee reasonable response times for interactive users.\n\n"
                     "The only interesting issue with round robin scheme is the length of the quantum. Setting the quantum too \n"
                     "short causes too many context switches and lower the CPU efficiency. On the other hand, setting the quantum \n"
                     "too long may cause poor response time and appoximates FCFS.\n\n"
                     "In any event, the average waiting time under round robin scheduling is often quite long.\n").pack()

def disp_mlq():
    about_mlq = Toplevel()
    about_mlq.title("Multi Level Queue (MLQ) Scheduling")
    about_mlq.configure(background="#a1dbcd")
    txtabout = Label(about_mlq,
                text="\nAnother class of scheduling algorithms has been created for situations in which processes are \n"
                     "easily classified into different groups.For example, a common division is made between \n"
                     "foreground (interactive) processes and background (batch) processes. These two types of\n" \
           "processes have different response-time requirements and so may have different scheduling needs. In \n" \
           "addition, foreground processes may have priority (externally defined) over background processes.\n" \
           "\nA multilevel queue scheduling algorithm partitions the ready queue into several separate queues. \n"
            "The processes are permanently assigned to one queue, generally based on some property of the \n"
            "process, such as memory size, process priority, or process type. Each queue has its own scheduling\n" \
           "algorithm. For example, separate queues might be used for foreground and background processes. The \n"
           "foreground queue might be scheduled by an RR algorithm, while the background queue is scheduled by \n"
           "an FCFS algorithm. In addition, there must be scheduling among the queues, which is commonly\n" \
           "implemented as fixed-priority preemptive scheduling. For example, the foreground queue may have absolute \n"
                     "priority over the background queue.\n").pack()

abouttxt="A Process Scheduler schedules different processes to be assigned to the CPU based on particular scheduling algorithms.\n\n " \
         "There are seven popular process scheduling algorithms that have been simulated in this simulator −\n" \
      "First-Come, First-Served (FCFS) Scheduling\nShortest-Job-Next (SJN) Scheduling\nPriority Scheduling\n" \
         "Shortest Remaining Time\nRound Robin(RR) Scheduling\nMultiple-Level Queues Scheduling\n\n" \
      "These algorithms are either non-preemptive or preemptive. \n" \
         "Non-preemptive algorithms are designed so that once a process enters the running state, it cannot be \n" \
         "preempted until it completes its allotted time, whereas the preemptive scheduling is based on priority \n" \
         "where a scheduler may preempt a low priority running process anytime when a high priority process \n" \
         "enters into a ready state.\n"

intro=Label(about,text="What is Process Scheduling\n\n").grid(row=0)
txtabout=Label(about,text=abouttxt).grid(row=3)
about_fcfs=Button(about,text="What is FCFS Scheduling",bg="white",fg="black",command=disp_fcfs).grid(row=4)
about_sjf=Button(about,text="What is SJF Scheduling",bg="white",fg="black",command=disp_sjf).grid(row=5)
about_srtf=Button(about,text="What is SRTF Scheduling",bg="white",fg="black",command=disp_srtf).grid(row=6)
about_prio=Button(about,text="What is Priority Scheduling",bg="white",fg="black",command=disp_prio).grid(row=7)
about_rr=Button(about,text="What is Round Robin Scheduling",bg="white",fg="black",command=disp_rr).grid(row=8)
about_mlq=Button(about,text="What is Multi-Level Queue Scheduling",bg="white",fg="black",command=disp_mlq).grid(row=9)

root.mainloop()
about.mainloop()
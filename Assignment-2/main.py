from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg,  NavigationToolbar2Tk

root = Tk()

individualContacts = dict()
grpToMembers = dict()
memberToGrp = dict()
message = dict()
listOfUsers = list()
curr = "1"


with open("social_network.txt") as f:
    line = f.readline()
    flag = 0
    while True:
        line = f.readline()
        if(line.strip() == "" and flag == 1):
            break
        if(line.strip() == "" and flag == 0):
            continue
        if(line[1:7] == "groups"):
            line = f.readline()
            flag = 1
        user = line[1]
        l = list()
        
        line1 = line[4:-2]
        line1 = ''.join(line1.split())
        l = line1.split(',')
        if(flag == 0):
            individualContacts[user] = l
        else:
            grpToMembers[user] = l                                              
        

for member in individualContacts:
    listOfUsers.append(member)

for member in grpToMembers:
    l = grpToMembers[member]
    for j in l:
        memberToGrp[j] = []

for member in grpToMembers:
    l = grpToMembers[member]
    for j in l:
        memberToGrp[j].append(member)


def refresh(self):
    self.destroy()
    self.__init__()
    root.geometry("1366x768")
    root.title("Chat Room")
    
    with open("messages.txt","w") as messagefile:
        for key in message:
            l = message[key]
            messagefile.write(key + ":" )
            for item in l: 
                messagefile.write(item[0] + '\n')

    f0 = Frame(root, background="#f5e9bf", width=10, height=200)
    variable = StringVar(f0)
    txt = Text(root , width = 30 , height = 2)
    w = OptionMenu(f0, variable, *listOfUsers)
    w.pack(pady=20)
    w.config(background="#bf9556",fg="#002b87",bd=5)

    def clicked():
        global curr
        curr = variable.get()
        if curr not in listOfUsers:
            messagebox.showerror("Error", "No user selected : Select user first and then continue working")
        else:
            refresh(root)
        
    b1 = Button(f0, text="Select", command=clicked,width=15,height=2,background="#bf9556",fg="#002b87",bd=5)
    b1.pack(pady=10)
    txt2 = Text(root , width = 30 , height = 2)
    label0 = Label(f0,text="Current user : " + curr, height=2,width=15,background="#bf9556",fg="#002b87",relief=RAISED).pack(pady=50)
    b = Button(f0, text="Exit", command=root.quit,width=15,height=2,background="#bf9556",fg="#002b87",bd=5)
    b.pack(pady = (350,0))
    
    f1 = Frame(root, background="#97f0c0", width=10, height=100)
    f2 = Frame(root, background="pink", width=10, height=100)
    f3 = Frame(root, background="#b8f0b4", width=10, height=100)
    f4 = Frame(root, background="#f5cbd3", width=10, height=100)
    f0.grid(row=0, column=0, rowspan=2, sticky="nsew")
    txt3 = Text(root , width = 30 , height = 2)
    f1.grid(row=0, column=1, sticky="nsew")
    label1 = Label(f1, text="Post Something",font=50,background="#ad501d", relief=RAISED,fg="#002b87",width=16,height=2)
    label1.grid(row=0,column=0,pady=(10,0), padx=5,columnspan=3)
    label2 = Label(f1, text="Group / Indiviudual : ",background="#bf9556",fg="#002b87",relief=RAISED).grid(row=1,column=0,pady=30)

    v1 = StringVar()
    lis7 = Listbox(root , width = 15 , height = 2)
    R1 = Radiobutton(f1, text="Group", variable=v1, value="1")
    R2 = Radiobutton(f1, text="Individual", variable=v1, value="2")
    R1.grid(row=1,column=1,pady=5)
    R2.grid(row=1,column=2,pady=5)
    labh = Label(root , text = "root_label" , width = 20 , height = 2)
    R1.config(background="#bf9556",fg="#002b87")
    R2.config(background="#bf9556",fg="#002b87")
    txt6 = Text(root , width = 30 , height = 2)
    label3 = Label(f1, text="Enter the ID : ",background="#bf9556",fg="#002b87",relief=RAISED)
    label3.grid(row=2,column=0,pady=5)
    lis6 = Listbox(root , width = 15 , height = 2)
    textbox1 = Text(f1,width=20,height=2)
    textbox1.grid(row=2,column=1,pady=15)
    txt4 = Text(root , width = 30 , height = 2)
    btn = Button(root , width = 20 , height = 3 , background = 'red')
    textbox2 = Text(f1,width=60,height=5)
    textbox2.grid(row=3,column=0,pady=15,padx=10,sticky=W+E,columnspan=3)

    def openimage():
        ToSend = textbox1.get(1.0,END).strip('\n')
        if v1.get() == "1":
            if ToSend not in memberToGrp[curr]:
                    messagebox.showerror("Error","Invalid Group ID")
                    return
        else:
            if ToSend not in individualContacts[curr]:
                    messagebox.showerror("Error","Invalid User ID")
                    return
        f1.filename = filedialog.askopenfilename(initialdir = r'C:\Users\Dell-2\Pictures\Random' , title = 'select an image' , filetypes = (("jpg files" , "*.jpg"),))
        filepath = f1.filename
        
        if filepath != "":
            if v1.get() == "1":
                l1 = list()
                for member in grpToMembers[ToSend]:
                    if member != curr:
                        l1.append(member)
                for member in l1:
                    if member not in message:
                        message[member] = [[filepath,1]]
                    else:
                        message[member].append([filepath,1])
            else:
                if ToSend not in message:
                    message[ToSend] = [[filepath,1]]
                else:
                    message[ToSend].append([filepath,1])
            messagebox.showinfo("Info","Image Posted")
            

    def post():
        ToSend = textbox1.get(1.0,END).strip('\n')
        if v1.get() == "1":
            if ToSend not in memberToGrp[curr]:
                    messagebox.showerror("Error","Invalid Group ID")
                    return
        else:
            if ToSend not in individualContacts[curr]:
                    messagebox.showerror("Error","Invalid User ID")
                    return
        s = textbox2.get(1.0,END).strip('\n')
        textbox2.delete(1.0,END)
        ToSend = textbox1.get(1.0,END).strip('\n')
        if v1.get() == "1":
            l1 = list()
            for member in grpToMembers[ToSend]:
                if member != curr:
                    l1.append(member)
            for member in l1:
                if member not in message:
                    message[member] = [[s,0]]
                else:
                    message[member].append([s,0])
        else:
            if ToSend not in message:
                message[ToSend] = [[s,0]]
            else:
                message[ToSend].append([s,0])

    B1 = Button(f1,text="Post Text", width=12,height=1,command=post,bd=5,background="#bf9556",fg="#002b87").grid(row=4,column=0,pady=10)
    B2 = Button(f1,text="Select Image", width=16,height=1,command=openimage,bd=5,background="#bf9556",fg="#002b87").grid(row=4,column=2,pady=10)
    lab9 = Label(root , text = "label9" , width = 20 , height = 2)
    f2.grid(row=0, column=2, sticky="nsew")

    labe21 = Label(f2,text="Incoming Messages", font=50,background="#ad501d", relief=RAISED,fg="#002b87",width=20,height=2)
    labe21.pack(pady=20)
    
    text_scroll = Scrollbar(f2)
    text_scroll.pack(side = RIGHT , fill = Y)
    btn2 = Button(root , width = 20 , height = 3 , background = 'red')
    my_text = Text(f2 , width = 60 , height = 15 , font = ('Helvetics' , 10) , yscrollcommand = text_scroll.set)
    my_text.pack(pady = 10 , padx = 10)

    lab1 = Label(root , text = "label1" , width = 20 , height = 2)

    text_scroll.config(command = my_text.yview)
    global my_image
    global images
    images = []
    btn3 = Button(root , width = 20 , height = 3 , background = 'red')
    if curr in message:
        for mess in message[curr]:
            if mess[1] == 0:
                my_text.insert(END , mess[0] + '\n\n')
            else:
                my_image = Image.open(mess[0])
                my_image = my_image.resize((80,80) , Image.ANTIALIAS)
                my_image = my_image.rotate(270)
                my_image = ImageTk.PhotoImage(my_image)
                my_text.image_create(END , image = my_image)
                my_text.insert(END , '\n\n')
                images.append(my_image)


    f3.grid(row=1, column=1, sticky="nsew")
    label3 = Label(f3, text="Contacts", font=50,background="#ad501d", relief=RAISED,fg="#002b87",width=16,height=2)
    label3.pack(pady = 20)
    but_1 = Button(root , width = 20 , height = 3 , text = "check_button2")
    txt7 = Text(root , width = 30 , height = 2)
    scroll_bar31 = Scrollbar(f3)
    scroll_bar31.pack(side=RIGHT, fill=Y)
    btn4 = Button(root , width = 20 , height = 3 , background = 'red')
    txt8 = Text(root , width = 30 , height = 2)
    mylist3 = Listbox(f3, yscrollcommand=scroll_bar31.set, height=12, width=10,font=15)
    for item in individualContacts[curr]:
        mylist3.insert(END, item)
    scroll_bar31.config(command=mylist3.yview)
    lis2 = Listbox(root , width = 20 , height = 3)
    mylist3.pack(fill=BOTH,padx=15,pady=15)

    f4.grid(row=1, column=2, sticky="nsew")
    label4 = Label(f4, text="Groups", font=50,background="#ad501d", relief=RAISED,fg="#002b87",width=16,height=2)
    label4.pack(pady=20)
    lab2 = Label(root , text = "label2" , width = 20 , height = 3)
    txt_check = Text(root , width = 30 , height = 2)
    scroll_bar41 = Scrollbar(f4)
    scroll_bar41.pack(side=RIGHT, fill=Y)
    but_3 = Button(root , text = "button_3" , width = 20 , height = 3)
    txt_check1 = Text(root , width = 30 , height = 2)
    mylist4 = Listbox(f4, yscrollcommand=scroll_bar41.set, height=12, width=10,font=15)
    for item in memberToGrp[curr]:
        mylist4.insert(END, item)
    scroll_bar41.config(command=mylist4.yview)
    txt_check2 = Text(root , width = 30 , height = 2)
    btn5 = Button(root , width = 20 , height = 3 , background = 'red')
    lis = Listbox(root , width = 15 , height = 2)
    mylist4.pack(fill=BOTH,padx=15,pady=15)

    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=3)
    root.grid_columnconfigure(2, weight=3)

    root.grid_rowconfigure(0, weight=1)
    root.grid_rowconfigure(1, weight=1)

    f0.grid_propagate(0)
    f1.grid_propagate(0)
    f2.grid_propagate(0)
    f3.grid_propagate(0)
    f4.grid_propagate(0)
    f0.pack_propagate(False)
    f1.pack_propagate(False)
    f2.pack_propagate(False)
    f3.pack_propagate(False)
    f4.pack_propagate(False)

    variable.set("Select the user")
    

root.geometry("1366x768")
root.configure(bg = "#c2eda6")
root.title("Chit Chat")

imag = Image.open(r"C:\Users\Dell-2\Pictures\img1.jpeg")
imag = imag.resize((400, 400))
imag = ImageTk.PhotoImage(imag)
img_label = Label(root , image = imag).grid(row=0,column=0 ,padx=470 ,pady = 40,columnspan=2)

variable = StringVar(root)

w = OptionMenu(root, variable, *listOfUsers)
w.grid(row=1,column=0 ,pady = 10, padx=(450,0))
w.config(width = 25, height=2,bd="5",background="#bf9556",fg="#002b87")

but = Button(root , width = 20 , height = 2 , text = "check_button1")

variable.set("Select the user")
def clicked():
    global curr
    frame = 0
    curr = variable.get()
    frame = frame + 1
    if curr not in listOfUsers:
        messagebox.showerror("Error", "No user selected")
    else:
        refresh(root)


b1 = Button(root, text="Click", command=clicked,width=16,height=2,bd="5",background="#bf9556",fg="#002b87")
b1.grid(row=1,column=1, pady = 10, padx=(0,450))
btn5 = Button(root , width = 20 , height = 3 , background = 'red')
b2 = Button(root , text = "Exit" , command = root.quit, width=16,height=2,bd="5",background="#bf9556",fg="#002b87").grid(row=2,column=0, pady = (80,0),padx=550,columnspan=2)
lab4 = Label(root , width = 20 , height = 3 , text = "check_label")
root.mainloop()

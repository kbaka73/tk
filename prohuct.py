from tkinter import *
root= Tk()
root.geometry("400x300+350+100")
root.resizable(False,False)
root.title("KBAKA")



def custmars():
    root3=Tk()
    root3.geometry("800x500+150+10")
    root3.resizable(False,False)
    root3.title("KBAKA")
    f1= Frame(root3, width=800, height=50 , bg="#040D12")
    f1.place(x=0, y=0)

    tx= Label(f1,text="custmars data" , font="Roboto 18 " , bg="#040D12" , fg="#93B1A6")
    tx.place(x=330,y=10)
    f2= Frame(root3, width=800, height=400 , bg="#93B1A6")
    f2.place(x=0, y=50)


    # image = PhotoImage(file="1.png")
    # pho = Label(root ,image=image , width=300, height=300)
    # pho.place(x=10 , y=20)

    # name entery1
    name1 = Label(f2 , text="name :", font="Roboto 14 " , bg="#5C8374" , fg="#040D12",width=10)
    name1.place(x=10, y=5)
    entery = Entry(f2 ,width=20 , font="Roboto 14" )
    entery.place(x=160 , y= 5)
    # name entery2
    name1 = Label(f2 , text="city :", font="Roboto 14 " , bg="#5C8374" , fg="#040D12",width=10)
    name1.place(x=10, y=70)
    entery = Entry(f2 ,width=20 , font="Roboto 14" )
    entery.place(x=160 , y= 70)
    # name entery3
    name1 = Label(f2 , text="country :", font="Roboto 14 " , bg="#5C8374" , fg="#040D12",width=10)
    name1.place(x=10, y=140)
    entery = Entry(f2 ,width=20 , font="Roboto 14" )
    entery.place(x=160 , y= 140)
    # name entery4
    name1 = Label(f2 , text="country :", font="Roboto 14 " , bg="#5C8374" , fg="#040D12",width=10)
    name1.place(x=10, y=210)
    entery = Entry(f2 ,width=20 , font="Roboto 14" )
    entery.place(x=160 , y= 210)

    # name entery5
    name1 = Label(f2 , text="country :", font="Roboto 14 " , bg="#5C8374" , fg="#040D12",width=10)
    name1.place(x=10, y=280)
    entery = Entry(f2 ,width=20 , font="Roboto 14" )
    entery.place(x=160 , y= 280)

    # name entery6
    name1 = Label(f2 , text="country :", font="Roboto 14 " , bg="#5C8374" , fg="#040D12",width=10)
    name1.place(x=10, y=350)
    entery = Entry(f2 ,width=20 , font="Roboto 14" )
    entery.place(x=160 , y= 350)
    # frrem 3
    f3 = Frame(root3, width=800, height=50 ,bg="#5C8374")
    f3.place(x=0, y=450)
    bt1 = Button(f3, text="Add" , font="Roboto 12" ,width=10, bg="#93B1A6")
    bt1.place(x=10, y=7)

    bt2 = Button(f3, text="Edit" , font="Roboto 12" ,width=10, bg="#93B1A6")
    bt2.place(x=130, y=7)

    bt3 = Button(f3, text="Delet" , font="Roboto 12" ,width=10, bg="#93B1A6")
    bt3.place(x=260, y=7)


    bt6 = Button(f3, text="Back" ,command=root3.destroy, font="Roboto 12" ,width=10, bg="red")
    bt6.place(x=690, y=7)


def employess():
    root3=Tk()
    root3.geometry("800x500+150+10")
    root3.resizable(False,False)
    root3.title("KBAKA")
    f1= Frame(root3, width=800, height=50 , bg="#040D12")
    f1.place(x=0, y=0)

    tx= Label(f1,text="employess data" , font="Roboto 18 " , bg="#040D12" , fg="#93B1A6")
    tx.place(x=330,y=10)
    f2= Frame(root3, width=800, height=400 , bg="#93B1A6")
    f2.place(x=0, y=50)

    check = Label(f2 , text="Gnert" , font="Roboto 14 " , bg="#5C8374" , fg="#040D12",width=10)
    check.place(x=550,y=100)
    name1chack= Checkbutton(f2, text='en' ,font="Roboto 14 " , bg="#5C8374" , fg="#040D12",width=5)
    name1chack.place(x=500 , y=150)
    name2chack= Checkbutton(f2, text='ar' ,font="Roboto 14 " , bg="#5C8374" , fg="#040D12",width=5)
    name2chack.place(x=630 , y=150)

    # image = PhotoImage(file="1.png")
    # pho = Label(root ,image=image , width=300, height=300)
    # pho.place(x=10 , y=20)

    # name entery1
    name1 = Label(f2 , text="name :", font="Roboto 14 " , bg="#5C8374" , fg="#040D12",width=10)
    name1.place(x=10, y=5)
    entery = Entry(f2 ,width=20 , font="Roboto 14" )
    entery.place(x=160 , y= 5)
    # name entery2
    name1 = Label(f2 , text="city :", font="Roboto 14 " , bg="#5C8374" , fg="#040D12",width=10)
    name1.place(x=10, y=70)
    entery = Entry(f2 ,width=20 , font="Roboto 14" )
    entery.place(x=160 , y= 70)
    # name entery3
    name1 = Label(f2 , text="country :", font="Roboto 14 " , bg="#5C8374" , fg="#040D12",width=10)
    name1.place(x=10, y=140)
    entery = Entry(f2 ,width=20 , font="Roboto 14" )
    entery.place(x=160 , y= 140)
    # name entery4
    name1 = Label(f2 , text="country :", font="Roboto 14 " , bg="#5C8374" , fg="#040D12",width=10)
    name1.place(x=10, y=210)
    entery = Entry(f2 ,width=20 , font="Roboto 14" )
    entery.place(x=160 , y= 210)

    # name entery5
    name1 = Label(f2 , text="country :", font="Roboto 14 " , bg="#5C8374" , fg="#040D12",width=10)
    name1.place(x=10, y=280)
    entery = Entry(f2 ,width=20 , font="Roboto 14" )
    entery.place(x=160 , y= 280)

    # name entery6
    name1 = Label(f2 , text="country :", font="Roboto 14 " , bg="#5C8374" , fg="#040D12",width=10)
    name1.place(x=10, y=350)
    entery = Entry(f2 ,width=20 , font="Roboto 14" )
    entery.place(x=160 , y= 350)
    # frrem 3
    f3 = Frame(root3, width=800, height=50 ,bg="#5C8374")
    f3.place(x=0, y=450)
    bt1 = Button(f3, text="Add" , font="Roboto 12" ,width=10, bg="#93B1A6")
    bt1.place(x=10, y=7)

    bt2 = Button(f3, text="Edit" , font="Roboto 12" ,width=10, bg="#93B1A6")
    bt2.place(x=130, y=7)

    bt3 = Button(f3, text="Delet" , font="Roboto 12" ,width=10, bg="#93B1A6")
    bt3.place(x=260, y=7)


    bt6 = Button(f3, text="Back" ,command=root3.destroy, font="Roboto 12" ,width=10, bg="red")
    bt6.place(x=690, y=7)

def items():
    root3=Tk()
    root3.geometry("800x500+150+10")
    root3.resizable(False,False)
    root3.title("KBAKA")
    f1= Frame(root3, width=800, height=50 , bg="#040D12")
    f1.place(x=0, y=0)

    tx= Label(f1,text="Item data" , font="Roboto 18 " , bg="#040D12" , fg="#93B1A6")
    tx.place(x=330,y=10)
    f2= Frame(root3, width=800, height=400 , bg="#93B1A6")
    f2.place(x=0, y=50)

    # image = PhotoImage(file="1.png")
    # pho = Label(root ,image=image , width=300, height=300)
    # pho.place(x=10 , y=20)

    # name entery1
    name1 = Label(f2 , text="name :", font="Roboto 14 " , bg="#5C8374" , fg="#040D12",width=10)
    name1.place(x=10, y=5)
    entery = Entry(f2 ,width=20 , font="Roboto 14" )
    entery.place(x=160 , y= 5)
    # name entery2
    name1 = Label(f2 , text="cuntry :", font="Roboto 14 " , bg="#5C8374" , fg="#040D12",width=10)
    name1.place(x=10, y=70)
    entery = Entry(f2 ,width=20 , font="Roboto 14" )
    entery.place(x=160 , y= 70)
    # name entery3
    name1 = Label(f2 , text="prise :", font="Roboto 14 " , bg="#5C8374" , fg="#040D12",width=10)
    name1.place(x=10, y=140)
    entery = Entry(f2 ,width=20 , font="Roboto 14" )
    entery.place(x=160 , y= 140)
    # name entery4
    name1 = Label(f2 , text="quantity :", font="Roboto 14 " , bg="#5C8374" , fg="#040D12",width=10)
    name1.place(x=10, y=210)
    entery = Entry(f2 ,width=20 , font="Roboto 14" )
    entery.place(x=160 , y= 210)

    # name entery5
    name1 = Label(f2 , text="description :", font="Roboto 14 " , bg="#5C8374" , fg="#040D12",width=10)
    name1.place(x=10, y=280)
    entery = Entry(f2 ,width=20 , font="Roboto 14" )
    entery.place(x=160 , y= 280)

    # name entery6

    # frrem 3
    f3 = Frame(root3, width=800, height=50 ,bg="#5C8374")
    f3.place(x=0, y=450)
    bt1 = Button(f3, text="New" , font="Roboto 12" ,width=10, bg="#93B1A6")
    bt1.place(x=10, y=7)

    bt2 = Button(f3, text="Delet" , font="Roboto 12" ,width=10, bg="#93B1A6")
    bt2.place(x=130, y=7)

    bt3 = Button(f3, text="Find" , font="Roboto 12" ,width=10, bg="#93B1A6")
    bt3.place(x=260, y=7)


    bt6 = Button(f3, text="Back" ,command=root3.destroy, font="Roboto 12" ,width=10, bg="red")
    bt6.place(x=690, y=7)

def queries():
    root3=Tk()
    root3.geometry("800x500+150+10")
    root3.resizable(False,False)
    root3.title("KBAKA")
    f1= Frame(root3, width=800, height=50 , bg="#040D12")
    f1.place(x=0, y=0)

    tx= Label(f1,text="queries data" , font="Roboto 18 " , bg="#040D12" , fg="#93B1A6")
    tx.place(x=330,y=10)
    f2= Frame(root3, width=800, height=400 , bg="#93B1A6")
    f2.place(x=0, y=50)

    # frrem 3
    f3 = Frame(root3, width=800, height=50 ,bg="#5C8374")
    f3.place(x=0, y=450)
    bt1 = Button(f3, text="Add" , font="Roboto 12" ,width=10, bg="#93B1A6")
    bt1.place(x=10, y=7)

    bt2 = Button(f3, text="Edit" , font="Roboto 12" ,width=10, bg="#93B1A6")
    bt2.place(x=130, y=7)

    bt3 = Button(f3, text="Delet" , font="Roboto 12" ,width=10, bg="#93B1A6")
    bt3.place(x=260, y=7)


    bt6 = Button(f3, text="Back" ,command=root3.destroy, font="Roboto 12" ,width=10, bg="red")
    bt6.place(x=690, y=7)

def start():
    root2= Tk()
    root2.geometry("800x500+150+10")
    root2.resizable(False,False)
    root2.title("KBAKA")
    h2= Label(root2 , text="MAIN SCREN" ,fg="#93B1A6" , bg="#040D12", bd=10 ,  font="Roboto 24")
    h2.pack()

    Btn11 = Button(root2,command=custmars ,text="Custmars" , bg="#93B1A6" , fg="#040D12" , font="Roboto  14", width=10 ,relief="groove", bd=2, padx=10, pady=10)
    Btn11.place(x=240, y=100)

    Btn12 = Button(root2, text="vedores" , bg="#93B1A6" , fg="#040D12" , font="Roboto  14", width=10 ,relief="groove", bd=2, padx=10, pady=10)
    Btn12.place(x=450, y=100)

    Btn13 = Button(root2, text="Items",command=items , bg="#93B1A6" , fg="#040D12" , font="Roboto  14",width=10, relief="groove", bd=2, padx=10, pady=10)
    Btn13.place(x=240, y=200)

    Btn14 = Button(root2, text="Employess" ,command=employess ,bg="#93B1A6" , fg="#040D12" , font="Roboto  14",width=10, relief="groove", bd=2, padx=10, pady=10)
    Btn14.place(x=450, y=200)

    Btn15 = Button(root2, text="Rqueries" ,command=queries ,bg="#93B1A6" , fg="#040D12" , font="Roboto  14", width=10,relief="groove", bd=2, padx=10, pady=10)
    Btn15.place(x=240, y=300)

    Btn16 = Button(root2, text="Back" , bg="red" , fg="#040D12" , font="Roboto  14", width=10,relief="groove", bd=2, padx=10, pady=10 , command=root2.destroy)
    Btn16.place(x=450, y=300)
    Btn16 = Button(root2, text="Back" , bg="red" , fg="#040D12" , font="Roboto  14", width=10,relief="groove", bd=2, padx=10, pady=10 , command=root2.destroy)
    Btn16.place(x=450, y=300)





    root2.mainloop()

    


# home
h1 = Label(root, text="4U Grobe" , font="Roboto 24",fg="#040D12")
h1.pack()
btn = Button(root, text="Exit" , bg="#183D3D" ,fg="#040D12", width=10, font=24,command=root.destroy)
btn.place(x=50, y=140)
btn1 = Button(root, text="Start" , bg="#183D3D" ,fg="#040D12", width=10, font=24, command=start)
btn1.place(x=230, y=140)


































root.mainloop()
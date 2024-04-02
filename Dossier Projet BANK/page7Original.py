from tkinter import *
from customtkinter import *
from PIL import Image,ImageTk
from datetime import datetime
import locale


#met la localisatin suivant la france → permet davoir la langue française pour la date
locale.setlocale(locale.LC_TIME, 'fr_FR.UTF-8')


root = Tk()
root.title('AMAN')
root.iconbitmap('image/AMAN-LOGO.ico')
root.geometry("800x480")
root.minsize(800, 480)
root.maxsize(800, 480)
root.config(bg='#F2F7F9')

#bande bleu  TOP
frm1 = Frame(root, bg='#1679EF', height=50)
frm1.pack(fill=X, side=TOP,pady=15)

#logo
old_image_frm1 = Image.open('image/AMAN-BLEU.png')  
resized_frm1 = old_image_frm1.resize((60, 50), Image.LANCZOS)     
new_image_frm1 = ImageTk.PhotoImage(resized_frm1)   
label1 = Label(frm1, image=new_image_frm1,highlightthickness=0,bd=0)
label1.pack(expand=YES)

#Partie central (contenu)

frm2 = Frame(root,bg='#F2F7F9',height=360,width=800)

frm_box = Frame(root,bg='#F2F7F9',height=300,width=300)
frm_box.place(x=480,y=120)

box1 = CTkButton(master=frm_box,text='A1',text_color='#1679EF',fg_color='#F2F7F9',height=60,width=60,corner_radius=4,border_width=2,border_color='#1679EF',hover=None)
box1.grid(row=0,column=0,padx=0.5,pady=0.5)

box2 = CTkButton(master=frm_box,text='A2',text_color='#1679EF',fg_color='#F2F7F9',height=60,width=60,corner_radius=4,border_width=2,border_color='#1679EF',hover=None)
box2.grid(row=0,column=1,padx=0.5,pady=0.5)

box3 = CTkButton(master=frm_box,text='A3',text_color='#1679EF',fg_color='#F2F7F9',height=60,width=60,corner_radius=4,border_width=2,border_color='#1679EF',hover=None)
box3.grid(row=0,column=2,padx=0.5,pady=0.5)

box4 = CTkButton(master=frm_box,text='A4',text_color='#1679EF',fg_color='#F2F7F9',height=60,width=60,corner_radius=4,border_width=2,border_color='#1679EF',hover=None)
box4.grid(row=0,column=3,padx=0.5,pady=0.5)

box5 = CTkButton(master=frm_box,text='B1',text_color='#1679EF',fg_color='#F2F7F9',height=80,width=60,corner_radius=4,border_width=2,border_color='#1679EF',hover=None)
box5.grid(row=1,column=0,padx=0.5,pady=0.5)

box6 = CTkButton(master=frm_box,text='B2',text_color='#1679EF',fg_color='#F2F7F9',height=80,width=60,corner_radius=4,border_width=2,border_color='#1679EF',hover=None)
box6.grid(row=1,column=1,padx=0.5,pady=0.5)

box7 = CTkButton(master=frm_box,text='B3',text_color='#1679EF',fg_color='#F2F7F9',height=80,width=60,corner_radius=4,border_width=2,border_color='#1679EF',hover=None)
box7.grid(row=1,column=2,padx=0.5,pady=0.5)

box8 = CTkButton(master=frm_box,text='B4',text_color='#1679EF',fg_color='#F2F7F9',height=80,width=60,corner_radius=4,border_width=2,border_color='#1679EF',hover=None)
box8.grid(row=1,column=3,padx=0.5,pady=0.5)

box9 = CTkButton(master=frm_box,text='A5',text_color='#1679EF',fg_color='#F2F7F9',height=60,width=60,corner_radius=4,border_width=2,border_color='#1679EF',hover=None)
box9.grid(row=2,column=0,padx=0.5,pady=0.5)
box10 = CTkButton(master=frm_box,text='A6',text_color='#1679EF',fg_color='#F2F7F9',height=60,width=60,corner_radius=4,border_width=2,border_color='#1679EF',hover=None)
box10.grid(row=3,column=0,padx=0.5,pady=0.5)

box11 = CTkButton(master=frm_box,text='C1',text_color='#1679EF',fg_color='#F2F7F9',height=120,width=60,corner_radius=4,border_width=2,border_color='#1679EF',hover=None)
box11.grid(row=2,column=1,padx=0.5,pady=0.5,rowspan=2)

box12 = CTkButton(master=frm_box,text='C2',text_color='#1679EF',fg_color='#F2F7F9',height=120,width=60,corner_radius=4,border_width=2,border_color='#1679EF',hover=None)
box12.grid(row=2,column=2,padx=0.5,pady=0.5,rowspan=2)

box13 = CTkButton(master=frm_box,text='C3',text_color='#1679EF',fg_color='#F2F7F9',height=120,width=60,corner_radius=4,border_width=2,border_color='#1679EF',hover=None)
box13.grid(row=2,column=3,padx=0.5,pady=0.5,rowspan=2)



frm_msg = CTkFrame(master=frm2,fg_color='#F2F7F9')

label_msg = CTkLabel(master=frm_msg,text='Votre montant total à régler',font=('Arial',25),fg_color='#F2F7F9',text_color='#1679EF')
label_msg.grid(row=0,column=0,pady=30)

#case prix
label_msg = CTkLabel(master=frm_msg,text='400 DA',font=('Arial',40),fg_color='#1679EF',text_color='#F2F7F9',corner_radius=4,height=70,width=200,)
label_msg.grid(row=1,column=0)

#image fleche
img_flch = Image.open('fr/image/flech_bas.png')
img_flch_final = ImageTk.PhotoImage(img_flch)

label_flch = CTkLabel(master=frm2,fg_color='#1679EF',image=img_flch_final,text=None)
label_flch.place(x=10,y=105)

frm_msg.place(x=120,y=50)








frm2.pack()







#bande bleu BOTTOM
frm3 = Frame(root, bg='#1679EF', height=30)
date=datetime.now()
label2 = Label(frm3,text=f"{date:%d-%m-%Y}  /  {date:%I:%M}",font=('Arial',12),fg='#F2F7F9',bg='#1679EF')
label2.pack(expand=YES)

frm3.pack(fill=X, side=BOTTOM)

root.mainloop()
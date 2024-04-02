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


frm2.pack()














lbl_msg = CTkLabel(master=frm2,text='veuillez retirer vos bagages',font=('Arial',40,"bold"),text_color='#095CD3',fg_color='#F2F7F9')
lbl_msg.pack(expand=YES,pady=70)

bouton = CTkButton(master=frm2,text='Confimer',font=('Arial',30),text_color='#F2F7F9',fg_color='#1679EF',height=60,width=200,corner_radius=4)
bouton.pack(expand=YES,pady=10)










frm3 = Frame(root, bg='#1679EF', height=30)
date=datetime.now()
label2 = Label(frm3,text=f"{date:%d-%m-%Y}  /  {date:%I:%M}",font=('Arial',12),fg='#F2F7F9',bg='#1679EF')
label2.pack(expand=YES)

frm3.pack(fill=X, side=BOTTOM)

root.mainloop()
from tkinter import *
from customtkinter import *
from PIL import Image,ImageTk
from datetime import datetime
import locale


#met la localisatin suivant la france      permet davoir la langue française pour la date
locale.setlocale(locale.LC_TIME, 'fr_FR.UTF-8')


root = Tk()
root.title('langue')
root.iconbitmap('image/AMAN-LOGO.ico')
root.geometry("800x480")
root.minsize(800, 480)
root.maxsize(800, 480)
root.config(bg='#F2F7F9')

frm1 = Frame(root, bg='#1679EF', height=50)
frm1.pack(fill=X, side=TOP,pady=15)

    
old_image_frm1 = Image.open('image/AMAN-BLEU.png') # importe l'image image   
resized_frm1 = old_image_frm1.resize((60, 50), Image.LANCZOS)  # redimentioner l'image    
new_image_frm1 = ImageTk.PhotoImage(resized_frm1)   # image  final    ---------- si tu veux faire des modifs cest cette Var que tu va utiliser
label1 = Label(frm1, image=new_image_frm1,highlightthickness=0,bd=0)#afficher l'image(image rahi f label)
label1.pack(expand=YES)







image  = Image.open('image/fleche3.png')
img = ImageTk.PhotoImage(image)


frm2= Frame(root,bg='#F2F7F9',width=800,height=360)

bouton1 = CTkButton(master=frm2,
                 text='Français',
                 fg_color='#1679EF',
                 text_color='#F2F7F9',
                 font=(('Arial'),28),
                 width=170,
                 height=50,
                 border_width=0,
                 corner_radius=4)
bouton1.place(x=565,y=65)

label1 = Label(frm2,image=img,bg='#F2F7F9')
label1.place(x=735,y=59)


bouton2 = CTkButton(master=frm2,
                 text='العربية',
                 fg_color='#1679EF',
                 text_color='#F2F7F9',
                 font=(('Arial'),28),
                 width=170,
                 height=50,
                 border_width=0,
                 corner_radius=4)
bouton2.place(x=565,y=160)
label2 = Label(frm2,image=img,bg='#F2F7F9')
label2.place(x=735,y=154)



bouton3 = CTkButton(master=frm2,
                 text='Sortie  خروج ',
                 fg_color='#1679EF',
                 text_color='#F2F7F9',
                 font=(('Arial'),28),
                 width=170,
                 height=50,
                 border_width=0,
                 corner_radius=4)
bouton3.place(x=565,y=260)
label3 = Label(frm2,image=img,bg='#F2F7F9')
label3.place(x=735,y=254)



label = Label(frm2,text="S'il vous plaît, choisissez votre langue \n\n من فضلك، اختر لغتك ", bg='#F2F7F9',fg='#095CD3',font=('Arial',21,'bold'))
label.place(x=30,y=80)
frm2.pack()


frm3 = Frame(root, bg='#1679EF', height=30)
date=datetime.now()
label2 = Label(frm3,text=f"{date:%d-%m-%Y}  /  {date:%I:%M}",font=('Arial',12),fg='#F2F7F9',bg='#1679EF')
label2.pack(expand=YES)

frm3.pack(fill=X, side=BOTTOM)
root.mainloop()
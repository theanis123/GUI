from tkinter import *
from customtkinter import *
from PIL import Image,ImageTk
from datetime import datetime
import locale


#met la localisatin suivant la france → permet davoir la langue française pour la date
locale.setlocale(locale.LC_TIME, 'fr_FR.UTF-8')

#initialisation fenetre
root = Tk()
root.title('AMAN')
root.iconbitmap('image/AMAN-LOGO.ico')
root.geometry("800x480")
root.minsize(800, 480)
root.maxsize(800, 480)
root.config(bg='#F2F7F9')

#bande bleu TOP
frm1 = Frame(root, bg='#1679EF', height=50)
frm1.pack(fill=X, side=TOP,pady=15)

#logo AMAN TOP
old_image_frm1 = Image.open('image/AMAN-BLEU.png') 
resized_frm1 = old_image_frm1.resize((60, 50), Image.LANCZOS)   
new_image_frm1 = ImageTk.PhotoImage(resized_frm1)  
label1 = Label(frm1, image=new_image_frm1,highlightthickness=0,bd=0)
label1.pack(expand=YES)


#partie central (contenu)
frm2 = Frame(root,bg='#F2F7F9',height=360,width=800)

#message haut
label_msg = Label(frm2,text="Merci de bien vouloir choisir parmi\n les options suivantes en sélectionnant votre préférence",font=('Arial',18,"bold"),fg='#095CD3',bg='#F2F7F9')
label_msg.place(x=60,y=10)

#partie bouton 

btn1 = CTkButton(master=frm2,
                 text='Dépôt',
                 font=('Arial',27),
                 fg_color='#1679EF',
                 text_color='#F2F7F9',
                 width=350,
                 height=50,
                 border_width=0,
                 corner_radius=4)
btn1.place(x=385,y=130)

btn2 = CTkButton(master=frm2,
              text='Retrait',
              font=('Arial',27),
              fg_color='#1679EF',
              text_color='#F2F7F9',
              width=350,
              height=50,
              border_width=0,
              corner_radius=4)
btn2.place(x=385,y=230)


#partie flech
image_flch  = Image.open('image/fleche3.png')
img_flch = ImageTk.PhotoImage(image_flch)

label_flch = Label(frm2,image=img_flch,bg='#F2F7F9')
label_flch.place(x=735,y=224)


label_flch2 = Label(frm2,image=img_flch,bg='#F2F7F9')
label_flch2.place(x=735,y=123)


#bouton sortie
btn_srt = CTkButton(master=frm2,
                    text='Sortie',
                    font=('Arial',20),
                    fg_color='#1679EF',
                    text_color='#F2F7F9',
                    width=100,
                    height=30,
                    border_width=0,
                    corner_radius=3)
btn_srt.place(x=40,y=320)

#fleche pour bouton sortie
rotated_img = image_flch.rotate(180)
resize = rotated_img.resize((35,35),Image.LANCZOS)
img_flch_srt = ImageTk.PhotoImage(resize)
label_flch_srt = Label(frm2,image=img_flch_srt,bg='#F2F7F9')
label_flch_srt.place(x=1,y=316)


frm2.pack()


#bande blue BOTTOM
frm3 = Frame(root, bg='#1679EF', height=30)
date=datetime.now()
label2 = Label(frm3,text=f"{date:%d-%m-%Y}  /  {date:%I:%M}",font=('Arial',12),fg='#F2F7F9',bg='#1679EF')
label2.pack(expand=YES)

frm3.pack(fill=X, side=BOTTOM)

root.mainloop()
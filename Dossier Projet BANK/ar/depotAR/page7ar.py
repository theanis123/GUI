from tkinter import *
from customtkinter import *
from PIL import Image,ImageTk
from datetime import datetime
import locale
import arabic_reshaper
import bidi.algorithm


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
frm_box.place(x=600,y=100)

box1 = CTkButton(master=frm_box,text='A',text_color='#1679EF',fg_color='#F2F7F9',height=80,width=90,corner_radius=4,border_width=2,border_color='#1679EF',hover=None)
box1.grid(row=0,column=0,padx=0.5,pady=0.5)

box5 = CTkButton(master=frm_box,text='B',text_color='#1679EF',fg_color='#F2F7F9',height=100,width=90,corner_radius=4,border_width=2,border_color='#1679EF',hover=None)
box5.grid(row=1,column=0,padx=0.5,pady=0.5)

box13 = CTkButton(master=frm_box,text='C',text_color='#1679EF',fg_color='#F2F7F9',height=140,width=90,corner_radius=4,border_width=2,border_color='#1679EF',hover=None)
box13.grid(row=2,column=0,padx=0.5,pady=0.5,rowspan=2)



frm_msg = CTkFrame(master=frm2,fg_color='#F2F7F9')

label_msg = CTkLabel(master=frm_msg,text='المبلغ الإجمالي الذي عليك دفعه',font=('Arial',30,"bold"),fg_color='#F2F7F9',text_color='#095CD3')
label_msg.grid(row=0,column=0,pady=30)

#case prix
reshaped_text = arabic_reshaper.reshape( '400 دج')
text  = bidi.algorithm.get_display(reshaped_text)
label_msg = CTkLabel(master=frm_msg,text=text,font=('Arial',40),fg_color='#1679EF',text_color='#F2F7F9',corner_radius=4,height=70,width=200,)
label_msg.grid(row=1,column=0)

#image fleche
img_flch = Image.open('fr/image/flech_bas.png')
img_flch_final = ImageTk.PhotoImage(img_flch)

label_flch = CTkLabel(master=frm2,fg_color='#1679EF',image=img_flch_final,text=None)
label_flch.place(x=120,y=105)

frm_msg.place(x=220,y=50)








frm2.pack()







btn_srt = CTkButton(master=frm2,
                    text='خروج',
                    font=('Arial',20),
                    fg_color='#1679EF',
                    text_color='#F2F7F9',
                    width=100,
                    height=30,
                    border_width=0,
                    corner_radius=3)
btn_srt.place(x=40,y=320)


image_flch_srt  = Image.open('image/fleche3.png')
rotated_img = image_flch_srt.rotate(180)
resize = rotated_img.resize((35,35),Image.LANCZOS)
img_flch_srt = ImageTk.PhotoImage(resize)
label_flch_srt = Label(frm2,image=img_flch_srt,bg='#F2F7F9')
label_flch_srt.place(x=1,y=316)




frm3 = Frame(root, bg='#1679EF', height=30)
date=datetime.now()
label2 = Label(frm3,text=f"{date:%d-%m-%Y}  /  {date:%I:%M}",font=('Arial',12),fg='#F2F7F9',bg='#1679EF')
label2.pack(expand=YES)

frm3.pack(fill=X, side=BOTTOM)

root.mainloop()
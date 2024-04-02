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

lbl_msg = CTkLabel(master=frm2,text='يرجى ملء المعلومات التالية',font=('Arial',30,"bold"),text_color='#095CD3',fg_color='#F2F7F9')
lbl_msg.place(x = 280 , y=30)

frm_info = CTkFrame(master=frm2,fg_color='#F2F7F9')
lbl1 = CTkLabel(master=frm_info,text="إسم المستخدم",font=('Arial',22,"bold"),fg_color='#F2F7F9',text_color='#1679EF')
lbl1.grid(row=0,column=1,padx=10,pady=15,sticky='e')

lbl2 = CTkLabel(master=frm_info,text="كلمة السر",font=('Arial',22,"bold"),fg_color='#F2F7F9',text_color='#1679EF')
lbl2.grid(row=1,column=1,padx=10,pady=15,sticky='e')



entry1 = CTkEntry(master=frm_info,fg_color='#F2F7F9',text_color='black',font=('Arial',20),border_color='#1679EF',border_width=2.5,width=200)
entry1.grid(row=0,column=0,padx=10,pady=15)

entry2 = CTkEntry(master=frm_info,fg_color='#F2F7F9',text_color='black',font=('Arial',20),border_color='#1679EF',border_width=2.5,width=200)
entry2.grid(row=1,column=0,padx=10,pady=15)



frm_info.place(x=430,y=100)

frm_btn = CTkFrame(master=frm2,fg_color='#F2F7F9')
bouton = CTkButton(master=frm_btn,text='دخول',font=('Arial',25),text_color='#F2F7F9',fg_color='#1679EF',height=45,width=200,corner_radius=4)
bouton.grid(row=0,column=0,padx=10)

img_flch = Image.open('image/fleche10.png')
flch_img = ImageTk.PhotoImage(img_flch)
lbl_flch = CTkLabel(master=frm_btn,fg_color='#F2F7F9',image=flch_img,text="")
lbl_flch.grid(row=0,column=1)

frm_btn.place(x=533,y=280)





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
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

frm_info = CTkButton(master=frm2,fg_color='#F2F7F9',border_width=3,border_color='#1679EF',corner_radius=4,height=200,width=350,hover=NONE,text="")

reshaped_tex1 = arabic_reshaper.reshape( 'رقم التذكرة' + ' :')
tex1  = bidi.algorithm.get_display(reshaped_tex1)
label_ticket = CTkLabel(master=frm_info,text=tex1,font=('Arial',17,"bold"),fg_color='#F2F7F9',text_color='#1679EF')
label_ticket.grid(row=0,column=1,sticky="e")


reshaped_text2 = arabic_reshaper.reshape( "إسم المستخدم :")
text2  = bidi.algorithm.get_display(reshaped_text2)
label_nom = CTkLabel(master=frm_info,text=text2,font=('Arial',17,"bold"),fg_color='#F2F7F9',text_color='#1679EF')
label_nom.grid(row=1,column=1,sticky="e")

reshaped_text3 = arabic_reshaper.reshape( 'كلمة السر :')
text3  = bidi.algorithm.get_display(reshaped_text3)
label_mdp = CTkLabel(master=frm_info,text=text3,font=('Arial',17,"bold"),fg_color='#F2F7F9',text_color='#1679EF')
label_mdp.grid(row=2,column=1,sticky="e")

reshaped_text4 = arabic_reshaper.reshape( 'رقم الصندوق :')
text4  = bidi.algorithm.get_display(reshaped_text4)
label_coffre = CTkLabel(master=frm_info,text=text4,font=('Arial',17,"bold"),fg_color='#F2F7F9',text_color='#1679EF')
label_coffre.grid(row=3,column=1,sticky="e")

reshaped_text5 = arabic_reshaper.reshape( 'المبلغ الإجمالي :')
text5  = bidi.algorithm.get_display(reshaped_text5)
label_montant = CTkLabel(master=frm_info,text=text5,font=('Arial',17,"bold"),fg_color='#F2F7F9',text_color='#1679EF')
label_montant.grid(row=4,column=1,sticky="e")

#la partie à remplire(que tu peux modifier)
label_date = CTkLabel(master=frm_info,text="1111111111",font=('Arial',17,"bold"),fg_color='#F2F7F9',text_color='#1679EF')
label_date.grid(row=0,column=0,padx=40)

label1 = CTkLabel(master=frm_info,text="user name",font=('Arial',17,"bold"),fg_color='#F2F7F9',text_color='#1679EF')
label1.grid(row=1,column=0,padx=40)

label2 = CTkLabel(master=frm_info,text="password",font=('Arial',17,"bold"),fg_color='#F2F7F9',text_color='#1679EF')
label2.grid(row=2,column=0,padx=40)

label3 = CTkLabel(master=frm_info,text="nb box",font=('Arial',17,"bold"),fg_color='#F2F7F9',text_color='#1679EF')
label3.grid(row=3,column=0,padx=40)

label4 = CTkLabel(master=frm_info,text="price",font=('Arial',17,"bold"),fg_color='#F2F7F9',text_color='#1679EF')
label4.grid(row=4,column=0,padx=40)

frm_info.place(x= 230, y=0)



lbl_msg =  CTkLabel(master=frm2,text='الرجاء إغلاق الباب',font=('Arial',45,"bold"),fg_color='#F2F7F9',text_color='#095CD3')
lbl_msg.place(x=265,y=230)



frm2.pack()










btn_srt = CTkButton(master=frm2,
                    text='انهاء',
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
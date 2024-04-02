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

label_msg = Label(frm2,text="الرجاء تحديد مدة التخزين المطلوبة",font=('Arial',22,"bold"),fg='#095CD3',bg='#F2F7F9')
label_msg.place(x=245,y=3)



# partie bouton
        #bouton droit
reshaped_text1 = arabic_reshaper.reshape( '1 ساعة / 100 دج')
text1  = bidi.algorithm.get_display(reshaped_text1)
btn1 = CTkButton(master=frm2,
                 text=text1,
                 font=('Arial',26),
                 fg_color='#1679EF',
                 text_color='#F2F7F9',
                 width=260,
                 height=45,
                 border_width=0,
                 corner_radius=4)
btn1.place(x=475,y=60)


reshaped_text2 = arabic_reshaper.reshape( '2 ساعات / 200 دج')
text2  = bidi.algorithm.get_display(reshaped_text2)
btn2 = CTkButton(master=frm2,
                 text=text2,
                 font=('Arial',26),
                 fg_color='#1679EF',
                 text_color='#F2F7F9',
                 width=260,
                 height=45,
                 border_width=0,
                 corner_radius=4)
btn2.place(x=475,y=140)


reshaped_text3 = arabic_reshaper.reshape( '3 ساعات / 300 دج')
text3  = bidi.algorithm.get_display(reshaped_text3)
btn3 = CTkButton(master=frm2,
                 text=text3,
                 font=('Arial',26),
                 fg_color='#1679EF',
                 text_color='#F2F7F9',
                 width=260,
                 height=45,
                 border_width=0,
                 corner_radius=4)
btn3.place(x=475,y=220)


reshaped_text4 = arabic_reshaper.reshape( '4 ساعات / 400 دج')
text4  = bidi.algorithm.get_display(reshaped_text4)
btn4 = CTkButton(master=frm2,
                 text=text4,
                 font=('Arial',26),
                 fg_color='#1679EF',
                 text_color='#F2F7F9',
                 width=260,
                 height=45,
                 border_width=0,
                 corner_radius=4)
btn4.place(x=475,y=300)

    #bouton gauche
reshaped_text5 = arabic_reshaper.reshape( '12 ساعة / 1200 دج')
text5  = bidi.algorithm.get_display(reshaped_text5)
btn5 = CTkButton(master=frm2,
                 text=text5,
                 font=('Arial',26),
                 fg_color='#1679EF',
                 text_color='#F2F7F9',
                 width=260,
                 height=45,
                 border_width=0,
                 corner_radius=4)
btn5.place(x=66,y=60)


reshaped_text6 = arabic_reshaper.reshape( '24 ساعة / 2400 دج')
text6  = bidi.algorithm.get_display(reshaped_text6)
btn6 = CTkButton(master=frm2,
                 text=text6,
                 font=('Arial',26),
                 fg_color='#1679EF',
                 text_color='#F2F7F9',
                 width=260,
                 height=45,
                 border_width=0,
                 corner_radius=4)
btn6.place(x=66,y=140)



reshaped_text7 = arabic_reshaper.reshape( '48 ساعة / 4000 دج')
text7  = bidi.algorithm.get_display(reshaped_text7)
btn7 = CTkButton(master=frm2,
                 text=text7,
                 font=('Arial',26),
                 fg_color='#1679EF',
                 text_color='#F2F7F9',
                 width=260,
                 height=45,
                 border_width=0,
                 corner_radius=4)
btn7.place(x=66,y=220)

btn8 = CTkButton(master=frm2,
                 text='خروج',
                 font=('Arial',26),
                 fg_color='#1679EF',
                 text_color='#F2F7F9',
                 width=260,
                 height=45,
                 border_width=0,
                 corner_radius=4)
btn8.place(x=66,y=300)


#partie flech droite
image_flch  = Image.open('image/fleche10.png')
img_flch = ImageTk.PhotoImage(image_flch)

label_flch1 = Label(frm2,image=img_flch,bg='#F2F7F9')
label_flch1.place(x=750,y=63)


label_flch2 = Label(frm2,image=img_flch,bg='#F2F7F9')
label_flch2.place(x=750,y=144)


label_flch3 = Label(frm2,image=img_flch,bg='#F2F7F9')
label_flch3.place(x=750,y=224)


label_flch4 = Label(frm2,image=img_flch,bg='#F2F7F9')
label_flch4.place(x=750,y=305)


#rotated image
image_old = Image.open('image/fleche10.png')
image_rota = image_old.rotate(180)
image_final =  ImageTk.PhotoImage(image_rota)


#partie fleche gauche
label_flch5 = Label(frm2,image=image_final,bg='#F2F7F9')
label_flch5.place(x=9,y=63)

label_flch6 = Label(frm2,image=image_final,bg='#F2F7F9')
label_flch6.place(x=9,y=144)

label_flch7 = Label(frm2,image=image_final,bg='#F2F7F9')
label_flch7.place(x=9,y=224)

label_flch8 = Label(frm2,image=image_final,bg='#F2F7F9')
label_flch8.place(x=9,y=305)



frm2.pack()




#bande bleu BOTTOM
frm3 = Frame(root, bg='#1679EF', height=30)
date=datetime.now()
label2 = Label(frm3,text=f"{date:%d-%m-%Y}  /  {date:%I:%M}",font=('Arial',12),fg='#F2F7F9',bg='#1679EF')
label2.pack(expand=YES)

frm3.pack(fill=X, side=BOTTOM)

root.mainloop()
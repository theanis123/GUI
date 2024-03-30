from tkinter import *
from PIL import Image,ImageTk
from datetime import datetime
import locale


#met la localisatin suivant la france      permet davoir la langue française pour la date
locale.setlocale(locale.LC_TIME, 'fr_FR.UTF-8')


root = Tk()
root.title('AMAN')
root.iconbitmap('image/AMAN-LOGO.ico')
root.geometry("800x480")
root.minsize(800, 480)
root.maxsize(800, 480)
root.config(bg='#F2F7F9')

frm1 = Frame(root, bg='#1679EF', height=50)
frm1.pack(fill=X, side=TOP,pady=15)

#partie redimentionnage et creatin image logo h'en haut(AMAN BLANC)    
old_image_frm1 = Image.open('image/AMAN-BLEU.png') # importe l'image image   
resized_frm1 = old_image_frm1.resize((60, 50), Image.LANCZOS)  # redimentioner l'image    
new_image_frm1 = ImageTk.PhotoImage(resized_frm1)   # image  final    ---------- si tu veux faire des modifs cest cette Var que tu va utiliser
label1 = Label(frm1, image=new_image_frm1,highlightthickness=0,bd=0)#afficher l'image(image rahi f label)
label1.pack(expand=YES)



frm2 = Frame(root,bg='#F2F7F9',height=360,width=800)

label_msg = Label(frm2,text="Merci de bien vouloir choisir parmi\n les options suivantes en sélectionnant votre préférence",font=('Arial',18,"bold"),fg='#095CD3',bg='#F2F7F9')
label_msg.place(x=60,y=10)


btn1 = Button(frm2,text='Dépôt',font=('Arial',20),bg='#1679EF',fg='#F2F7F9',width=22,bd=0)
btn1.place(x=380,y=130)

btn2 = Button(frm2,text='Retrait',font=('Arial',20),bg='#1679EF',fg='#F2F7F9',width=22,bd=0)
btn2.place(x=380,y=230)

image_flch  = Image.open('fleche3.png')
img_flch = ImageTk.PhotoImage(image_flch)
label_flch = Label(frm2,image=img_flch,bg='#F2F7F9')
label_flch.place(x=735,y=224)


image_flch2  = Image.open('fleche3.png')
img_flch2 = ImageTk.PhotoImage(image_flch)
label_flch2 = Label(frm2,image=img_flch,bg='#F2F7F9')
label_flch2.place(x=735,y=123)



btn_srt = Button(frm2,text='Sortie',font=('Arial',15),bg='#1679EF',fg='#F2F7F9',width=7,bd=0)
btn_srt.place(x=45,y=320)


image_flch2  = Image.open('fleche3.png')
rotated_img = image_flch2.rotate(180)
resize = rotated_img.resize((35,35),Image.LANCZOS)
img_flch2 = ImageTk.PhotoImage(resize)
label_flch2 = Label(frm2,image=img_flch2,bg='#F2F7F9')
label_flch2.place(x=2,y=319)






frm2.pack()



frm3 = Frame(root, bg='#1679EF', height=30)
date=datetime.now()
label2 = Label(frm3,text=f"{date:%m-%d-%Y}  /  {date:%I:%M}",font=('Arial',12),fg='#F2F7F9',bg='#1679EF')
label2.pack(expand=YES)

frm3.pack(fill=X, side=BOTTOM)

root.mainloop()